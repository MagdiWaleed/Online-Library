from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import JsonResponse
from .models import SingleBookModel
from django.views.decorators.csrf import csrf_exempt



# function get_template(func_name.html) 

def Admin_about(request):
  template = loader.get_template('Admin_about.html')
  return HttpResponse(template.render())

def Admin_add_new_book(request):
  template = loader.get_template('Admin_add_new_book.html')
  return HttpResponse(template.render())

def Admin_books_screen(request):
  template = loader.get_template('Admin_books_screen.html')
  return HttpResponse(template.render())

def Admin_brrowed_books(request):
  template = loader.get_template('Admin_brrowed_books.html')
  return HttpResponse(template.render())

def Admin_main(request):
  template = loader.get_template('Admin_main.html')
  return HttpResponse(template.render())

def Admin_my_information(request):
  template = loader.get_template('Admin_my_information.html')
  return HttpResponse(template.render())

def Admin_searching(request):
  template = loader.get_template('Admin_searching.html')
  return HttpResponse(template.render())

def Admin_single_book(request):
  template = loader.get_template('Admin_single_book.html')
  return HttpResponse(template.render())

def Admin_single_user_author(request):
  template = loader.get_template('Admin_single_user_author.html')
  return HttpResponse(template.render())

def Admin_statistics(request):
  template = loader.get_template('Admin_statistics.html')
  return HttpResponse(template.render())

def Admin_users_authors(request):
  template = loader.get_template('Admin_users_authors.html')
  return HttpResponse(template.render())

def LoginScreen(request):
  template = loader.get_template('LoginScreen.html')
  return HttpResponse(template.render())

def SignupScreen(request):
  template = loader.get_template('SignupScreen.html')
  return HttpResponse(template.render())

def User_about(request):
  template = loader.get_template('User_about.html')
  return HttpResponse(template.render())

def User_main(request):
  template = loader.get_template('User_main.html')
  return HttpResponse(template.render())

def User_my_books(request):
  template = loader.get_template('User_my_books.html')
  return HttpResponse(template.render())

def User_my_information(request):
  template = loader.get_template('User_my_information.html')
  return HttpResponse(template.render())

def User_search(request):
  template = loader.get_template('User_search.html')
  return HttpResponse(template.render())

def User_SingleBook(request):
  template = loader.get_template('User_SingleBook.html')
  return HttpResponse(template.render())

@csrf_exempt 
def add_new_book(request):
  if request.method == 'POST':
      book_name = request.POST.get('book_name')
      book_description = request.POST.get('book_description')
      author_name = request.POST.get('author_name')
      about_author = request.POST.get('about_author')
      category = request.POST.get('category')
      image = request.FILES.get('image')
      # Save data to database
      new_book = SingleBookModel.objects.create(
          book_name=book_name,
          book_description=book_description,
          author_name=author_name,
          about_author=about_author,
          category=category,
          image=image )
      return JsonResponse({'status': 'success', 'message': 'Book added successfully'})
  return JsonResponse({'status': 'error', 'message': 'Invalid request method'})




