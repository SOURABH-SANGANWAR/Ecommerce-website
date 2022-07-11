from django.contrib import admin
from django.urls import path
from .views import detail_view,detail_view_Category,search
app_name = 'Products'


urlpatterns = [
    path('<int:id>/', detail_view,name="detail_view"),
    path('<int:id>/<int:seller>/', detail_view,name="detail_view_seller"),
    path('filter/<int:id>/', search,name="detail_view_filter"),
    path('search/<str:search>/', search,name="search"),
    path('search//', search,name="search"),
    path('search/<str:search>/<int:id1>', search,name="search_filter"),

    # path('update/<int:id>/', cview.as_view(),name = "update_view"),
    # path('delete/<int:id>/', dview.as_view(),name = "delete_view"),
    # path('create/', cview.as_view(), name = "create_view"),
    # path('',lview.as_view(), name = "list_view"),
    # path('/abcd',Myfun, name = "funt"),
]