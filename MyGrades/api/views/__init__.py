from .view_student import StudentList, GetStudentByTokenView
from .view_student_course import StudentCoursesViewSet, StudentCourseDetail
from .view_register import register_user
from .view_logout import user_logout
from .view_school import SchoolList
from .view_professor import ProfessorList
from .view_course import CourseList, CourseDetail
from .view_assignment import AssignmentView
from .view_create_course import CourseView
from .view_semester import SemesterViewSet


__all__ = [
    'StudentList',
    'register_user',
    'ListStudents',
    'SchoolList',
    'ProfessorList',
    'StudentList',
    'CourseList',
    'CourseDetail',
    'CourseView',
    'DeleteCourseViewSet',
    'GetStudentByTokenView',
    'AssignmentView',
    'SemesterViewSet',
    'StudentCourseDetail'
]