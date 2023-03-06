from django.urls import path
from .views import homePageView, aboutPageView, delainePageView, homePost, results

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('delaine/', delainePageView, name='delaine'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
