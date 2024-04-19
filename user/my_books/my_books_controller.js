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
          "Fiction", "2024-04-19", "Bob", "1002");
   book3= new SingleBookModel("#3", "1984", "A dystopian novel exploring totalitarianism and surveillance",
         "#103", "George Orwell", "English novelist and essayist",
        "Fiction", "2024-04-20", "Carol", "1003");
   book4= new SingleBookModel("#4", "Pride and Prejudice", "A romantic novel focusing on love and societal norms",
         "#104", "Jane Austen", "English novelist known for wit and social commentary",
        "Fiction", "2024-04-21", "David", "1004");
   book5= new SingleBookModel("#5", "The Great Gatsby", "A tragic novel set during the Roaring Twenties",
          "#105", "F. Scott Fitzgerald", "American writer associated with the Jazz Age",
          "Fiction", "2024-01-01", "Eva", "1005");
   book6= new SingleBookModel("#6", "Brave New World", "A dystopian novel depicting a futuristic society",
          "#106", "Aldous Huxley", "English writer and philosopher",
          "Fiction", "null", "null", "1006");
   book7= new SingleBookModel("#7", "The Catcher in the Rye", "A coming-of-age novel following Holden Caulfield",
          "#107", "J.D. Salinger", "American author known for reclusive lifestyle",
          "Fiction", "null", "null", "1007");
   book8= new SingleBookModel("#8", "The Hobbit", " classic fantasy novel by J.R.R. Tolkien",
          "#108", ": J.R.R. Tolkien", "American author known for reclusive lifestyle",
          "Fiction", "null", "null", "1008");
   book9= new SingleBookModel("#9", "The Shadow of the Wind", " A mysterious novel set in post-war Barcelona, uncovering secrets and hidden libraries",
          "#109", ": Carlos Ruiz Zafón", "Spanish novelist known for his captivating storytelling",
          " Mystery", "null", "null", "1009");
   book10= new SingleBookModel("#10", "he Name of the Wind", " an epic fantasy following the life of Kvothe, a talented musician and magician.",
          "#110", ": Patrick Rothfuss", " American writer and former college lecturer.",
          " Fantasy", "null", "null", "1010");
   book11= new SingleBookModel("#11", "The Martian", "A gripping sci-fi novel about an astronaut stranded on Mars, fighting for survival.",
         "#111", ": Andy Weir", "  Software engineer turned autho.",
         " Science Fiction", "null", "Grace", "1011");
   book12= new SingleBookModel("#12", "Gone Girl", "A psychological thriller exploring a missing wife and the secrets behind her disappearance.",
          "#112", ": Gillian Flynn", "  American author and screenwriter.",
          "  Thriller", "null", "null", "1012");
   book13= new SingleBookModel("#13", "The Handmaid’s Tale", "A dystopian novel depicting a totalitarian society where women are oppressed.",
          "#113", ": Margaret Atwood", "  Canadian poet and novelist.",
          "   Dystopia", "null", "null", "1013");
   book14= new SingleBookModel("#14", "The Book Thief", " A moving historical novel set during World War II, narrated by Death.",
        "#114", ": Markus Zusak", "  Australian writer known for his unique narrative style.",
        "   Historical Fiction", "null", "null", "1014");
   book15= new SingleBookModel("#15", "The Catch-22", " A satirical war novel highlighting the absurdity of bureaucracy and military rules.",
              "#115", ":Joseph Heller", "  American author and playwright.",
              "   Satire", "null", "null", "1015");
  
    bookList=[
      book1
      ,
      book2
      ,
      book3
      ,
      book4
      ,
      book5,book6,book7,book8,book9,book10,book11,book12,book13,book14,book15
    ]
  
   
  
  
    function goToSingleBook(singleBookDataindex){
         console.log(singleBookDataindex);
         singleBookData=JSON.stringify(bookList[singleBookDataindex]);
          
         sessionStorage.setItem("single_book",singleBookData);
         window.location.href="/user/SingleBook/SingleBook.html?query="+encodeURIComponent("my_brrowed_books");
         
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
  
  function getMyBooksList  (){
           bookCardsList="";
          
           for(var i in bookList){
            if(bookList[i].image=="#"){
                  bookList[i].image='/references/images/default-book-cover.jpg';
            }
             
              bookCardsList+=" "+buildBookCard(bookList[i],i);
             
             
          }
          document.write(bookCardsList);
  }
  
  function getNumberOfBooks(){
    document.getElementById("number_of_books").innerHTML=bookList.length;
  }