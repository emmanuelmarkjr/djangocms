from django.conf.urls import url
from . import views as v

urlpatterns = [
    url(r'^$', v.home, name='home')
]