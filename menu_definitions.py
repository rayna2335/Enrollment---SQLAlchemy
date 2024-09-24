from Menu import Menu
from Option import Option
from constants import *
"""
This little file just has the menus declared.  Each variable (e.g. menu_main) has 
its own set of options and actions.  Although, you'll see that the "action" could
be something other than an operation to perform.

Doing the menu declarations here seemed like a cleaner way to define them.  When
this is imported in main.py, these assignment statements are executed and the 
variables are constructed.  To be honest, I'm not sure whether these are global
variables or not in Python.
"""

# The main options for operating on Departments and Courses.
menu_main = Menu('main', 'Please select one of the following options:', [
    Option("Add", "add(sess)"),
    Option("List", "list_objects(sess)"),
    Option("Delete", "delete(sess)"),
    Option("Boilerplate Data", "boilerplate(sess)"),
    Option("Commit", "sess.commit()"),
    Option("Rollback", "session_rollback(sess)"),
    Option("Exit this application", "pass")
])
# A menu for how the user will specify which student they want to access,
# given that there are three separate candidate keys for Student.
student_select = Menu('student select', 'Please select how you want to select a student:', [
    Option("ID", "ID"),
    Option("First and last name", "first/last name"),
    Option("Electronic mail", "email")
])

add_menu = Menu('add', 'Please indicate what you want to add:', [
    Option("Add Department", "add_department(sess)"),
    Option("Add Course", "add_course(sess)"),
    Option("Add Section", "add_section(sess)"),  # edited
    Option("Add Major", "add_major(sess)"),
    Option("Add Student", "add_student(sess)"),
    Option("Add Student to Major", "add_student_major(sess)"),
    Option("Add Major to Student", "add_major_student(sess)"),
    Option("Enroll by adding Section to Student", "add_section_student(sess)"), # EDITED HERE
    Option("Enroll by adding Student to Section", "add_student_section(sess)"),  # EDITED HERE
    Option("Exit", "pass")
])

delete_menu = Menu('delete', 'Please indicate what you want to delete from:', [
    Option("Delete Department", "delete_department(sess)"),
    Option("Delete Course", "delete_course(sess)"),
    Option("Delete section", "delete_section(sess)"),  # edited
    Option("Delete Major", "delete_major(sess)"),
    Option("Delete Student", "delete_student(sess)"),
    Option("Delete Student to Major", "delete_student_major(sess)"),
    Option("Delete Major to Student", "delete_major_student(sess)"),
    Option("Delete Enrollment by Student", "delete_section_student(sess)"),  # EDITED HERE
    Option("Delete Enrollment by Section", "delete_student_section(sess)"),  # EDITED HERE
    Option("Exit", "pass")
])

list_menu = Menu('list', 'Please indicate what you want to list:', [
    Option("List all Department", "list_department(sess)"),
    Option("List all Course", "list_course(sess)"),
    Option("List all sections", "list_sections(sess)"),  # edited
    Option("List all Major", "list_major(sess)"),
    Option("List all Student", "list_student(sess)"),
    Option("List all Student to Major", "list_student_major(sess)"),
    Option("List all Major to Student", "list_major_student(sess)"),
    Option("List all Students enrolled in section", "list_section_student(sess)"),  # EDITED HERE
    Option("List all Section that this student is enrolled:", "list_student_section(sess)"),  # EDITED HERE
    Option("Exit", "pass")
])

# A menu to prompt for the amount of logging information to go to the console.
debug_select = Menu('debug select', 'Please select a debug level:', [
    Option("Informational", "logging.INFO"),
    Option("Debug", "logging.DEBUG"),
    Option("Error", "logging.ERROR")
])

# A menu to prompt for whether to create new tables or reuse the old ones.
introspection_select = Menu("introspection selectt", 'To introspect or not:', [
    Option('Start all over', START_OVER),
#   Option("Reuse tables", INTROSPECT_TABLES),
    Option("Reuse without introspection", REUSE_NO_INTROSPECTION)
])