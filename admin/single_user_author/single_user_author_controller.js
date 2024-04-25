class SingleBookModel{

       constructor(id="#",book_name="#",book_description="#",author_id="#",author_name="#",about_author="#",category="#",brrowed_date="#",user_name="#",useer_id="#",image="#"){
       // this.short_id=GLOBAL_ID;
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
     
      book1= new SingleBookModel("#1", "The Alchemist", "A philosophical novel about a shepherd's journey",
             "#101", "Paulo Coelho", "Brazilian novelist and lyricist",
             "Fiction", "2024-04-18", "Alice", "1001","/references/images/books/the alchemist.jfif");
     
     
      book2= new SingleBookModel("#2", "To Kill a Mockingbird", "A classic novel addressing racial injustice",
             "#102", "Harper Lee", "American author and Pulitzer Prize winner",
             "Fiction", "2024-04-19", "Bob", "1002", "/references/images/books/to-kill-a-mockingbird-one-sheet.jpg");

      book3= new SingleBookModel("#3", "1984", "A dystopian novel exploring totalitarianism and surveillance",
            "#103", "George Orwell", "English novelist and essayist",
           "Fiction", "2024-04-20", "Carol", "1003" , "/references/images/books/1984.jpg");

      book4= new SingleBookModel("#4", "Pride and Prejudice", "A romantic novel focusing on love and societal norms",
            "#104", "Jane Austen", "English novelist known for wit and social commentary",
           "Fiction", "2024-04-21", "David", "1004", "/references/images/books/9780593622452.jpeg");

      book5= new SingleBookModel("#5", "The Great Gatsby", "A tragic novel set during the Roaring Twenties",
             "#105", "F. Scott Fitzgerald", "American writer associated with the Jazz Age",
             "Fiction", "2024-01-01", "Eva", "1005", "/references/images/books/The_Great_Gatsby_Cover_1925_Retouched.jpg");

      book6= new SingleBookModel("#6", "Brave New World", "A dystopian novel depicting a futuristic society",
             "#106", "Aldous Huxley", "English writer and philosopher",
             "Fiction", "null", "null", "1006", "/references/images/books/flat,750x,075,f-pad,750x1000,f8f8f8.u5.jpg");

      book7= new SingleBookModel("#7", "The Catcher in the Rye", "A coming-of-age novel following Holden Caulfield",
             "#107", "J.D. Salinger", "American author known for reclusive lifestyle",
             "Fiction", "null", "null", "1007", "/references/images/books/Reproduction-cover-edition-The-Catcher-in-the.jpg");

      book8= new SingleBookModel("#8", "The Hobbit", " classic fantasy novel by J.R.R. Tolkien",
             "#108", "J.R.R. Tolkien", "American author known for reclusive lifestyle",
             "Fiction", "null", "null", "1008", "/references/images/books/the-hobbit-book-cover-art-2003.jpg");

      book9= new SingleBookModel("#9", "The Shadow of the Wind", " A mysterious novel set in post-war Barcelona, uncovering secrets and hidden libraries",
             "#109", "Carlos Ruiz Zafón", "Spanish novelist known for his captivating storytelling",
             " Mystery", "null", "null", "1009", "/references/images/books/51MQxESTvUL.jpg");

      book10= new SingleBookModel("#10", "he Name of the Wind", " an epic fantasy following the life of Kvothe, a talented musician and magician.",
             "#110", "Patrick Rothfuss", " American writer and former college lecturer.",
             " Fantasy", "null", "null", "1010", "/references/images/books/TheNameoftheWind_cover.jpg");

      book11= new SingleBookModel("#11", "The Martian", "A gripping sci-fi novel about an astronaut stranded on Mars, fighting for survival.",
            "#111", "Andy Weir", "  Software engineer turned autho.",
            " Science Fiction", "null", "Grace", "1011", "/references/images/books/05before-and-after-slide-T6H2-superJumbo.jpg");

      book12= new SingleBookModel("#12", "Gone Girl", "A psychological thriller exploring a missing wife and the secrets behind her disappearance.",
             "#112", "Gillian Flynn", "  American author and screenwriter.",
             "  Thriller", "null", "null", "1012", "/references/images/books/71+khXHbe5L._AC_UF894,1000_QL80_.jpg");

      book13= new SingleBookModel("#13", "The Handmaid’s Tale", "A dystopian novel depicting a totalitarian society where women are oppressed.",
             "#113", "Margaret Atwood", "  Canadian poet and novelist.",
             "   Dystopia", "null", "null", "1013", "/references/images/books/9780385539241.jpeg");

      book14= new SingleBookModel("#14", "The Book Thief", " A moving historical novel set during World War II, narrated by Death.",
           "#114", "Markus Zusak", "  Australian writer known for his unique narrative style.",
           "   Historical Fiction", "null", "null", "1014", "/references/images/books/914cHl9v7oL._AC_UF1000,1000_QL80_.jpg");

      book15= new SingleBookModel("#15", "The Catch-22", " A satirical war novel highlighting the absurdity of bureaucracy and military rules.",
                 "#115", "Joseph Heller", "  American author and playwright.",
                 "   Satire", "null", "null", "1015", "/references/images/books/4f339fc1d3b37ecb39b521b0a70c3be3.png");

       book16= new SingleBookModel("#16", "Mein Kampf", "Mein Kamph is the autobiography of Adolf Hitler, this autobiography gives detailed insight into the mission and vision of Hitler that shocked the world. The beauty of the book Mein Kamph is that it is an empirical document which bears the imprint of its own time. The author has tried his best making German vocabulary easy to understand. After Hitler's death, copyright of Mein Kampf passed to the state government of Bavaria, which refused to allow any copying or printing of the book in Germany. You will never be satisfied until go through the whole book. This book is one of the most widely read book worldwide.",
                 "#116", "Adolf Hitler", "Adolf Hitler was an Austrian-born German politician who was the dictator of Nazi Germany from 1933 until his suicide in 1945. He rose to power as the leader of the Nazi Party, becoming the chancellor in 1933 and then taking the title of Führer und Reichskanzler in 1934",
                 "Autobiography", "null", "null", "1016" , "/references/images/books/mein.jpg");

       book17= new SingleBookModel("#17", "All Quiet on The Western Front", "This graphic novel recreates the classic story in vivid detail through meticulous research. The accurate depictions of uniforms, weapons, trenches, and death brings the horrors of the Western Front to life in a bold new way..",
                 "#117", "Wayne Vansant", "For more than 30 years Wayne Vansant has been writing and illustrating comics and graphic novels on historic and military subjects, beginning with Marvel's Savage Tales and The 'Nam. Since then, he has produced Days of Darkness, Battron: The Trojan Woman, Blockade, The War in Korea, Stephan Crane's The Red Badge of Courage, Normandy, Grant vs. Lee, Bombing Nazi Germany, The Battle of the Bulge, The Red Baron, and others.",
                 " War novel", "null", "null", "1017", "/references/images/books/9781682473337.jpg");

        book18= new SingleBookModel("#18", "Can't Hurt Me", " For David Goggins, childhood was a nightmare -- poverty, prejudice, and physical abuse colored his days and haunted his nights. But through self-discipline, mental toughness, and hard work, Goggins transformed himself from a depressed, overweight young man with no future into a U.S. Armed Forces icon and one of the world's top endurance athletes. ",
                 "#118", "David Goggins", "David Goggins is a Retired Navy SEAL and the only member of the U.S. Armed Forces to complete SEAL training, Army Ranger School, and Air Force Tactical Air Controller training. Goggins has completed more than seventy ultra-distance races, often placing in the top five, he is often know as 'toughest man alive'.",
                 "Autobiography", "null", "null", "1018", "/references/images/books/81gTRv2HXrL._AC_UF1000,1000_QL80_.jpg");     
                 
      book19= new SingleBookModel("#19", "The Communist Manifesto", "The complete The Communist Manifesto by Karl Marx and Friedrich Engels, in the 1888 English version edited by Engels himself. One of the most influential political treatises of all time, The Communist Manifesto is essential reading for every student of politics and history.",
                 "#119", "Karl Marx & Friedrich Engels", "Karl Marx was born in Trier, Germany and studied law at Bonn and Berlin. In 1848, with Freidrich Engels, he finalized The Communist Manifesto. He settled in London, where he studied economics and wrote the first volume of his major work, & Friedrich Engels was born in Westphalia in 1820, the son of a textile manufacturer. After military training in Berlin, Engels already a convert to communism,  went to Manchester in 1842 to represent the family firm.",
                 "philosophy", "null", "null", "1019", "/references/images/books/the-communist-manifesto-104.jpg");    
     
       bookList=[
         book1
         ,
         book2
         ,
         book3
         ,
         book4
         ,
         book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15,book16,book17,book18,book19
       ]
     
     
     
     
     



  function goToSingleBook(singleBookDataindex){
       console.log(singleBookDataindex);
       singleBookData=JSON.stringify(bookList[singleBookDataindex]);
        
       sessionStorage.setItem("single_book",singleBookData);
       window.location.href="/admin/single_book/single_book.html";
       
}









   
//     <div class="book_details" onclick="navigateToPage('/admin/single_book/single_book.html')">
//     <img src="/references/images/book.jpg" alt="IMAGE-NOT-FOUND" class="book_image" >
//     <h4>The Art Of</h4>
//     <p>By: Author Name</p>
//   </div>
// var bookCard="  <div class='book_details' onclick=''><img src='/references/images/book.jpg' alt='IMAGE-NOT-FOUND' class='book_image' ><h4>The Art Of</h4><p>By: Author Name</p></div>";

function buildBookCard(singleBookData , index){
  image_layer="<div class='book_details ' onclick=\"goToSingleBook('"+index+"')\"><img src='"+singleBookData.image+"' alt='IMAGE-NOT-FOUND' class='book_image' >";
  book_details_layer="<h4>"+singleBookData.book_name+"</h4><p>By: "+singleBookData.author_name+"</p></div>"
  return image_layer+book_details_layer;
}


function getTheBooksList  (){
         bookCardsList="";
        
         for(var i in bookList){
          if(bookList[i].image=="#"){
                bookList[i].image='/references/images/default-book-cover.jpg';
          }
          
            bookCardsList+=" "+buildBookCard(bookList[i],i);
          
           
        }
        document.write(bookCardsList);
}

  
  function HOW_IAM_HERE(){
    try{
        comingFrom=sessionStorage.getItem("single_user_author");
        console.log(comingFrom);
    }
    
    catch(error){
        console.log(error);
    }
      if(comingFrom=="users_table"){
            document.getElementById("owner_text").innerHTML="User Name: "+document.getElementById("owner_text").innerHTML;
        }
        else if(comingFrom=="authors_table"){
            document.getElementById("owner_text").innerHTML="By: "+document.getElementById("owner_text").innerHTML;
        }
        else{
            document.getElementById("owner_text").innerHTML="[some erro occur]: "+document.getElementById("owner_text").innerHTML;
        }
//     console.log(document.getElementById("owner_text").innerHTML);
  }