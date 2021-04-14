from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    url('^$', views.home, name='home'),
    url('^discount$', views.discount, name='discount'),
    url('^score$', views.score, name='score'),
    url('^(?P<good_id>[0-9]+)/good_info/$', views.good_info, name='good_info'),
    url('^acount$', views.acount, name='acount'),
    url('^logIn$', views.logIn, name='logIn'),
    url('^logOut$', views.logOut, name='logOut'),
    url('^create_acount$', views.create_acount, name='create_acount'),
    url('^created_acount$', views.created_acount, name='created_acount'),
    url('^electronic_menu$', views.elect_menu, name='electronic_menu'),
    url('^clothes_menu$', views.clothes_menu, name='clothes_menu'),
    url('^homeApp_menu$', views.homeApp_menu, name='homeApp_menu'),
    url('^sport_menu$', views.sport_menu, name='sport_menu'),
    url('^stationery_menu$', views.stationery_menu, name='stationery_menu'),
    url('^(?P<user_ID>[0-9]+)/create_acount_address/$', views.create_acount_address, name='create_acount_address'),
    url('^(?P<user_id>[0-9]+)/add_address/$', views.add_address, name='add_address'),
    url('^(?P<user_id>[0-9]+)/check_address/$', views.check_address, name='check_address'),
    url('^(?P<user_ID>[0-9]+)/del_address(?P<address_id>[0-9]+)/$', views.del_address, name='del_address'),
    url('^electronic$', views.electronic, name='electronic'),
    url('^lap_top$', views.lap_top, name='lap_top'),
    url('^mobile$', views.mobile, name='mobile'),
    url('^headset$', views.headset, name='headset'),
    url('^charger$', views.charger, name='charger'),
    url('^male_clothes$', views.male_clothes, name='male_clothes'),
    url('^female_clothes$', views.female_clothes, name='female_clothes'),
    url('^shirt$', views.shirt, name='shirt'),
    url('^tshirt$', views.tshirt, name='tshirt'),
    url('^male_pants$', views.male_pants, name='male_pants'),
    url('^female_pants$', views.female_pants, name='female_pants'),
    url('^manto$', views.manto, name='manto'),
    url('^blouse$', views.blouse, name='blouse'),
    url('^home_app$', views.home_app, name='home_app'),
    url('^refrigerator$', views.refrigerator, name='refrigerator'),
    url('^TV$', views.TV, name='TV'),
    url('^washing_machine$', views.washing_machine, name='washing_machine'),
    url('^sofa$', views.sofa, name='sofa'),
    url('^sport$', views.sport, name='sport'),
    url('^bicycle$', views.bicycle, name='bicycle'),
    url('^treadmill$', views.treadmill, name='treadmill'),
    url('^ball$', views.ball, name='ball'),
    url('^stationery$', views.stationery, name='stationery'),
    url('^notebook$', views.notebook, name='notebook'),
    url('^pen$', views.pen, name='pen'),
    url('^crayons$', views.crayons, name='crayons'),
    url('^eraser$', views.eraser, name='eraser'),
    url('^(?P<user_id>[0-9]+)/interesting/$', views.interesting, name='interesting'),
    url('^cart$', views.cart, name='cart'),
    url('^(?P<cart_id>[0-9]+)/del_cart/$', views.del_cart, name='del_cart'),
    url('^choose_address$', views.choose_address, name='choose_address'),
    url('^message$', views.message, name='message'),
    url('^(?P<cart_id>[0-9]+)/cart_plus/$', views.cart_plus, name='cart_plus'),
    url('^(?P<cart_id>[0-9]+)/cart_minus/$', views.cart_minus, name='cart_minus'),
    url('^all$', views.all, name='all'),
    url('^search$', views.search, name='search'),
]
