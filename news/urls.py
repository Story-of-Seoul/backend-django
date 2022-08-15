


from django.urls import path
from .views import NewsView


urlpatterns = [
    path(r'', NewsView.as_view(), name='dataType'),    
]
