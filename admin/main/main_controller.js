class SingleBookModel{

  constructor(id="#",book_name="#",book_description="#",author_id="#",author_name="#",about_author="#",category="#",image="#"){
  // this.short_id=GLOBAL_ID;
  this.id=id;
  this.book_name=book_name;
  this.book_description=book_description;
  this.author_name=author_name;
  this.author_id=author_id
  this.about_author=about_author;
  this.category=category;    
  this.image =image;
  }
}


   
//     <div class="book_details" onclick="navigateToPage('/admin/single_book/single_book.html')">
//     <img src="/references/images/book.jpg" alt="IMAGE-NOT-FOUND" class="book_image" >
//     <h4>The Art Of</h4>
//     <p>By: Author Name</p>
//   </div>
// var bookCard="  <div class='book_details' onclick=''><img src='/references/images/book.jpg' alt='IMAGE-NOT-FOUND' class='book_image' ><h4>The Art Of</h4><p>By: Author Name</p></div>";

function buildBookCard(singleBookData){
  if ((singleBookData.book_name).length > 20) {
  image_layer="<div class='book_details' onclick=\"navigateToPage('/admin/single_book/single_book.html')\"><img src='"+singleBookData.image+"' alt='IMAGE-NOT-FOUND' class='book_image' >";
  book_details_layer="<h4 class='overflow'>"+singleBookData.book_name+"</h4><p>By: "+singleBookData.author_name+"</p></div>"
  if ((singleBookData.author_name).length > 17) {
    console.log("ana khol");
    image_layer="<div class='book_details' onclick=\"navigateToPage('/admin/single_book/single_book.html')\"><img src='"+singleBookData.image+"' alt='IMAGE-NOT-FOUND' class='book_image' >";
    book_details_layer="<h4 class='overflow'>"+singleBookData.book_name+"</h4><p class='overflow'>By: "+singleBookData.author_name+"</p></div>"
  }
}
     
  else if ((singleBookData.author_name).length > 17) {
    console.log("i'm here author");
    image_layer="<div class='book_details' onclick=\"navigateToPage('/admin/single_book/single_book.html')\"><img src='"+singleBookData.image+"' alt='IMAGE-NOT-FOUND' class='book_image' >";
    book_details_layer="<h4>"+singleBookData.book_name+"</h4><p class='overflow'>By: "+singleBookData.author_name+"</p></div>"
  }
  else {
    image_layer="<div class='book_details' onclick=\"navigateToPage('/admin/single_book/single_book.html')\"><img src='"+singleBookData.image+"' alt='IMAGE-NOT-FOUND' class='book_image' >";
    book_details_layer="<h4>"+singleBookData.book_name+"</h4><p>By: "+singleBookData.author_name+"</p></div>"
  }
  return image_layer+book_details_layer;
}

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
*/
// var brrowedBook=" <div class='borrowed_books'><div style='position: relative;'> <img src='/references/images/book.jpg'alt='IMAGE-NOT-FOUND' class='book_image'/><h4>The Art Of</h4><p>By: Author Name</p></div ><h2 class='BORROWED'>BORROWED</h2></div>"


function buildBrrowedBookCard(singleBookData){
 first_layer="<div class='borrowed_books' onclick=\"navigateToPage('/admin/single_book/single_book.html')\"><div style='position: relative;' >";
 image_layer="<img src='"+singleBookData.image+"'alt='IMAGE-NOT-FOUND' class='book_image'/>";
 book_details_layer="<h4>"+singleBookData.book_name+"</h4>"+"<p>By:"+singleBookData.author_name+"</p></div ><h2 class='BORROWED'>BORROWED</h2></div>";
return first_layer+image_layer+book_details_layer;
}

function getTrendingBooksList  (numberOfElements){
         bookCardsList="";
         console.log(buildBookCard(new SingleBookModel()));
        for(i=0;i<numberOfElements;i++){
          s =new SingleBookModel();
          s.id=0;
          s.book_name= "how to type to type ez like a bitch";
          s.book_description="how t";
          s.author_id=11;
          s.author_name="magdi waleed khalf allah";
          s.category="action";
          s.about_author="he is good autoher"
          s.image="/references/images/book.jpg";
          
            if(i%5==0){
                bookCardsList+=" "+buildBrrowedBookCard(s);
            }
            else{
            bookCardsList+=" "+buildBookCard(s);
            }
            delete s;
        }
        document.write(bookCardsList);
}

function getLatestBooksList  (numberOfElements){
  bookCardsList="";
  for(i=0;i<numberOfElements;i++){
    s =new SingleBookModel();
    s.id=0;
    s.book_name= "how ";
    s.book_description="its a nice book";
    s.author_id=11;
    s.author_name="Ahmed mohammed";
    s.category="action";
    s.about_author="he is good autoher"
    s.image="/references/images/book.jpg";
    
      if(i%5==0){
          bookCardsList+=" "+buildBrrowedBookCard(s);
      }
      else{
      bookCardsList+=" "+buildBookCard(s);
      }
      delete s;
  }
  document.write(bookCardsList);
}