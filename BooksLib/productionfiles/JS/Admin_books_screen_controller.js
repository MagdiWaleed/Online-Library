
  /////////////////////////////////////////////////////////////////////////////////////

  

  async function getBookData() {
    const response = await fetch('/get-books/'); // Replace with your actual API endpoint
    const data = await response.json();
    return data;
  }
  
    var bookList;
    getBookData().then(data => {
           bookList = data;
           console.log(bookList);
    }
    );
  
    function addNewBook(){
      window.location.href="Admin_add_new_book.html";
   }
 
    
    
    
    
      function goToSingleBook(singleBookDataindex){
           console.log(singleBookDataindex);
           singleBookData=JSON.stringify(bookList[singleBookDataindex]);
            
           sessionStorage.setItem("single_book",singleBookData);
           window.location.href ="Admin_single_book.html";
           
    }
    
    
    
    
    
    
    

    
    function buildBookCard(singleBookData , index){
      image_layer="<div class='book_details ' onclick=\"goToSingleBook('"+index+"')\"><img src=\"" + singleBookData.image+ "\" alt='IMAGE-NOT-FOUND' class='book_image' >";
      book_details_layer="<h4>"+singleBookData.book_name+"</h4><p>By: "+singleBookData.author_name+"</p></div>"
      return image_layer+book_details_layer;
    }
    

    function buildBrrowedBookCard(singleBookData, index){
      first_layer="<div class='borrowed_books' onclick=\"goToSingleBook('"+index+"')\"><div style='position: relative;' >";
      image_layer="<img src=\"" + singleBookData.image+ "\"  alt='IMAGE-NOT-FOUND' class='book_image'/>";
      book_details_layer="<h4>"+singleBookData.book_name+"</h4>"+"<p>By:"+singleBookData.author_name+"</p></div ><h2 class='BORROWED'>BORROWED</h2></div>";
     return first_layer+image_layer+book_details_layer;
     }
    
    async  function getTheBooksList  (){
      const bookData = await getBookData();
      let bookCardsList = "";
            
      for (const book of bookData) {
        var i=bookData.indexOf(book);
        if (book.image === "") {
          book.image='default-book-cover.jpg';
        }
        if(book.user_id != null){
          bookCardsList+=" "+buildBrrowedBookCard(book,i);
        }
        else{
          bookCardsList+=" "+buildBookCard(book,i);
        }
  }
            document.getElementById('bookshelves').innerHTML +=  bookCardsList; // Update the container with the generated HTML
          }
  
  
  getTheBooksList();

