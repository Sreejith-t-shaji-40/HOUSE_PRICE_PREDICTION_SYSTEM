"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dilapp import views
from userapp import usrviews
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/', views.mypage, name='home'),
    path('mypage2/', views.mypage2, name='mypage2'),
    path('mypage4/', views.mypage4, name='home'),
    path('mypage5/', views.mypage5, name='home'),
    path('mypage3/', views.mypage3, name='home'),
    path('testview/', views.testview, name='testview'),
    path('ultra/', views.ultra, name='ultra'),
    path('new/', views.new, name='new'),
    path('test/', views.test, name='test'),
    path('final/', views.final, name='final'),
    path('calender/', views.calender, name='calender'),
    path('gallery/', views.gallery, name='gallery'),
    path('todo_list/', views.todo_list, name='todo_list'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('table/', views.table, name='table'),
    path('approval/', views.approval, name='approval'),
    path('bookings/', views.bookings, name='bookings'),
    path('inbox/', views.inbox, name='inbox'),
    path('compose/',views.compose, name='compose'),
    path('custable/',views.custable,name='custable'),
    path('gustable/',views.gustable,name='gustable'),
    path('addtable/',views.addtable,name='addtable'),
    path('deltable/',views.deltable,name='deltable'),
    path('uptable/',views.uptable,name='uptable'),
    path('logtable/',views.logtable,name='logtable'),
    path('booktable/',views.booktable,name='booktable'),

    path('usrhome/',usrviews.usrhome, name='usrhome'),
    path('predictiondetails/',usrviews.predictiondetails, name='predictiondetails'),
    path('register/',usrviews.register, name='register'),
    path('vendorreg/',usrviews.vendorreg, name='vendorreg'),
    path('customerreg/',usrviews.customerreg, name='customerreg'),
    path('guest/',usrviews.guest,name='guest'),
      path('usrlogin',usrviews.usrlogin,name='usrlogin'),
    path('',usrviews.usrlogin,name='usrlogin'),
    path('product/',usrviews.product,name='product'),
    path('addproduct/',usrviews.addproduct,name='addproduct'),
    path('deleteproduct/',usrviews.deleteproduct,name='deleteproduct'),
    path('updateproduct/',usrviews.updateproduct,name='updateproduct'),
    path('contact/',usrviews.contact,name='contact'),
    path('photogallery/',usrviews.photogallery,name='photogallery'),
    path('cart/',usrviews.cart,name='cart'),
    path('details/',usrviews.details,name='details'),
    path('booking/',usrviews.booking,name='booking'),
    path('notification/',usrviews.notification,name='notification'),
    path('usrhommenu/',usrviews.usrhommenu,name='usrhommenu'),
    path('usrvehmenu/',usrviews.usrvehmenu,name='usrvehmenu'),
    path('usraudmenu/',usrviews.usraudmenu,name='usraudmenu'),
    path('usrparmenu/',usrviews.usrparmenu,name='usrparmenu'),
    path('usrelemenu/',usrviews.usrelemenu,name='usrelemenu'),
    path('logoutview/',usrviews.logoutview,name='logoutview'),
    path('payment1/',usrviews.payment1,name='payment1'),
    path('payment2/',usrviews.payment2,name='payment2'),
    path('payment3/',usrviews.payment3,name='payment3'),
    path('payment4/',usrviews.payment4,name='payment4'),
    path('payment5/',usrviews.payment5,name='payment5'),
    path('myaccount/',usrviews.myaccount,name='myaccount')
    
    
]+staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
