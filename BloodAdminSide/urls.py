from django.urls import path
from BloodAdminSide import views

urlpatterns =[
    path('iindexx/',views.iindexx,name="iindexx"),

    path('donar_page/',views.donar_page,name="donar_page"),
    path('save_donar/',views.save_donar,name="save_donar"),
    path('display_donar/',views.display_donar,name="display_donar"),
    path('edit_donar/<int:dataid>/',views.edit_donar,name="edit_donar"),
    path('update_donar/<int:dataid>/',views.update_donar,name="update_donar"),
    path('delete_donar/<int:dataid>/',views.delete_donar,name="delete_donar"),

    path('recipient_page/',views.recipient_page,name="recipient_page"),
    path('save_recipient/',views.save_recipient,name="save_recipient"),
    path('display_recipient/',views.display_recipient,name="display_recipient"),
    path('edit_recipient/<int:dataid>/',views.edit_recipient,name="edit_recipient"),
    path('update_recipient/<int:dataid>/',views.update_recipient,name="update_recipient"),
    path('delete_recipient/<int:dataid>/',views.delete_recipient,name="delete_recipient"),

    path('',views.adminlogin_page,name="adminlogin_page"),
    path('adminlogin_save/',views.adminlogin_save,name="adminlogin_save"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    path('display_contact/',views.display_contact,name="display_contact"),
    path('delete_contact/<int:dataid>/',views.delete_contact,name="delete_contact"),
]