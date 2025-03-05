from django.urls import path
from .views import Get_posts, Register, Add_Comments, get_profile, update_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('blog/', Get_posts, name="get_posts"),
    path('blog/register/', Register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='autorizations/login.html'), name='login'),
    path('blog/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/profile/', Get_posts, name="profile"),
    path('blog/add_comment/<int:post_id>', Add_Comments, name='add_comment'),
    path('blog/profile', get_profile, name='profile'),
    path('blog/update_profile', update_profile, name='update_profile')
]