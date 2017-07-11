from django.conf.urls import url
from cms import views

urlpatterns = [
    url(r'^$', v.home, name='home')
]