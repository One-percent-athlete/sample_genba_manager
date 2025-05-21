from django.urls import path
from genba_manager_app import views

urlpatterns = [
    path('', views.home, name="home"),

    path('delete_notification/<int:notification_id>/', views.delete_notification, name="delete_notification"),
    
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('register_user/', views.register_user, name="register_user"),
    path('delete_user/<int:user_id>/', views.delete_user, name="delete_user"),
    
    path('profile_list/', views.profile_list, name="profile_list"),
    path('profile_details/<int:profile_id>/', views.profile_details, name="profile_details"),
    path('profile_genba/', views.profile_genba, name="profile_genba"),

    path('genba_list/', views.genba_list, name="genba_list"),
    path('add_genba/', views.add_genba, name="add_genba"),
    path('genba_details/<int:genba_id>/', views.genba_details, name="genba_details"),
    path('delete_genba/<int:genba_id>/', views.delete_genba, name="delete_genba"),
    
    path('report_list/', views.report_list, name="report_list"),
    path('add_report/', views.add_report, name="add_report"),
    path('report_details/<int:report_id>/', views.report_details, name="report_details"),
    path('delete_report/<int:report_id>/', views.delete_report, name="delete_report"),

    path('export_csv/', views.export_csv, name="export_csv"),
    path('export_searched/<str:keyword>/', views.export_searched, name="export_searched"),
]