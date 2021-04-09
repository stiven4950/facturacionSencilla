# Predefined packages
from django.urls import path

# Custom packages
from .views import HomeListView

core_patterns = ([
    path('', HomeListView.as_view(), name="home"),
],'core')