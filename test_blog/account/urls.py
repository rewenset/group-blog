from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'login/$',
        views.user_login,
        name='login'),

    url(r'^logout/$',
        auth_views.logout,
        name='logout'),

    url(r'^logout-then-login$',
        auth_views.logout_then_login,
        name='logout_then_login'),

    url(r'^register/$',
        views.register,
        name='register'),

    url(r'^register/$',
        views.register,
        name='register'),

    url(r'^activate/(?P<key>.+)$',
        views.confirm_signup,
        name='activation'),

    url(r'^edit/$',
        views.edit,
        name='edit'),
]
