from django.urls import path
from .views import GetSafe, GetDisableCallTaxi, GetEnvironment, GetAccident

urlpatterns = [
    path('safe/', GetSafe.as_view()),
    path('disablecalltaxi/', GetDisableCallTaxi.as_view()),
    path('environment/', GetEnvironment.as_view()),
    path('accident/', GetAccident.as_view()),
    # path('earthquake/', GetEarthquakeView.as_view()),
    # path('awareness/', GetAwarenessView.as_view()),
    # path('building/', GetBuildingResistance.as_view()),
    # path('shelter/', GetShelter.as_view()),
    # path('calltotal/', GetCallTaxiTotal.as_view()),
    # path('waiting/', GetCallTaxiWaiting.as_view()),
    # path('callfrequency/', GetCallTaxiFrequency.as_view()),
    # path('calltime/', GetCallTaxiTime.as_view()),
    # path('callstartend/', GetCallTaxiStartEnd.as_view()),
    # path('temperature/', GetTemperature.as_view()),
    # path('dust/', GetDust.as_view()),
]