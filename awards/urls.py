from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^search/', views.search,name = 'search'),
    url(r'^new/project$',views.newproject, name='newproject'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^project/(\d+)', views.project, name='project'),
    url(r'^new/rating/(\d+)',views.newrating, name='newrating'), 
    url(r'^new/profile$',views.newprofile, name='newprofile'),
    url(r'^mail$',views.mail,name='mail'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^subscribe/', views.subscribe, name='subscribe'),
    url(r'^myprojects/', views.myprojects, name='myprojects'),
    url(r'^password/', views.password, name='password'),
    url(r'^searchme/', views.searchme, name='searchme'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)