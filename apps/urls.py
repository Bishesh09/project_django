from django.urls import path
from apps.views import home_view,about_view,book_list_view,add_new_book,edit_book

app_name="apps"

urlpatterns=[path('home/',home_view,name='home'),
    path('about/',about_view,name='about'),
    path('book_list/',book_list_view,name="book_list"),
    path ('add_book/',add_new_book,name="add_book"),
    path('edit_book/<int:book_id>/',edit_book,name="edit_book"),
    ]