from .view_student import StudentList, StudentDetailViewSet
from .view_student_course import StudentCoursesViewSet, StudentCourseAssignmentsViewSet, DeleteCourseViewSet
from .view_register import register_user
from .view_logout import user_logout
from .view_school import SchoolList
from .view_professor import ProfessorList
from .view_course import CourseList, CourseDetail
from .view_assignment import AssignmentList
from .view_create_course import CourseView


__all__ = [
    'StudentList',
    'register_user',
    'ListStudents',
    'SchoolList',
    'ProfessorList',
    'StudentList',
    'CourseList',
    'CourseDetail',
    'StudentDetailViewSet',
    'StudentCoursesViewSet',
    'AssignmentList',
    'StudentCourseAssignmentsViewSet',
    'CourseView',
    'DeleteCourseViewSet'
]