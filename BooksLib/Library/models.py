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

class SingleBookModel(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_description = models.TextField()
    author_id = models.IntegerField()
    author_name = models.CharField(max_length=100)
    about_author = models.TextField()
    category = models.CharField(max_length=100)
    brrowed_date = models.DateField()
    user_name = models.CharField(max_length=100)
    useer_id = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{ self.id} { self.book_name} {self.author_name} {self.category} {self.brrowed_date} "
    

