from django.core.management.base import BaseCommand
from books.models import Book
import os


#get image and read it and retur it AS binary
def get_image(image_path):
    with open("media/books/24/05/22/" + image_path, 'rb') as img:
        return img.read()
class Command(BaseCommand):
    help = 'Populate books in the database'

    def handle(self, *args, **options):
        book_data = [

            {
        "title": "Everything is F*cked",
        "description": "From the author of the international mega-bestseller The Subtle Art of Not Giving A F*ck comes a counterintuitive guide to the problems of hope.",
        "author_name": "Mark Manson ",
        "about_author": "Mark Manson (born 1984) is a professional blogger, entrepreneur, and former dating coach. Since 2007, he's been helping people with their emotional and relationship problems. He has worked with thousands of people from over 30 different countries.",
        "category": "Psychology",
        "img": get_image('Everything is Fcked.jpg'),

    },

    ]

        # Loop through the book data and create instances of SingleBookModel
        for book_info in book_data:
            Book.objects.create(**book_info)

        self.stdout.write(self.style.SUCCESS('Books populated successfully'))
