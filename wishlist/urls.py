from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import return_data_XML
from wishlist.views import return_data_JSON
from wishlist.views import return_data_XML_by_id
from wishlist.views import return_data_JSON_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', return_data_XML, name='return_data_XML'),
    path('json/', return_data_JSON, name='return_data_JSON'),
    path('xml/<int:id>', return_data_XML_by_id, name='return_data_XML_by_id'),
    path('json/<int:id>', return_data_JSON_by_id, name='return_data_JSON_by_id'),
]