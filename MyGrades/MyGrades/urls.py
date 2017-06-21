"""
    MyGrades URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from api import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token



router = routers.DefaultRouter()

router.register(r'students', views.StudentList)
router.register(r'schools', views.SchoolList)
router.register(r'professors', views.ProfessorList)
router.register(r'courses', views.CourseList)
router.register(r'assignments', views.AssignmentView)


app_name = "MyGrades"

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^register$', views.register_user, name='register'),

    url(r'^getstudent/(?P<token>\w+)/', views.GetStudentByTokenView.as_view()),

    url(r'^student-course/', views.StudentCoursesViewSet.as_view()),
    url(r'^create-course/', views.CourseView.as_view()),
    url(r'^student-course-delete/(?P<pk>[0-9]+)/$', views.DeleteCourseViewSet),
    
    url(r'^create-assignment/(?P<student_course_pk>[0-9]+)/$', views.AssignmentView.as_view()),
    url(r'^student-course-assignments/', views.StudentCourseAssignmentsViewSet.as_view()),
    url(r'^student-assignment-delete/(?P<pk>[0-9]+)/$', views.AssignmentView.as_view()),



    url(r'^semesters/', views.SemesterViewSet.as_view()),

]

