function navigateToPage(url){
    window.location.href=url;
}
function showpopup(){
    if(localStorage.getItem("isloged") == "true"){
       
        const storedUserDataString = localStorage.getItem(name.value);
        const storedUserData = JSON.parse(storedUserDataString);
        console.log(storedUserData.check);
        if(storedUserData.check == false){
        
        navigateToPage('/user/my_information/my_information.html');}
    }
    else{
    let pop_up = document.getElementById("popup");
    pop_up.classList.add("open-popup");}
}
function closepopup(){
       
    name = document.getElementById('user');
    pass = document.getElementById('pass');
    check = document.getElementById('check');
    const storedUserDataString = localStorage.getItem("user");
    console.log(localStorage.getItem("user"));
    if(!(storedUserDataString == null)){
           const storedUserData = JSON.parse(storedUserDataString);
           if(storedUserData.pass == pass.value){
                  if(check.checked == false){
                 localStorage.setItem("isloged","true");
                 console.log('in');
                 let pop_up = document.getElementById("popup");
                  pop_up.classList.remove("open-popup");}
                  else{
                         window.location.href="/admin/main/main.html";
                  }
           }
           else{
                  window.alert('wrong password');
           }
          
    }
    else{
        window.alert('No user');   
    }
    

    }
function closepop(){
    console.log('wrong');
    let pop_up = document.getElementById("popup");
    pop_up.classList.remove("open-popup");
}
