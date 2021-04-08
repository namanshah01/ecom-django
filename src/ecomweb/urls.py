"""ecomweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views
from users.views import (
	registration_view,
	logout_view,
	login_view,
	account_view,
	must_authenticate_view,
	# profile_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
	# path('', include('users.urls')),
	path('', include('store.urls')),

	# other
	path('login/', login_view, name="login"),
	path('logout/', logout_view, name="logout"),
	path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
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

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
