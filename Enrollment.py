from sqlalchemy import UniqueConstraint, ForeignKey
from IntrospectionFactory import IntrospectionFactory
from db_connection import engine
from orm_base import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship, column_property
from sqlalchemy import Table


class Enrollment(Base):
    """ Association class between Section and Student"""
    __tablename__ = "enrollments"

    student: Mapped["Student"] = relationship(back_populates="sections")
    section: Mapped["Section"] = relationship(back_populates="students")

    studentId: Mapped[int] = mapped_column('student_id', ForeignKey("students.student_id"), primary_key=True)
    sectionId = mapped_column('section_id', ForeignKey('sections.section_id'), primary_key=True)


    def __init__(self, student, section):
        self.student = student
        self.section = section
        self.sectionId = section.sectionID  # surrogate

    def __str__(self):
        return f"Student section - student: {self.student} section: {self.section}"
