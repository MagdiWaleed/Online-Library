from django.db import models

# Create your models here.

""" SingleBookModel{

       constructor(id="#",book_name="#",book_description="#",author_id="#",author_name="#",about_author="#",category="#",brrowed_date="#",user_name="#",useer_id="#",image="#"){
       this.id=id;
       this.book_name=book_name;
       this.book_description=book_description;
       this.author_id=author_id
       this.author_name=author_name;
       this.about_author=about_author;
       this.category=category;   
       this.brrowed_date=brrowed_date;
       this.user_name=user_name;
       this.useer_id=useer_id;
       this.image =image;
       }
     }
     """


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class SingleBookModel(models.Model):
    # Use a unique identifier for author (consider UUID for better distribution)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    book_name = models.CharField(max_length=100)
    book_description = models.TextField()
    about_author = models.TextField()
    category = models.CharField(max_length=100)
    brrowed_date = models.DateField()
    user_name = models.CharField(max_length=100)
    user_id = models.IntegerField()
    #image = models.ImageField(upload_to='Media/books/', blank=True, null=True)  # Upload to 'books/' subdirectory in static/media

    def __str__(self):
        return f"{self.book_name} by {self.author.name} ({self.category})"
