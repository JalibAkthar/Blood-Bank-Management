from django.urls import path
from BloodUserSide import views

urlpatterns = [
    path('home_page/',views.home_page,name="home_page"),
    path('donar__page/',views.donar__page,name="donar__page"),
    path('about_page/',views.about_page,name="about_page"),
    path('recipient__page/',views.recipient__page,name="recipient__page"),
    path('single_page/<int:recid>/',views.single_page,name="single_page"),
    path('single_donar/<int:donarid>/',views.single_donar,name="single_donar"),

    path('adding_donar/',views.adding_donar,name="adding_donar"),
    path('donar_save/',views.donar_save,name="donar_save"),
    path('adding_recipient/',views.adding_recipient,name="adding_recipient"),
    path('recipient_save/',views.recipient_save,name="recipient_save"),

    path('contact_page/',views.contact_page,name="contact_page"),
    path('save_contact/',views.save_contact,name="save_contact"),
    # path('delete_contact/',views.delete_contact,name="delete_contact"),

    path('',views.login_page,name="login_page"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('Signin_check/',views.Signin_check,name="Signin_check"),
    path('logout/',views.logout,name="logout"),
]