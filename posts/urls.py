from django.urls import path
from posts import views

app_name = "post"
urlpatterns = [
    path('' , views.index, name="index"),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/',views.post_view_details,name = "post_view"),
    path('category/' , views.category_view , name="category_view"),
    path('tag/<slug:tag_slug>' , views.index , name="tag_view"),
    path('search/' , views.index , name="search"),
    path('share/<int:year>/<int:month>/<int:day>/<slug:slug>/' , views.share , name="share"),





]
