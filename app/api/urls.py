"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^language-datas/$', views.LanguageDataView.as_view()),
    re_path(r'^language-datas/(?P<short_name>(?:[^%]|%[0-9A-Fa-f]{2})+)/$', views.SingleLanguageDataRudView.as_view()),

    re_path(r'^language-labels/$', views.LanguageLabelView.as_view()),
    re_path(r'^language-labels/(?P<short_name>(?:[^%]|%[0-9A-Fa-f]{2})+)/$', views.SingleLanguageLabelRudView.as_view()),

    re_path(r'^confidentiality-datas/$', views.ConfidentialityDataView.as_view()),
    re_path(r'^confidentiality-datas/(?P<name>(?:[^%]|%[0-9A-Fa-f]{2})+)/$', views.SingleConfidentialityDataRudView.as_view()),

    re_path(r'^confidentiality-labels/$', views.ConfidentialityLabelView.as_view()),
    re_path(r'^confidentiality-labels/(?P<name>(?:[^%]|%[0-9A-Fa-f]{2})+)/$', views.SingleConfidentialityLabelRudView.as_view()),

    re_path(r'^doctype-datas/$', views.DoctypeDataView.as_view()),
    re_path(r'^doctype-datas/(?P<name>(?:[^%]|%[0-9A-Fa-f]{2})+)/$', views.SingleDoctypeDataRudView.as_view()),

    re_path(r'^doctype-labels/$', views.DoctypeLabelView.as_view()),
    re_path(r'^doctype-labels/(?P<name>(?:[^%]|%[0-9A-Fa-f]{2})+)/$', views.SingleDoctypeLabelRudView.as_view()),
]
