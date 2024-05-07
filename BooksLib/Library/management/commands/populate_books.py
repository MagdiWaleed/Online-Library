from django.core.management.base import BaseCommand
from Library.models import SingleBookModel


class Command(BaseCommand):
    help = 'Populate books in the database'

    def handle(self, *args, **options):
        book_data = [
 {
        "id": 1,
        "book_name": "The Alchemist",
        "book_description": "A philosophical novel about a shepherd's journey",
        "author_name": "Paulo Coelho",
        "about_author": "Brazilian novelist and lyricist",
        "category": "Fiction",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/the_alchemist.jfif"
    },
    {
        "id": 2,
        "book_name": "To Kill a Mockingbird",
        "book_description": "A classic novel addressing racial injustice",
        "author_name": "Harper Lee",
        "about_author": "American author and Pulitzer Prize winner",
        "category": "Fiction",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/to-kill-a-mockingbird-one-sheet.jpg"
    },
    {
        "id": 3,
        "book_name": "1984",
        "book_description": "A dystopian novel exploring totalitarianism and surveillance",
        "author_name": "George Orwell",
        "about_author": "English novelist and essayist",
        "category": "Fiction",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/1984.jpg"
    },
    {
        "id": 4,
        "book_name": "Pride and Prejudice",
        "book_description": "A romantic novel focusing on love and societal norms",
        "author_name": "Jane Austen",
        "about_author": "English novelist known for wit and social commentary",
        "category": "Fiction",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/9780593622452.jpeg"
    },
    {
        "id": 5,
        "book_name": "The Great Gatsby",
        "book_description": "A tragic novel set during the Roaring Twenties",
        "author_name": "F. Scott Fitzgerald",
        "about_author": "American writer associated with the Jazz Age",
        "category": "Fiction",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/The_Great_Gatsby_Cover_1925_Retouched.jpg"
    },
    {
        "id": 6,
        "book_name": "Brave New World",
        "book_description": "A dystopian novel depicting a futuristic society",
        "author_name": "Aldous Huxley",
        "about_author": "English writer and philosopher",
        "category": "Fiction",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/flat,750x,075,f-pad,750x1000,f8f8f8.u5.jpg"
    },
    {
        "id": 7,
        "book_name": "The Catcher in the Rye",
        "book_description": "A coming-of-age novel following Holden Caulfield",
        "author_name": "J.D. Salinger",
        "about_author": "American author known for reclusive lifestyle",
        "category": "Fiction",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/Reproduction-cover-edition-The-Catcher-in-the.jpg"
    },
    {
        "id": 8,
        "book_name": "The Hobbit",
        "book_description": "A classic fantasy novel by J.R.R. Tolkien",
        "author_name": "J.R.R. Tolkien",
        "about_author": "British author and philologist",
        "category": "Fiction",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/the-hobbit-book-cover-art-2003.jpg"
    },
    {
        "id": 9,
        "book_name": "The Shadow of the Wind",
        "book_description": "A mysterious novel set in post-war Barcelona, uncovering secrets and hidden libraries",
        "author_name": "Carlos Ruiz Zafón",
        "about_author": "Spanish novelist known for his captivating storytelling",
        "category": "Mystery",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/51MQxESTvUL.jpg"
    },
    {
        "id": 10,
        "book_name": "The Name of the Wind",
        "book_description": "An epic fantasy following the life of Kvothe, a talented musician and magician.",
        "author_name": "Patrick Rothfuss",
        "about_author": "American writer and former college lecturer.",
        "category": "Fantasy",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/TheNameoftheWind_cover.jpg"
    },
    {
        "id": 11,
        "book_name": "The Martian",
        "book_description": "A gripping sci-fi novel about an astronaut stranded on Mars, fighting for survival.",
        "author_name": "Andy Weir",
        "about_author": "Software engineer turned author.",
        "category": "Science Fiction",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/05before-and-after-slide-T6H2-superJumbo.jpg"
    },
    {
        "id": 12,
        "book_name": "Gone Girl",
        "book_description": "A psychological thriller exploring a missing wife and the secrets behind her disappearance.",
        "author_name": "Gillian Flynn",
        "about_author": "American author and screenwriter.",
        "category": "Thriller",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/71+khXHbe5L._AC_UF894,1000_QL80_.jpg"
    },
    {
        "id": 13,
        "book_name": "The Handmaid’s Tale",
        "book_description": "A dystopian novel depicting a totalitarian society where women are oppressed.",
        "author_name": "Margaret Atwood",
        "about_author": "Canadian poet and novelist.",
        "category": "Dystopia",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/9780385539241.jpeg"
    },
    {
        "id": 14,
        "book_name": "The Book Thief",
        "book_description": "A moving historical novel set during World War II, narrated by Death.",
        "author_name": "Markus Zusak",
        "about_author": "Australian writer known for his unique narrative style.",
        "category": "Historical Fiction",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/914cHl9v7oL._AC_UF1000,1000_QL80_.jpg"
    },
    {
        "id": 15,
        "book_name": "The Catch-22",
        "book_description": "A satirical war novel highlighting the absurdity of bureaucracy and military rules.",
        "author_name": "Joseph Heller",
        "about_author": "American author and playwright.",
        "category": "Satire",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/4f339fc1d3b37ecb39b521b0a70c3be3.png"
    }, 
    {
        "id": 16,
        "book_name": "Mein Kampf",
        "book_description": "Mein Kamph is the autobiography of Adolf Hitler, this autobiography gives detailed insight into the mission and vision of Hitler that shocked the world. The beauty of the book Mein Kamph is that it is an empirical document which bears the imprint of its own time. The author has tried his best making German vocabulary easy to understand. After Hitler's death, copyright of Mein Kampf passed to the state government of Bavaria, which refused to allow any copying or printing of the book in Germany. You will never be satisfied until go through the whole book. This book is one of the most widely read book worldwide.", 
        "author_name": "Adolf Hitler",
        "about_author": "Adolf Hitler was an Austrian-born German politician who was the dictator of Nazi Germany from 1933 until his suicide in 1945. He rose to power as the leader of the Nazi Party, becoming the chancellor in 1933 and then taking the title of Führer und Reichskanzler in 1934",
        "category": "Autobiography",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/mein.jpg"
    },
    {
        "id": 17,
        "book_name": "All Quiet on The Western Front",
        "book_description": "This graphic novel recreates the classic story in vivid detail through meticulous research. The accurate depictions of uniforms, weapons, trenches, and death brings the horrors of the Western Front to life in a bold new way..",
        "author_name": "Wayne Vansant",
        "about_author": "For more than 30 years Wayne Vansant has been writing and illustrating comics and graphic novels on historic and military subjects, beginning with Marvel's Savage Tales and The 'Nam. Since then, he has produced Days of Darkness, Battron: The Trojan Woman, Blockade, The War in Korea, Stephan Crane's The Red Badge of Courage, Normandy, Grant vs. Lee, Bombing Nazi Germany, The Battle of the Bulge, The Red Baron, and others.",
        "category": "War novel",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/9781682473337.jpg"
    },
    {
        "id": 18,
        "book_name": "Can't Hurt Me",
        "book_description": " For David Goggins, childhood was a nightmare -- poverty, prejudice, and physical abuse colored his days and haunted his nights. But through self-discipline, mental toughness, and hard work, Goggins transformed himself from a depressed, overweight young man with no future into a U.S. Armed Forces icon and one of the world's top endurance athletes. ",
        "author_name": "David Goggins",
        "about_author": "David Goggins is a Retired Navy SEAL and the only member of the U.S. Armed Forces to complete SEAL training, Army Ranger School, and Air Force Tactical Air Controller training. Goggins has completed more than seventy ultra-distance races, often placing in the top five, he is often know as 'toughest man alive'.",
        "category": "Autobiography",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/81gTRv2HXrL._AC_UF1000,1000_QL80_.jpg"
    },
    {
        "id": 19,
        "book_name": "The Communist Manifesto",
        "book_description": "The complete The Communist Manifesto by Karl Marx and Friedrich Engels, in the 1888 English version edited by Engels himself. One of the most influential political treatises of all time, The Communist Manifesto is essential reading for every student of politics and history.",
        "author_name": "Karl Marx & Friedrich Engels",
        "about_author": "Karl Marx was born in Trier, Germany and studied law at Bonn and Berlin. In 1848, with Freidrich Engels, he finalized The Communist Manifesto. He settled in London, where he studied economics and wrote the first volume of his major work, & Friedrich Engels was born in Westphalia in 1820, the son of a textile manufacturer. After military training in Berlin, Engels already a convert to communism,  went to Manchester in 1842 to represent the family firm.",
        "category": "philosophy",
        "brrowed_date": None,
        "user_name": None,
        "user_id": None,
        "image": "images/the-communist-manifesto-104.jpg"
    },
        ]

        # Loop through the book data and create instances of SingleBookModel
        for book_info in book_data:
            SingleBookModel.objects.create(**book_info)

        self.stdout.write(self.style.SUCCESS('Books populated successfully'))
