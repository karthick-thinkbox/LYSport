from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import detail,Orderlist,logout_page,neworeder

urlpatterns = [
    
    url(r'^home/', login_required(Orderlist.as_view()),name='home_page'),
    url(r'detail/(?P<pk>.*)/(?P<currency>.*)/', login_required(detail.as_view()),name='Deatail_page'),
    
    url(r'logout/$', logout_page,name='exit_page'),
    url(r'create_order/$', neworeder,name='order_page'),
    
    ]