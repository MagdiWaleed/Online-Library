from django.shortcuts import render
from .models import Book
from django.http import JsonResponse 
from profileModel.models import ProfileModel 
from django.utils.timezone import now
from django.conf import settings
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from filtering.views import removeSpaces
import os
from django.http import HttpResponse


# Create your views here.
def getBooksList(request):
    return render(request, 'books/main.html')

def getStatistics(request):
    books= Book.objects.all()
    authors=[]
    users=ProfileModel.objects.all()
    for book in books:
        authors.append(book.author_name)
    authors= [removeSpaces(t)for t in authors]
    authors=set(authors)
    counter=0
    for user in users:
        borrowed = Book.objects.filter(user=user)
        for book in borrowed:
            counter+=1
    context={
        "num_books":str(len(books)),
        "num_authors":str(len(authors)),
        "num_users":str(len(users)),
        "num_borrowed":str(counter),
    }
    return render(request,'books/statistics.html',context)




def getBooksData(request):
    books= Book.objects.all()
    trending_data=[]
    latest_data=[]
    # i=0
    # j=0

    for book in books:
        isborrowed =""
        if book.user== None:
            isborrowed='no'
        else:
            isborrowed='yes'
        if book.user != None:
            item={
                    "title": str(book.title),
                    "description":str(book.description),
                    "img":str(book.img),
                    'author_name':str(book.author_name),
                    'about_author':str(book.about_author),
                    'id':str(book.id),
                    'isborrowed':str(isborrowed),
                    'username':str(book.user.username)
                }
            
        else:
              item={
                    "title": str(book.title),
                    "description":str(book.description),
                    "img":str(book.img),
                    'author_name':str(book.author_name),
                    'about_author':str(book.about_author),
                    'id':str(book.id),
                    'isborrowed':str(isborrowed),
                 }
        # if i<4: 
        #    i+=1 
        #    latest_data.append(item)
        # elif book.is_trending and j<8  :
        #     j+=1  
        #     trending_data.append(item)
        # else:
        #     other_data.append(item)
        if book.is_trending:
            trending_data.append(item)
        else: 
            latest_data.append(item)
    context={
        "trending":trending_data,
        "latest":latest_data,  
            }
   
    return JsonResponse(context)

def getSingleBook(request,pk):
    print("this is the primary key" ,pk)
    obj = Book.objects.get(pk=pk)
    user=""
    if obj.user != None:
        user= obj.user.username
    data={
        'id': str(obj.id),
        'title': str(obj.title),
        "description":str(obj.description),
        'img': str("/books/"+ pk +"/image"),
        'author_name':str(obj.author_name),
        'about_author':str(obj.about_author),
        'category':str(obj.category),
        'user':str(user),
    }
    return render(request,'books/single_book.html',{'data':data})


def getAbout(request):
    return render(request,'pages/about.html')


def getAllBooks(request):
    books= Book.objects.all()
    data=[]
    try:    
        for book in books:
            item={
                "title": str(book.title),
                "description":str(book.description),
                "img":str(book.img),
                'author_name':str(book.author_name),
                'about_author':str(book.about_author),
                'id':str(book.id),
            }
            data.append(item)
        context={"data":data,"filter":"all books"}
    except Exception as e:
        print(e)
        context={
           "data":"no books found" 
        }
    return render(request,'books/books_screen.html',context)




def addBook(request):
    return render(request,'books/add_new_book.html')



from django.utils.timezone import now
import os

def getBookForEdit(request,pk):
    print("this is the primary key" ,pk)
    obj = Book.objects.get(pk=pk)
    is_trending= str('False')
    if obj.is_trending:
        is_trending = "True"
    data={
        'id': str(obj.id),
        'title': str(obj.title),
        "description":str(obj.description),
        "category":str(obj.category),
        'img': str("/books/"+ pk +"/image"),
        'author_name':str(obj.author_name),
        'about_author':str(obj.about_author),
        'is_trending':str(is_trending),
    }
    print(data)
    return render(request,'books/edit_single_book.html',{'data':data})
def deleteBook(request):
    if request.method == 'POST':
       
        book_id =int(request.POST['book_id'])

        book = Book.objects.get(pk=book_id)

        if book.img != "default-book-cover.jpg":
            image_path = os.path.join(str(settings.MEDIA_ROOT), str(book.img))
            if os.path.exists(image_path):
                os.remove(image_path)
        try:
            Book.objects.filter(pk=book_id).delete()

            return JsonResponse({'status': 'success', 'message': 'Book deleted successfully'})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Book not found'})
        except (ValidationError, Exception) as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


def changeBookData(request):
    if request.method == 'POST':
        try:
            data_dict = request.POST.dict()
            book_name = data_dict.get('book_name')
            book_description = data_dict.get('book_description')
            author_name = data_dict.get('author_name')
            about_author = data_dict.get('about_author')
            category = data_dict.get('book_category')
            book_id = data_dict.get('book_id')
            image = request.FILES.get('image')
            trending_check = data_dict.get('trending_check')
            if trending_check == "False":
                trending_check = False
            else:
                trending_check = True


            if not book_name or not book_description or not author_name or not about_author or not category:
                raise ValidationError('Missing required fields.')
            obj = Book.objects.get(pk=book_id)
            obj.title = book_name
            obj.description = book_description
            obj.author_name = author_name
            obj.about_author = about_author
            obj.category = category
            obj.is_trending = trending_check
            if image != None:
                obj.img = image.read()
            else:
                # do nothing
                obj.img = obj.img
            if trending_check ==True:
                obj.mark_as_trending()

            obj.save()
            addTotrending()

            return JsonResponse({'status': 'Success', 'Message': 'Book added successfully'})
        except (ValidationError, Exception) as e:
            return JsonResponse({'status': 'Success', 'Message': "Book Was Add successfully"})

def addNewBook(request):
    if request.method == 'POST':
        try:
            data_dict = request.POST.dict()
            book_name = data_dict.get('book_name')
            book_description = data_dict.get('book_description')
            author_name = data_dict.get('author_name')
            about_author = data_dict.get('about_author')
            category = data_dict.get('category')
            image = request.FILES.get('image')
            trending_check = data_dict.get('trending_check')
            if trending_check == "False":
                trending_check = False
            else:
                trending_check = True

            print("data_dict: ", data_dict)
            print("book_name: ", book_name)
            print("book_description: ", book_description)
            print("author_name: ", author_name)
            print("about_author: ", about_author)
            print("category: ", category)
            print("is_trending: ", type(trending_check))
            print("image: ", image)
            
            if not book_name or not book_description or not author_name or not about_author or not category:
                raise ValidationError('Missing required fields.')

            new_book = Book.objects.create(
                title=book_name,
                description=book_description,
                author_name=author_name,
                about_author=about_author,
                category=category,
            )
            

            if image:
                new_book.img = image.read()
                new_book.save()
            else:
                # Set default image AS BINARY read from the media folder
                with open(os.path.join(settings.MEDIA_ROOT, 'default-book-cover.jpg'), 'rb') as default_image:
                    new_book.img = default_image.read()
                    new_book.save()
                
            if trending_check ==True:
                new_book.mark_as_trending()
            
            new_book.save()
            addTotrending()
            
                
            return JsonResponse({'status': 'success', 'message': 'Book added successfully'})
        except (ValidationError, Exception) as e:
            return JsonResponse({'status': 'error', 'message': str(e)})


def getBookImage(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        if book.img:
            return HttpResponse(book.img, content_type='image/jpeg')
        else:
            return HttpResponse(status=404)
    except Book.DoesNotExist:
        return HttpResponse(status=404)



def getSingleBookUserId(request,pk):
    
    context={}

    try:
        book =Book.objects.get(pk=pk)
        item={
            "username":book.user.username,
            "book_id":pk,
        }
        context={
            "data":item
        }
    except Exception as e:
        context={"data":{
            "username":"#",
            "book_id": pk,
        }}
    print(context)
    return JsonResponse(context)


def goToNotAuthorized(request):
    return render(request,'pages/not_authorized.html')



######################################################################
#######################################################################
####################################################################

def addTotrending():
    books = Book.objects.filter(is_trending=True).order_by('trending_date')
    for i in books:
        print(f'{i.title} -----> {i.is_trending} -----> {i.trending_date}')
    i= 4
    books =books.reverse()
    for i in range(len(books)):
        if i >=4 :
            print(books[i].title)
            books[i].is_trending =False
            books[i].trending_date =None
            books[i].save()

        i+=1
