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
        "title": "Good Rich People",
        "description": "Lyla has always believed that life is a game she is destined to win, but her husband, Graham, takes the game to dangerous levels. The wealthy couple invites self-made success stories to live in their guesthouse and then conspires to ruin their lives. After all, there is nothing worse than a bootstrapper.",
        "author_name": "Eliza Jane Brazier",
        "about_author": "Other books: If I Disappear, Girls and their Horses, It Had to Be You.",
        "category": "Fiction",
        "img": get_image('Good Rich People.jpg')
    },
    {
        "title": "Read People Like a Book",
        "description": "How to Analyze, Understand, and Predict People’s Emotions, Thoughts, Intentions, and Behaviors.",
        "author_name": "Patrick King",
        "about_author": "Patrick King is a Social Interaction Specialist, in other words, a dating, online dating, image, and communication and social skills coach based in San Francisco, California, and has been featured on numerous national publications such as Inc.com. He’s also a #1 Amazon best-selling dating and relationships author with the most popular online dating book on the market.",
        "category": "Psychology",
        "img": get_image('Read People Like a Book.jpg')
    },
    {
        "title": "milk and honey",
        "description": "Milk and Honey is a collection of poetry and prose about survival. About the experience of violence, abuse, love, loss, and femininity.",
        "author_name": "Rupi Kaur",
        "about_author": "A breakout literary phenomenon and #1 New York Times Bestselling Author, Rupi Kaur wrote, illustrated, and self-published her first poetry collection, 'milk and honey' in 2014.",
        "category": "Poetry",
        "img": get_image('milk and honey.jpg')
    },
    {
        "title": "Hide and Don't Seek",
        "description": "A contemporary collection of original short stories by Anica Mrose Rissi that is sure to elicit chills, laughs, and screams, even from the most devoted fans of Scary Stories to Tell in the Dark! A game of hide-and-seek goes on far too long...",
        "author_name": "Anica Mrose Rissi",
        "about_author": "Writer, storyteller, editrix. Author of picture books, chapter books, middle grade, and YA. Fan of dogs and ice cream. Offers energetic, interactive presentations and writing workshops for students of all ages at libraries, festivals, and schools.",
        "category": "Horror",
        "img": get_image('Hide and Don\'t Seek.jpg')
    },
    {
        "title": "Surrounded by Idiots",
        "description": "A runaway bestseller in Sweden that has sold more than a million copies worldwide, Surrounded by Idiots shares a groundbreaking new method of understanding the people around you that will change how you interact with everyone from your coworkers to your spouse.",
        "author_name": "Thomas Erikson",
        "about_author": "Thomas Erikson is a behaviourist and the bestselling author of the Surrounded by- series about human behaviours. The series, has been translated to close to 60 languages and has sold over 8 million copies.",
        "category": "Psychology",
        "img": get_image('Surrounded by Idiots.png')
    },
    {
        "title": "Verity",
        "description": "Lowen Ashleigh is a struggling writer on the brink of financial ruin when she accepts the job offer of a lifetime. Jeremy Crawford, husband of bestselling author Verity Crawford, has hired Lowen to complete the remaining books in a successful series his injured wife is unable to finish.",
        "author_name": "Colleen Hoover",
        "about_author": "International and #1 New York Times bestselling author of romance, YA, thriller, women's fiction and paranormal romance.",
        "category": "Thriller",
        "img": get_image('Verity.jpg')
    },
    {
        "title": "Thinking, Fast and Slow",
        "description": "In the highly anticipated Thinking, Fast and Slow, Kahneman takes us on a groundbreaking tour of the mind and explains the two systems that drive the way we think. System 1 is fast, intuitive, and emotional; System 2 is slower, more deliberative, and more logical. Kahneman exposes the extraordinary capabilities—and also the faults and biases—of fast thinking, and reveals the pervasive influence of intuitive impressions on our thoughts and behavior.",
        "author_name": "Daniel Kahneman",
        "about_author": "Daniel Kahneman (Hebrew: דניאל כהנמן; born 5 March 1934 - died 27 March 2024), was an American psychologist and winner of the 2002 Nobel Memorial Prize in Economic Sciences, notable for his work on behavioral finance and hedonic psychology.",
        "category": "Psychology",
        "img": get_image('Thinking, Fast and Slow.jpg')
    },
    {
        "title": "Just the Two of Us",
        "description": "The lyrics of a Grammy winner's hit single are joined with stunning pencil and oil illustrations to celebrate the dignity, integrity, and honor of being a father. 125,000 first printing.",
        "author_name": "Will Smith",
        "about_author": "Will Smith is an actor, producer and musician, two-time Academy Award nominee, Grammy Award and NAACP award winner who has enjoyed a diverse career encompassing films, television and multi-platinum records.",
        "category": "Music",
        "img": get_image('Just the Two of Us.jpeg')
    },
    {
        "title": "How to Kill Your Family",
        "description": "I have killed several people (some brutally, others calmly) and yet I currently languish in jail for a murder I did not commit.",
        "author_name": "Bella Mackie",
        "about_author": "Vogue columnist. Author of best-selling novel “How to Kill Your Family.\"",
        "category": "Fiction",
        "img": get_image('How to Kill Your Family.jpg')
    },
    {
        "title": "Fable",
        "description": "For seventeen-year-old Fable, the daughter of the most powerful trader in the Narrows, the sea is the only home she has ever known. It’s been four years since the night she watched her mother drown during an unforgiving storm. The next day her father abandoned her on a legendary island filled with thieves and little food. To survive she must keep to herself, learn to trust no one, and rely on the unique skills her mother taught her.",
        "author_name": "Adrienne Young",
        "about_author": "Adrienne Young is the New York Times and international bestselling author of the Sky and Sea duology, the Fable series, and Spells for Forgetting. When she’s not writing, you can find Adrienne on her yoga mat, on a walk in the woods, or planning her next travel adventure. She lives and writes in the Blue Ridge Mountains of North Carolina.",
        "category": "Fantasy",
        "img": get_image('Fable.jpg')
    },
    {
        "title": "Too Scared to Sleep",
        "description": "From debut author Andrew Duplessie, a terrifying collection of teen short horror stories--and accompanying videos--that will keep you up long into the night! Perfect for fans of Five Nights at Freddy's.",
        "author_name": "Andrew Duplessie",
        "about_author": "Andrew Duplessie is a prolific writer and tech entrepreneur whose scary stories are devoured online by millions of readers. He's also a producer and writer on a handful of major television shows, including American Horror Stories. He lives in New York, New York.",
        "category": "Horror",
        "img": get_image('Too Scared to Sleep.jpg')
    },
    {
        "title": "Will",
        "description": "Will Smith isn't holding back in his bravely inspiring new memoir . . . An ultimately heartwarming read, Will provides a humane glimpse of the man behind the actor, producer and musician, as he bares all his insecurities and trauma.” —USA Today Winner of the NAACP Image Award for Outstanding Literary Achievement One of the most dynamic and globally recognized entertainment forces of our time opens up fully about his life, in a brave and inspiring book that traces his learning curve to a place where outer success, inner happiness, and human connection are aligned. Along the way, Will tells the story in full of one of the most amazing rides through the worlds of music and film that anyone has ever had.",
        "author_name": "Will Smith",
        "about_author": "Will Smith is an actor, producer and musician, two-time Academy Award nominee, Grammy Award and NAACP award winner who has enjoyed a diverse career encompassing films, television and multi-platinum records.",
        "category": "Memoir",
        "img": get_image('Will.jpg')
    },
    {
    "title": "The Subtle Art of Not Giving a F*ck",
    "description": "In this generation-defining self-help guide, a superstar blogger cuts through the crap to show us how to stop trying to be 'positive' all the time so that we can truly become better, happier people.",
    "author_name": "Mark Manson",
    "about_author": "Mark Manson (born 1984) is a professional blogger, entrepreneur, and former dating coach. Since 2007, he's been helping people with their emotional and relationship problems. He has worked with thousands of people from over 30 different countries.",
    "category": "Self-Help",
    "img": get_image('The Subtle Art of Not Giving a Fck.png')
},
{
    "title": "The Power of Habit",
    "description": "A young woman walks into a laboratory. Over the past two years, she has transformed almost every aspect of her life. She has quit smoking, run a marathon, and been promoted at work. The patterns inside her brain, neurologists discover, have fundamentally changed.",
    "author_name": "Charles Duhigg",
    "about_author": "CHARLES DUHIGG is a Pulitzer prize-winning reporter and the author of The Power of Habit, which spent over three years on New York Times bestseller lists. His second book, Smarter Faster Better, was a bestseller.",
    "category": "Self-Help",
    "img": get_image('The Power of Habit.jpg')
},
{
    "title": "Reminders of Him",
    "description": "After serving five years in prison for a tragic mistake, Kenna Rowan returns to the town where it all went wrong, hoping to reunite with her four-year-old daughter. But the bridges Kenna burned are proving impossible to rebuild.",
    "author_name": "Colleen Hoover",
    "about_author": "International and #1 New York Times bestselling author of romance, YA, thriller, women's fiction and paranormal romance.",
    "category": "Romance",
    "img": get_image('Reminders of Him.jpg')
},
{
    "title": "Act Like a Success, Think Like a Success",
    "description": "When Steve Harvey was thirtysomething, he was living in his car. It was a sacrifice he was willing to make to give it his best shot at becoming a comedian. After several months of this lifestyle-washing in public bathrooms, eating fast food-he had considered giving up. Before calling his mother to ask if he could stay with her, he checked his voicemail. The Apollo Theatre wanted him to perform! Great opportunity, but Steve did not have enough money for gas to get from Tennessee to New York. He prayed about it, as he was too proud to ask for money. The following day he had a message from a club in Florida. The audience loved him so much they asked Steve back for a second night. The gig provided him enough money to fly to New York. Although he had no place to stay, walking around all night with a bag that held everything that he owned, it did not get him down.",
    "author_name": "Steve Harvey",
    "about_author": "Broderick Steven 'Steve' Harvey is an American comedian, actor, entertainer, and radio personality. He is probably best known as the star of the WB sitcom The Steve Harvey Show, and as one of the four comedians featured in the Spike Lee film The Original Kings of Comedy. Currently, he is the host of The Steve Harvey Morning Show, a nationally syndicated radio program.",
    "category": "Self-Help",
    "img": get_image('Act Like a Success, Think Like a Success.jpg')
},
{
    "title": "Jog On",
    "description": "How I Got My Life Back on Track. Divorced and struggling with deep-rooted mental health problems, Bella Mackie ended her twenties in tears. She could barely find the strength to get off the sofa, let alone piece her life back together. Until one day she did something she had never done of her own free will – she pulled on a pair of trainers and went for a run.",
    "author_name": "Bella Mackie",
    "about_author": "Vogue columnist. Author of best-selling novel 'How to Kill Your Family.'",
    "category": "Memoir",
    "img": get_image('Jog On.jpg')
},
{
    "title": "A Good Girl's Guide to Murder",
    "description": "Everyone in Fairview knows the story. Pretty and popular high school senior Andie Bell was murdered by her boyfriend, Sal Singh, who then killed himself. It was all anyone could talk about. And five years later, Pip sees how the tragedy still haunts her town.",
    "author_name": "Holly Jackson",
    "about_author": "Holly Jackson was born in 1992. She grew up in Buckinghamshire and started writing stories from a young age, completing her first (poor) attempt at a book aged fifteen.",
    "category": "Thriller",
    "img": get_image('A Good Girl\'s Guide to Murder.jpg')
},
{
    "title": "The Shadow of the Wind",
    "description": "Barcelona, 1945: A city slowly heals from its war wounds, and Daniel, an antiquarian book dealer's son who mourns the loss of his mother, finds solace in a mysterious book entitled The Shadow of the Wind, by one Julian Carax. But when he sets out to find the author's other works, he makes a shocking discovery: someone has been systematically destroying every copy of every book Carax has written. In fact, Daniel may have the last of Carax's books in existence. Soon Daniel's seemingly innocent quest opens a door into one of Barcelona's darkest secrets--an epic story of murder, madness, and doomed love.",
    "author_name": "Carlos Ruiz Zafón",
    "about_author": "Carlos Ruiz Zafón was a Spanish novelist known for his 2001 novel La sombra del viento (The Shadow of the Wind). The novel sold 15 million copies and was winner of numerous awards; it was included in the list of the one hundred best books in Spanish in the last twenty-five years, made in 2007 by eighty-one Latin American and Spanish writers and critics.",
    "category": "Historical Fiction",
    "img": get_image('The Shadow of the Wind.jpg')
},
{
    "title": "Sky in the Deep",
    "description": "Raised to be a warrior, seventeen-year-old Eelyn fights alongside her Aska clansmen in an ancient rivalry against the Riki clan. Her life is brutal but simple: fight and survive. Until the day she sees the impossible on the battlefield—her brother, fighting with the enemy—the brother she watched die five years ago.",
    "author_name": "Adrienne Young",
    "about_author": "Adrienne Young is the New York Times and international bestselling author of the Sky and Sea duology, the Fable series, and Spells for Forgetting. When she’s not writing, you can find Adrienne on her yoga mat, on a walk in the woods, or planning her next travel adventure. She lives and writes in the Blue Ridge Mountains of North Carolina.",
    "category": "Fantasy",
    "img": get_image('Sky in the Deep.jpg')
},
{
    "title": "It Ends with Us",
    "description": "Sometimes it is the one who loves you who hurts you the most.",
    "author_name": "Colleen Hoover",
    "about_author": "International and #1 New York Times bestselling author of romance, YA, thriller, women's fiction and paranormal romance.",
    "category": "Romance",
    "img": get_image('It end with us.jpg')
},
{
    "title": "Everything is F*cked",
    "description": "From the author of the international mega-bestseller The Subtle Art of Not Giving A F*ck comes a counterintuitive guide to the problems of hope.",
    "author_name": "Mark Manson",
    "about_author": "Mark Manson (born 1984) is a professional blogger, entrepreneur, and former dating coach. Since 2007, he's been helping people with their emotional and relationship problems. He has worked with thousands of people from over 30 different countries.",
    "category": "Psychology",
    "img": get_image('Everything is Fcked.jpg')
}


    ]

        # Loop through the book data and create instances of SingleBookModel
        for book_info in book_data:
            Book.objects.create(**book_info)

        self.stdout.write(self.style.SUCCESS('Books populated successfully'))
