from django.conf.urls import url
from . import views
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView

urlpatterns = [
    url('^$', views.index),
    url('^get_page$', views.get_page),
    url('^reset$', views.reset),
    url('^load/(?P<page_num>\d+)$', views.load),
    url('^posts_api$', views.posts_api),
    url('^create$', views.create),
    # url(r'^favicon.ico$',RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'),),name="favicon"),
]
