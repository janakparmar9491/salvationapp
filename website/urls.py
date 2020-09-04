from django.urls import path
from . import views
from .views import (
    HomePage,
    AboutPage,
    AllBlogPage,
    BlogPage,
    EventPage,
)

urlpatterns = [
    # The home page
    path('', HomePage.as_view(), name="index"),
    path('about/', AboutPage.as_view(), name="about"),
    path('blog/', AllBlogPage.as_view(), name="blog"),
    path('contact/', views.contact_page, name="contact"),
    path('events/', EventPage.as_view(), name="events"),
    # path('blog/{slug}', BlogPage.as_view(), name="blogsingle"),
]