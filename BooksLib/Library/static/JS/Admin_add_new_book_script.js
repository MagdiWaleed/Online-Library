// Admin_add_new_book_script.js

document.getElementById('add_new_book_form').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent default form submission
  
  // Collect form data
  var formData = new FormData();
  formData.append('book_name', document.getElementById('input_book_name').value);
  formData.append('book_description', document.getElementById('input_description').value);
  formData.append('author_name', document.getElementById('input_author_name').value);
  formData.append('about_author', document.getElementById('input_about_author').value);
  formData.append('category', document.getElementById('input_book_category').value);
  formData.append('image', document.getElementById('image_input').files[0]);

  // Send AJAX request
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/add_new_book/');
  
  // Set CSRF token in the request header
  xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken')); // function to get CSRF token
  
  xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
              // Success, do something
              console.log(xhr.responseText);
          } else {
              // Error handling
              console.error(xhr.responseText);
          }
      }
  };
  xhr.send(formData);
});

// Function to get CSRF token from cookies
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

/*
document.getElementById('add_new_book_form').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent default form submission
  
  // Collect form data
  var formData = new FormData();
  formData.append('book_name', document.getElementById('input_book_name').value);
  formData.append('book_description', document.getElementById('input_description').value);
  formData.append('author_name', document.getElementById('input_author_name').value);
  formData.append('about_author', document.getElementById('input_about_author').value);
  formData.append('category', document.getElementById('input_book_category').value);
  formData.append('image', document.getElementById('image_input').files[0]);

  // Send AJAX request
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/your_django_view_url/');
  xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken')); // function to get CSRF token
  xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
              // Success, do something
              console.log(xhr.responseText);
          } else {
              // Error handling
              console.error(xhr.responseText);
          }
      }
  };
  xhr.send(formData);
});

// Function to get CSRF token from cookies
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
*/

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
        
        document.getElementById("book_image").src="/static/Media/default-book-cover.jpg";
        }
        else{
            document.getElementById("book_image").src="/static/" + singleBookData.image ;
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