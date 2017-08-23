from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.usersignup, name="signup"),
    url(r'^login/$', views.userlogin, name="login"),
    url(r'^logout/$', views.userlogout, name="logout"),
    url(r'^home/$', views.main_home, name="home"),
    url(r'^ingredents/$', views.ingredents, name="ingredents"),
    url(r'^create/$', views.coffe_create, name="create"),
    url(r'^create_poweders/$', views.powders_create, name="powders_create"),
    url(r'^syrups_create/$', views.syrups_create, name="syrups_create"),
    url(r'^roast_create/$', views.roast_create, name="roast_create"),
    url(r'^bean_create/$', views.bean_create, name="bean_create"),
	url(r'^update/(?P<post_id>[\d]+)/$', views.coffe_update, name="update"),
	url(r'^delete/(?P<post_id>[\d]+)/$', views.coffe_delete, name="delete"),
	url(r'^delete_syrups/(?P<post_id>[\d]+)/$', views.syrups_delete, name="delete_syrups"),
	url(r'^delete_powders/(?P<post_id>[\d]+)/$', views.powders_delete, name="delete_powders"),
	url(r'^delete_roast/(?P<post_id>[\d]+)/$', views.roast_delete, name="delete_roast"),
	url(r'^delete_bean/(?P<post_id>[\d]+)/$', views.bean_delete, name="delete_bean"),
	url(r'^update_syrups/(?P<post_id>[\d]+)/$', views.syrups_update, name="update_syrups"),
	url(r'^update_bean/(?P<post_id>[\d]+)/$', views.bean_update, name="update_bean"),
	url(r'^update_roast/(?P<post_id>[\d]+)/$', views.roast_update, name="update_roast"),
	url(r'^update_powders/(?P<post_id>[\d]+)/$', views.powders_update, name="update_powders"),
	url(r'^create_widget/$', views.create_widget, name="create_widget"),
	url(r'^details/(?P<post_id>[\d]+)/$', views.coffe_details, name="details"),
	url(r'^admin_view/$', views.admin_view, name="admin_view"),
	url(r'^city_create/$', views.city_create, name="city_create"),
	url(r'^address_create/$', views.address_create, name="address_create"),
	





]
