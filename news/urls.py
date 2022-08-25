
from django.urls import path
from .views import NewsView, GetNewsPolicyTotal, GetNewsPolicy


urlpatterns = [
    path(r'', NewsView.as_view(), name='dataType'),
    path('newspolicytotal/', GetNewsPolicyTotal.as_view()),
    path('newspolicy/', GetNewsPolicy.as_view()),
]
