from django.urls import path

from analysis.views import GetCountyDrunkDrivingView

urlpatterns = [
    path('drunkDriving/', GetCountyDrunkDrivingView.as_view())
]