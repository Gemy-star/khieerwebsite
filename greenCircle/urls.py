from django.urls import path
from . import views

urlpatterns = [
    path('greenCircle', views.greenCircle, name='green-circle'),
    path('greenCourse/<int:pk>', views.greenCircleCourses, name='green-courses'),
    path('greenTrainer/<int:pk>', views.green_trainer_details, name='green-trainer'),
    path('greenCourse/add/<int:pk>', views.CourseRequestView.as_view(), name='green-add-user'),
    path('greenCircle/add', views.add_greenCourse, name='register-greenCircle'),
    path('greenCircle/list', views.Greencourses_list, name='all-green'),
    path('greenCircle/requests', views.Greenrequest_list, name='all-requests'),
    path('greenCircle/trainers', views.Greentrainers_list, name='all-trainers'),

]
