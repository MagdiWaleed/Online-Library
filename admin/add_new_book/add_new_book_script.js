

function fetchData(){
    
  try{
   parameters=new URLSearchParams(window.location.search);
   query= parameters.get('query');
  }
  catch(error){
    console.log(error);
  }
  try{
    stringSingleBookData=sessionStorage.getItem("single_book");
    singleBookData=JSON.parse(stringSingleBookData);
  }catch(error){
    console.log(error);
    singleBookData= new SingleBookModel();
  }
 
  
  if (query=="singleBook"){
    document.getElementById('book_name').innerHTML=singleBookData.book_name;
    document.getElementById('author_name').innerHTML=singleBookData.author_name;
    document.getElementById('description').innerHTML=singleBookData.book_description;
    document.getElementById('about_author').innerHTML=singleBookData.about_author;
    document.getElementById('book_category').innerHTML=singleBookData.category;
    if(singleBookData.image=="#"){
        
        document.getElementById("book_image").src='/references/images/default-book-cover.jpg';
        }
        else{
            document.getElementById("book_image").src=singleBookData.image;
        }
    
    document.getElementById('input_book_name').value=singleBookData.book_name;
    document.getElementById('input_author_name').value=singleBookData.author_name;
    document.getElementById('input_description').value=singleBookData.book_description;
    document.getElementById('input_about_author').value=singleBookData.about_author;
    document.getElementById('input_book_category').value=singleBookData.category;
    document.getElementById('delete_button').style.display="inline-block";
    document.getElementById('done_button').innerText="Save Changes";
    
    
    }
    else{
        document.getElementById('book_name').innerHTML="";
        document.getElementById('author_name').innerHTML="";
        document.getElementById('description').innerHTML="";
        document.getElementById('about_author').innerHTML="";
        document.getElementById('book_category').innerHTML="";
        //////////////////////////
        document.getElementById('input_book_name').value="";
        document.getElementById('input_author_name').value="";
        document.getElementById('input_description').value="";
        document.getElementById('input_about_author').value="";
        document.getElementById('input_book_category').value="";
    }
}