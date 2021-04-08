from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
	path('login/', login_view, name="login"),
	path('logout/', logout_view, name="logout"),
	path('register/', registration_view, name="register"),
	path('account/', account_view, name="account"),

	# Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
	path('password_change/done/',
		auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
		name='password_change_done'
	),

	path('password_change/',
		auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'),
		name='password_change'
	),

	path('password_reset/done/',
		auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_done.html'),
		name='password_reset_done'
	),

	path('reset/<uidb64>/<token>/',
		auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
		name='password_reset_confirm'
	),

	path('password_reset/',
		auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
		name='password_reset'
	),
	
	path('reset/done/',
		auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
		name='password_reset_complete'
	),
]

