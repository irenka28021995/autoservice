from django.urls import path
from autoservice import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('create_order/', views.create_order, name='create_order'),
    path('client_orders/', views.client_orders, name='orders'),
    path('contact/', views.contact, name='contact'),
    path('<int:pk>/update', views.ClientUpdateApi.as_view(), name='update_order'),
    path('<int:pk>/delete', views.ClientDeleteApi.as_view(), name='delete_order'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)