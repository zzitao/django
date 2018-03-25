from django.conf.urls import url
import booktest.views
app_name = 'booktest'
urlpatterns =[
    url(r'^$',booktest.views.index,name="index"),
    #url(r'^(\d+)$',booktest.views.detail),
    url(r'^getTest1/$',booktest.views.getTest1),
    url(r'^getTest2/$',booktest.views.getTest2),
    url(r'^getTest3/$',booktest.views.getTest3),
    url(r'^postTest1/$',booktest.views.postTest1),
    url(r'^postTest2/$',booktest.views.postTest2),
    url(r'^cookieTest/$',booktest.views.cookieTest),
    url(r'^sessionTest1/$',booktest.views.sessionTest1),
    url(r'^sessionTest2/$',booktest.views.sessionTest2),
    url(r'^sessionTest3/$',booktest.views.sessionTest3),
    url(r'^sessionTest2_handle/$',booktest.views.sessionTest2_handle),
    url(r'^\d+/$',booktest.views.show,name="show"),
    url(r'^base1/$',booktest.views.base1),
    url(r'^base2/$',booktest.views.base2),
]