from django.shortcuts import render
from django.urls import path
from . import views
from MySite import settings
from django.conf.urls.static import static

urlpatterns=[

    path('',views.post_list,name='post_list'),
    path('contact/',views.contact,name='contact'),
    path('Resume/',views.pdf_view,name='pdf'),
    path('blog/',views.blog,name='blog'),
    path('blog/<slug:menu>/',views.detail,name='detail'),
]


if settings.DEBUG:
    urlpatterns+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
