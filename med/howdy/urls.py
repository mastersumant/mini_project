# howdy/urls.py
from django.conf.urls import url
from howdy import view


urlpatterns = [
   url('', view.check_med, name = 'check_med')]