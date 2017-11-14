from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views


urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    #url(r'^$', views.dashboard, name='dashboard'),

    #url(r'^register/$', views.register, name='register'),
    #url(r'^edit/$', views.edit, name='edit'),

    # login / logout urls
    url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),
    #url(r'^logout/$', logout,{'template_name': 'logout.html'}, name='mysite_logout'),
    #url(r'^logout-then-login/$',logout-then-login,{'template_name': 'logout-then-login.html'}, name='mysite_logout-then-login')

    # change password urls
   # url(r'^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
   # url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),

    # restore password urls
    #url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    #url(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
]