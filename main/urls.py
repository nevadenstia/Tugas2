from django.urls import path
from main.views import add_product_ajax, create_product_flutter, get_product_json, show_main, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, delete_item, add_item, subtract_item, get_total_stock

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('main/', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),  
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('main/add_item/<int:item_id>/', add_item, name='add_item'),
    path('main/subtract_item/<int:item_id>/', subtract_item, name='subtract_item'),
    path('main/delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax'),
    path('get_total_stock/', get_total_stock, name='get_total_stock'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),

]