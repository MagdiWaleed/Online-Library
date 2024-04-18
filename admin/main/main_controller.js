    //     <div class="book_details" onclick="navigateToPage('/admin/single_book/single_book.html')">
    //     <img src="/references/images/book.jpg" alt="IMAGE-NOT-FOUND" class="book_image" >
    //     <h4>The Art Of</h4>
    //     <p>By: Author Name</p>
    //   </div>
var bookCard="  <div class='book_details' onclick=''><img src='/references/images/book.jpg' alt='IMAGE-NOT-FOUND' class='book_image' ><h4>The Art Of</h4><p>By: Author Name</p></div>";
/////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////
/* <div class="borrowed_books">
<div style="position: relative;">
  <img src="/references/images/book.jpg" alt="IMAGE-NOT-FOUND" class="book_image">
 <h4>Book Title</h4>
 <p>By: Author Name</p>
</div >
  <h2 class="BORROWED">BORROWED</h2>
</div>
<div class="book_details" onclick="navigateToPage('/admin/single_book/single_book.html')">
 <img src="/references/images/book.jpg" alt="IMAGE-NOT-FOUND" class="book_image" >
 <h4>The Art Of</h4>
 <p>By: Author Name</p>
</div> */
var brrowedBook="<div class='borrowed_books'><div style='position: relative;'><img src='/references/images/book.jpg' alt='IMAGE-NOT-FOUND' class='book_image'><h4>Book Title</h4> <p>By: Author Name</p></div ><h2 class='BORROWED'>BORROWED</h2></div><div class='book_details'><img src='/references/images/book.jpg' alt='IMAGE-NOT-FOUND' class='book_image' ><h4>The Art Of</h4><p>By: Author Name</p></div> "


function getTrendingBooksList  (numberOfElements){

          bookCardsList="";
        for(i=0;i<numberOfElements;i++){
            if(i%5==0){
                bookCardsList+=" "+brrowedBook;
            }
            else{
            bookCardsList+=" "+bookCard;
            }
        }
        document.write(bookCardsList);
}

function getLatestBooksList  (numberOfElements){

    bookCardsList="";
  for(i=0;i<numberOfElements;i++){
      if(i%5==0){
          bookCardsList+=" "+brrowedBook;
      }
      else{
      bookCardsList+=" "+bookCard;
      }
  }
  document.write(bookCardsList);
}