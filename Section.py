from orm_base import Base
from db_connection import engine
from IntrospectionFactory import IntrospectionFactory
from sqlalchemy import UniqueConstraint, ForeignKeyConstraint, PrimaryKeyConstraint, CheckConstraint, Identity
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship, column_property
from sqlalchemy import Table
from Department import Department
from constants import START_OVER, REUSE_NO_INTROSPECTION, INTROSPECT_TABLES
from Course import Course
from sqlalchemy import Time
from typing import List
from datetime import datetime
from Enrollment import Enrollment


class Section(Base):  # this runs when user selects start over ot reuse
    __tablename__ = 'sections'
    course: Mapped[Course] = relationship(back_populates="section")

    departmentAbbreviation: Mapped[str] = mapped_column('department_abbreviation', String(10), primary_key=True)
    courseNumber: Mapped[int] = mapped_column('course_number', Integer, primary_key=True)
    sectionNumber: Mapped[int] = mapped_column('section_number', Integer, primary_key=True)
    semester: Mapped[str] = mapped_column('semester', String(10), nullable=False, primary_key=True)
    sectionYear: Mapped[int] = mapped_column('section_year', Integer, nullable=False, primary_key=True)
    building: Mapped[str] = mapped_column('building', String(6), nullable=False)
    room: Mapped[int] = mapped_column('room', Integer, nullable=False)
    schedule: Mapped[str] = mapped_column('schedule', String(6), nullable=False)
    startTime: Mapped[Time] = mapped_column('start_time', Time)
    instructor: Mapped[str] = mapped_column('instructor', String(80), nullable=False)

    #surrogate key
    sectionID: Mapped[int] = mapped_column('section_id', Integer, Identity(start=1, cycle=True), primary_key=True)
    students: Mapped[List["Enrollment"]] = relationship(back_populates="section",
                                                          cascade="all, save-update, delete-orphan")

    # unique constraints ensures that we don't get more than 1 section meeting in the same room at the same time
    __table_args__ = (
        UniqueConstraint("section_year", "semester", "schedule", "start_time", "building", "room",
                         name='sections_uk_01'),
        UniqueConstraint("section_year", "semester", "schedule", "start_time", "instructor", name="sections_uk_02"),
        UniqueConstraint('section_id', name="sections_uk_03"),
        ForeignKeyConstraint([departmentAbbreviation, courseNumber], [Course.departmentAbbreviation, Course.courseNumber]),
        CheckConstraint("semester IN ('Fall', 'Spring', 'Winter', 'Summer I', 'Summer II')", name="valid_semester"),
        CheckConstraint("building IN ('VEC', 'ECS', 'EN2', 'EN3', 'EN4', 'ET', 'SSPA')", name="valid_building"),
        CheckConstraint("schedule IN ('MW', 'TuTh', 'MWF', 'F', 'S')", name="valid_schedule")
    )

    def __init__(self, course: Course, department: Department,departmentAbbreviation: str, courseNumber: int, sectionNumber: int, semester: str,
                 sectionYear: int, building: str, room: str, schedule: str, startTime: Time, instructor: str):
        #self.set_department(course)
        self.departmentAbbreviation = departmentAbbreviation
        self.courseNumber = courseNumber
        self.sectionNumber = sectionNumber
        self.semester = semester
        self.sectionYear = sectionYear
        self.building = building
        self.room = room
        self.schedule = schedule
        self.startTime = startTime
        self.instructor = instructor

    def set_department(self, course: Course):
        """
        Accept a new department without checking for any uniqueness.
        I'm going to assume that either a) the caller checked that first
        and/or b) the database will raise its own exception.
        :param department:  The new department for the course.
        :return:            None
        """
        self.departmentAbbreviation = course.departmentAbbreviation
        self.courseNumber = course.courseNumber

    def add_student(self, student):
        """Add a new student to the list of students in the section."""
        for next_student in self.students:
            if next_student.student == student:
                return
        enrollment = Enrollment(student, self)
        student.sections.append(enrollment)
        self.students.append(enrollment)


    def remove_enrollment(self, student):
        for next_enrollment in self.students:
            if next_enrollment.student == student:
                self.students.remove(next_enrollment)
                return


    def __str__(self):
        return (f"\n----- Section Info ------ \n"
                f"Department Abbreviation: {self.departmentAbbreviation}\n "
                f"Course Number: {self.courseNumber}\n"
                f"Section Number: {self.sectionNumber}\n"
                f"Semester: {self.semester}\n"
                f"Section Year: {self.sectionYear}\n"
                f"Building: {self.building}\n"
                f"Room: {self.room}\n"
                f"Schedule: {self.schedule}\n"
                f"Start Time: {self.startTime}\n"
                f"Instructor: {self.instructor}\n")

