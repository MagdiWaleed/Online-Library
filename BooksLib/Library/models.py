from django.db import models

# Create your models here.

class SingleBookModel(models.Model):
    # Use a unique identifier for author (consider UUID for better distribution)
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_description = models.TextField()
    author_name = models.CharField(max_length=100)
    about_author = models.TextField()
    category = models.CharField(max_length=100)
    brrowed_date = models.DateField(blank=True, null=True)
    user_name = models.CharField(max_length=100,blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, default='images/default-book-cover.jpg')  # Upload to 'images/' subfolder within media

    def __str__(self):
        return f"ID: {self.id} Title: {self.book_name} by {self.author_name} ({self.category})"
    def serialize(self):
        return {
            'id': self.id,
            'book_name': self.book_name,
            'book_description': self.book_description,
            'author_name': self.author_name,
            'about_author': self.about_author,
            'category': self.category,
            'brrowed_date': self.brrowed_date.strftime("%Y-%m-%d") if self.brrowed_date else None,
            'user_name': self.user_name,
            'user_id': self.user_id,
            'image': self.image.url if self.image else None
        }


