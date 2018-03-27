from django.conf.urls import include,url
import df_user.views

urlpatterns = [
    url(r'^register/$',df_user.views.register),
    url(r'^register_handle/$',df_user.views.register_handle),
    url(r'^login/$',df_user.views.login),
    url(r'^register_exist/',df_user.views.register_exist),
    url(r'^login_handle/$',df_user.views.login_handle),
    url(r'^user_center_info',df_user.views.info),
    url(r'^user_center_order',df_user.views.order),
    url(r'^user_center_site',df_user.views.site),
]