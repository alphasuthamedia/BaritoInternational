from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_product_entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('edit/<uuid:id>', edit_product, name='edit_product'),
    path('create-mood-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    
    ## FLUTTER
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]