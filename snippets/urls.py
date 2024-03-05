from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='name'),
    path('language/<str:language>/', views.languageShow, name='languageShow'),
    path('snippets/all/', views.allSnippets.as_view(), name='allSnippets'),
    path('snippet/detail/<int:pk>/', views.DetailCode.as_view(), name='DetailCode'),
    path('language/tag/<str:hashtag_name>/', views.hashtag, name='hashtag'),
    path('search/', views.search, name='Search'),
    path('snippets/new/', views.new_post, name='new_snippet'),
    path('snippets/update/<int:snippet_id>', views.updateSnippets, name='update_snippet'),
]