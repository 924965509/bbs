from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'(\w+)/p/(\d+)', views.article_detail),
    url(r'(\w+)', views.home),

]
