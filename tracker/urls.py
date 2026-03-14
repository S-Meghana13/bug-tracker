# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              # Landing / Home
    path('signup/', views.signup_user, name='signup'), # Signup page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard after login
    path('add_project/', views.add_project, name='add_project'),
    path('add_bug/', views.add_bug, name='add_bug'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('project/update/<int:project_id>/', views.update_project, name='update_project'),
    path('project/delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('bug/update/<int:bug_id>/', views.update_bug, name='update_bug'),
    path('bug/delete/<int:bug_id>/', views.delete_bug, name='delete_bug'),



]
#     path('add_project/', views.add_project, name='add_project'),
#     path('add_bug/', views.add_bug, name='add_bug'),
#     path('login/', views.login_user, name='login'),
#     path('logout/', views.logout_user, name='logout'),



# ]