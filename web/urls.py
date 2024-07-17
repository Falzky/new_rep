from django.urls import path
from web.views import home, hello, stud, newstud

urlpatterns= [
    path('', home, name="home"),
    path('greet/<str:name>', hello),
    path('students',stud),
    path('new_students', newstud, name="gold")
]

