from .serializer_student import StudentSerializer, AdminStudentSerializer
from .serializer_school import SchoolSerializer
from .serializer_professor import ProfessorSerializer
from .serializer_course import CourseSerializer
from .serializer_student_course import StudentCourseSerializer
from .serializer_assignment import AssignmentSerializer

__all__ = [
    'StudentSerializer',
    'AdminStudentSerializer',
    'SchoolSerializer',
    'ProfessorSerializer',
    'CourseSerializer',
    'StudentCourseSerializer',
    'AssignmentSerializer'
]