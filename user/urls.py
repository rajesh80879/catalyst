from django.urls import path
from user.views import *

urlpatterns = [
    
    path("", login_data, name="login-data"),
    path("dashboard", dashboard, name="dashboard"),
    path("users/", all_users, name="users"),

    path("logout/", logout_user, name="logout"),
    path("delete-user/<int:pk>/", del_user, name="delete-user"),

]