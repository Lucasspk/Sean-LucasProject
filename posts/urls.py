from django.urls import path
from .import views
from Component.views import BootstrapFilterView

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('blog/post/<str:pk>', views.post, name='post'),
    path('search', BootstrapFilterView, name='bootstrap'),
    path('timeline', views.timeline, name='timeline'),
    path('works', views.works, name='works'),
    path('select-component/', views.select_component, name='select_component'),
    path('create-component/<str:component_type>/', views.create_component, name='create_component'),
    path('components/', views.component_list, name='component_list'),
    path('gpu/<int:pk>/', views.gpu_detail, name='gpu_detail'),
    path('cpu/<int:pk>/', views.cpu_detail, name='cpu_detail'),
    path('psu/<int:pk>/', views.psu_detail, name='psu_detail'),
    path('motherboard/<int:pk>/', views.motherboard_detail, name='motherboard_detail'),
]