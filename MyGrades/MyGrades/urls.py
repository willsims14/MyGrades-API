"""
    MyGrades URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from api import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token



router = routers.DefaultRouter()

router.register(r'student', views.StudentList)
router.register(r'school', views.SchoolList)
router.register(r'professor', views.ProfessorList)
router.register(r'course', views.CourseList)
router.register(r'assignment', views.AssignmentView)


app_name = "MyGrades"

urlpatterns = [
    # Auth / Admini
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^register$', views.register_user, name='register'),

    # Gets student by user token upon register/login
    url(r'^getstudent/(?P<token>\w+)/', views.GetStudentByTokenView.as_view()),

    # Courses
    url(r'^course/get/(?P<pk>[0-9]+)/$', views.CourseView.as_view()),
    url(r'^course/create/', views.CourseView.as_view()),
    url(r'^course/delete/(?P<pk>[0-9]+)/$', views.CourseView.as_view()),



    # Assignments
    url(r'^assignment/delete/(?P<pk>[0-9]+)/$', views.AssignmentView.as_view()),
    url(r'^assignment/create/(?P<student_course_pk>[0-9]+)/$', views.AssignmentView.as_view()),
    url(r'^course-assignments/$', views.AssignmentView.as_view()),
    url(r'^course/(?P<pk>[0-9]+)/assignments/$', views.AssignmentView.as_view()),





    url(r'^semesters/', views.SemesterViewSet.as_view()),

]

