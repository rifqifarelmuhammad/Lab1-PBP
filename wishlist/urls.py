import imp
from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import return_data_XML
from wishlist.views import return_data_JSON
from wishlist.views import return_data_XML_by_id
from wishlist.views import return_data_JSON_by_id
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user
from wishlist.views import show_wishlist_ajax
from wishlist.views import create_wishlist_ajax

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', return_data_XML, name='return_data_XML'),
    path('json/', return_data_JSON, name='return_data_JSON'),
    path('xml/<int:id>', return_data_XML_by_id, name='return_data_XML_by_id'),
    path('json/<int:id>', return_data_JSON_by_id, name='return_data_JSON_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('ajax/submit', create_wishlist_ajax, name='create_wishlist_ajax'),
]