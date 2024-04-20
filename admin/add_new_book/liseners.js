var inputField = document.getElementById('input_book_name');
var outputElement = document.getElementById('book_name');

var inputField2 = document.getElementById('input_author_name');
var outputElement2 = document.getElementById('author_name');

var inputField3 = document.getElementById('input_description');
var outputElement3 = document.getElementById('description');

var inputField4 = document.getElementById('input_about_author');
var outputElement4 = document.getElementById('about_author');

var inputField5 = document.getElementById('input_book_category');
var outputElement5 = document.getElementById('book_category');



inputField.addEventListener('input', function() {
    outputElement.innerText = inputField.value;
});

inputField2.addEventListener('input',function(){
    outputElement2.innerText=inputField2.value;
});

inputField3.addEventListener('input',function(){
    outputElement3.innerText=inputField3.value;
});

inputField4.addEventListener('input',function(){
    outputElement4.innerText=inputField4.value;
});

inputField5.addEventListener('input',function(){
    outputElement5.innerText=inputField5.value;
});
