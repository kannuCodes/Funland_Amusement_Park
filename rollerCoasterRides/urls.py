from django.urls import path
from rollerCoasterRides import views 
urlpatterns=[
    path('',views.home,name='home'),
    path("roller_coaster/",views.index , name="rollerCoaster"),
    path("drop_tower/", views.drop_tower, name="drop_tower"),
    path("bumper_cars/", views.bumper_cars, name="bumper_cars"),
    path("ferris_wheel/", views.ferris_wheel, name="ferris_wheel"),
    path("water_slides/", views.water_slides, name="water_slides"),
    path("rain_dance/", views.rain_dance, name="rain_dance"),
    path("chatbot/", views.chatbot_response, name="chatbot")
]