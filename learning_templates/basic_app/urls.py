from django.conf.urls import url
from basic_app import views

# Template tagging
# getting link to setting urls when the basic_app.urls called
app_name = "basic_app"

urlpatterns = [
	url(r'^relative/$',views.relative, name = "relative"),
	url(r'^other/$',views.other, name = 'other'),
]