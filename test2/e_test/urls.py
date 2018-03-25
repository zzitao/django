from django.conf.urls import url
import e_test.views
app_name = 'e_test'
urlpatterns =[
    url(r'^$',e_test.views.index,name="index"),
    url(r'^base/$',e_test.views.base),
    url(r'^base_user/$',e_test.views.base_user),
    url(r'^base_goods$',e_test.views.base_goods),
    url(r'^user1/$',e_test.views.user1),
    url(r'^user2/$',e_test.views.user2),
    url(r'^csrf1/$',e_test.views.crrf1),
    url(r'^csrf2/$',e_test.views.csrf2),
    ]