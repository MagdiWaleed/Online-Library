from django.urls import path
from . import views

# Admin_about ,Admin_add_new_book ,Admin_books_screen ,Admin_brrowed_books ,Admin_main ,Admin_my_information ,Admin_searching ,Admin_single_book ,Admin_single_user_author ,Admin_statistics ,Admin_users_authors ,LoginScreen ,SignupScreen ,User_about, User_main
# User_my_books ,User_my_information ,User_search , User_SingleBook

urlpatterns = [
    path('', views.User_main),
    path('/Admin_about/', views.Admin_about),
    path('/Admin_add_new_book/', views.Admin_add_new_book),
    path('/Admin_books_screen/', views.Admin_books_screen),
    path('/Admin_brrowed_books/', views.Admin_brrowed_books),
    path('/Admin_main/', views.Admin_main),
    path('/Admin_my_information/', views.Admin_my_information),
    path('/Admin_searching/', views.Admin_searching),
    path('/Admin_single_book/', views.Admin_single_book),
    path('/Admin_single_user_author/', views.Admin_single_user_author),
    path('/Admin_statistics/', views.Admin_statistics),
    path('/Admin_users_authors/', views.Admin_users_authors),
    path('/LoginScreen/', views.LoginScreen),
    path('/SignupScreen/', views.SignupScreen),
    path('/User_about/', views.User_about),
    path('/User_main/', views.User_main),
    path('/User_my_books/', views.User_my_books),
    path('/User_my_information/', views.User_my_information),
    path('/User_search/', views.User_search),
    path('/User_SingleBook/', views.User_SingleBook),

    path('/Admin_about', views.Admin_about),
    path('/Admin_add_new_book', views.Admin_add_new_book),
    path('/Admin_books_screen', views.Admin_books_screen),
    path('/Admin_brrowed_books', views.Admin_brrowed_books),
    path('/Admin_main', views.Admin_main),
    path('/Admin_my_information', views.Admin_my_information),
    path('/Admin_searching', views.Admin_searching),
    path('/Admin_single_book', views.Admin_single_book),
    path('/Admin_single_user_author', views.Admin_single_user_author),
    path('/Admin_statistics', views.Admin_statistics),
    path('/Admin_users_authors', views.Admin_users_authors),
    path('/LoginScreen', views.LoginScreen),
    path('/SignupScreen', views.SignupScreen),
    path('/User_about', views.User_about),
    path('/User_main', views.User_main),
    path('/User_my_books', views.User_my_books),
    path('/User_my_information', views.User_my_information),
    path('/User_search', views.User_search),
    path('/User_SingleBook', views.User_SingleBook),

    path('/Admin_about.html/', views.Admin_about),
    path('/Admin_add_new_book.html/', views.Admin_add_new_book),
    path('/Admin_books_screen.html/', views.Admin_books_screen),
    path('/Admin_brrowed_books.html/', views.Admin_brrowed_books),
    path('/Admin_main.html/', views.Admin_main),
    path('/Admin_my_information.html/', views.Admin_my_information),
    path('/Admin_searching.html/', views.Admin_searching),
    path('/Admin_single_book.html/', views.Admin_single_book),
    path('/Admin_single_user_author.html/', views.Admin_single_user_author),
    path('/Admin_statistics.html/', views.Admin_statistics),
    path('/Admin_users_authors.html/', views.Admin_users_authors),
    path('/LoginScreen.html/', views.LoginScreen),
    path('/SignupScreen.html/', views.SignupScreen),
    path('/User_about.html/', views.User_about),
    path('/User_main.html/', views.User_main),
    path('/User_my_books.html/', views.User_my_books),
    path('/User_my_information.html/', views.User_my_information),
    path('/User_search.html/', views.User_search),
    path('/User_SingleBook.html/', views.User_SingleBook),


    path('/Admin_about.html', views.Admin_about),
    path('/Admin_add_new_book.html', views.Admin_add_new_book),
    path('/Admin_books_screen.html', views.Admin_books_screen),
    path('/Admin_brrowed_books.html', views.Admin_brrowed_books),
    path('/Admin_main.html', views.Admin_main),
    path('/Admin_my_information.html', views.Admin_my_information),
    path('/Admin_searching.html', views.Admin_searching),
    path('/Admin_single_book.html', views.Admin_single_book),
    path('/Admin_single_user_author.html', views.Admin_single_user_author),
    path('/Admin_statistics.html', views.Admin_statistics),
    path('/Admin_users_authors.html', views.Admin_users_authors),
    path('/LoginScreen.html', views.LoginScreen),
    path('/SignupScreen.html', views.SignupScreen),
    path('/User_about.html', views.User_about),
    path('/User_main.html', views.User_main),
    path('/User_my_books.html', views.User_my_books),
    path('/User_my_information.html', views.User_my_information),
    path('/User_search.html', views.User_search),
    path('/User_SingleBook.html', views.User_SingleBook),


    path('Admin_about/', views.Admin_about),
    path('Admin_add_new_book/', views.Admin_add_new_book),
    path('Admin_books_screen/', views.Admin_books_screen),
    path('Admin_brrowed_books/', views.Admin_brrowed_books),
    path('Admin_main/', views.Admin_main),
    path('Admin_my_information/', views.Admin_my_information),
    path('Admin_searching/', views.Admin_searching),
    path('Admin_single_book/', views.Admin_single_book),
    path('Admin_single_user_author/', views.Admin_single_user_author),
    path('Admin_statistics/', views.Admin_statistics),
    path('Admin_users_authors/', views.Admin_users_authors),
    path('LoginScreen/', views.LoginScreen),
    path('SignupScreen/', views.SignupScreen),
    path('User_about/', views.User_about),
    path('User_main/', views.User_main),
    path('User_my_books/', views.User_my_books),
    path('User_my_information/', views.User_my_information),
    path('User_search/', views.User_search),
    path('User_SingleBook/', views.User_SingleBook),

    path('Admin_about', views.Admin_about),
    path('Admin_add_new_book', views.Admin_add_new_book),
    path('Admin_books_screen', views.Admin_books_screen),
    path('Admin_brrowed_books', views.Admin_brrowed_books),
    path('Admin_main', views.Admin_main),
    path('Admin_my_information', views.Admin_my_information),
    path('Admin_searching', views.Admin_searching),
    path('Admin_single_book', views.Admin_single_book),
    path('Admin_single_user_author', views.Admin_single_user_author),
    path('Admin_statistics', views.Admin_statistics),
    path('Admin_users_authors', views.Admin_users_authors),
    path('LoginScreen', views.LoginScreen),
    path('SignupScreen', views.SignupScreen),
    path('User_about', views.User_about),
    path('User_main', views.User_main),
    path('User_my_books', views.User_my_books),
    path('User_my_information', views.User_my_information),
    path('User_search', views.User_search),
    path('User_SingleBook', views.User_SingleBook),

    path('Admin_about.html/', views.Admin_about),
    path('Admin_add_new_book.html/', views.Admin_add_new_book),
    path('Admin_books_screen.html/', views.Admin_books_screen),
    path('Admin_brrowed_books.html/', views.Admin_brrowed_books),
    path('Admin_main.html/', views.Admin_main),
    path('Admin_my_information.html/', views.Admin_my_information),
    path('Admin_searching.html/', views.Admin_searching),
    path('Admin_single_book.html/', views.Admin_single_book),
    path('Admin_single_user_author.html/', views.Admin_single_user_author),
    path('Admin_statistics.html/', views.Admin_statistics),
    path('Admin_users_authors.html/', views.Admin_users_authors),
    path('LoginScreen.html/', views.LoginScreen),
    path('SignupScreen.html/', views.SignupScreen),
    path('User_about.html/', views.User_about),
    path('User_main.html/', views.User_main),
    path('User_my_books.html/', views.User_my_books),
    path('User_my_information.html/', views.User_my_information),
    path('User_search.html/', views.User_search),
    path('User_SingleBook.html/', views.User_SingleBook),


    path('Admin_about.html', views.Admin_about),
    path('Admin_add_new_book.html', views.Admin_add_new_book),
    path('Admin_books_screen.html', views.Admin_books_screen),
    path('Admin_brrowed_books.html', views.Admin_brrowed_books),
    path('Admin_main.html', views.Admin_main),
    path('Admin_my_information.html', views.Admin_my_information),
    path('Admin_searching.html', views.Admin_searching),
    path('Admin_single_book.html', views.Admin_single_book),
    path('Admin_single_user_author.html', views.Admin_single_user_author),
    path('Admin_statistics.html', views.Admin_statistics),
    path('Admin_users_authors.html', views.Admin_users_authors),
    path('LoginScreen.html', views.LoginScreen),
    path('SignupScreen.html', views.SignupScreen),
    path('User_about.html', views.User_about),
    path('User_main.html', views.User_main),
    path('User_my_books.html', views.User_my_books),
    path('User_my_information.html', views.User_my_information),
    path('User_search.html', views.User_search),
    path('User_SingleBook.html', views.User_SingleBook),

    path('/addBook/', views.addBook, name='addBook'),
    path('addBook/', views.addBook, name='addBook'),
    path('addBook', views.addBook, name='addBook'),
    path('/addBook', views.addBook, name='addBook'),

]