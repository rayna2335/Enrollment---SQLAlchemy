from sqlalchemy import UniqueConstraint
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List  # Use this for the list of courses offered by the department

"""This is the guts of the department class that needs to be defined
regardless whether we introspect or not."""
__tablename__ = "departments"  # Give SQLAlchemy th name of the table.
abbreviation: Mapped[str] = mapped_column('abbreviation', String, nullable=False, primary_key=True)
courses: Mapped[List["Course"]] = relationship(back_populates="department")
name: Mapped[str] = mapped_column('name', String(50), nullable=False)

majors: Mapped[List["Major"]] = relationship(back_populates="department")
# __table_args__ can best be viewed as directives that we ask SQLAlchemy to
# send to the database.  In this case, that we want two separate uniqueness
# constraints (candidate keys).
__table_args__ = (UniqueConstraint("name", name="departments_uk_01"),)


def add_course(self, course):
    if course not in self.courses:
        self.courses.add(course)  # I believe this will update the course as well.

def remove_course(self, course):
    if course in self.courses:
        self.courses.remove(course)

def get_courses(self):
    return self.courses



def __str__(self):
    return (f"\n----- Department Info ------ \n"
            f"Department abbreviation: {self.abbreviation}\n"
            f" name: {self.name}\n"
            f"number course offered: {len(self.courses)}\n")

