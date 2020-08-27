from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from user.views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, AddressView

urlpatterns = [
    # url(r'^register$',views.register, name='register'),  # 注册
    # url(r'^register_handle$',views.register_handle, name='register_handle'),  # 注册
    url(r'^register$', RegisterView.as_view(), name='register'),  # 注册
    # 补获token，作为关键字
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='avtive'),  # 激活
    url(r'^login$', LoginView.as_view(), name='login'),  # 登录
    url(r'^logout$', LogoutView.as_view(), name='logout'),  # 注销登录

    # url(r'^$', login_required(UserInfoView.as_view()), name='user'),  # 用户中心
    # url(r'^order', login_required(UserOrderView.as_view()), name='order'),  # 用户订单
    # url(r'^address', login_required(AddressView.as_view()), name='address'),  # 用户地址

    url(r'^$', UserInfoView.as_view(), name='user'),  # 用户中心
    url(r'^order/(?P<page>\d+)/(?P<order_status>\d+)$', UserOrderView.as_view(), name='order'),  # 用户订单
    url(r'^address', AddressView.as_view(), name='address'),  # 用户地址
]
