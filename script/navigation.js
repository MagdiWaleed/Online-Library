function navigateToPage(url){
    window.location.href=url;
}
function showpopup(){
    if(localStorage.getItem("isloged") == "true"){
        console.log("im here ");
        const storedUserDataString = localStorage.getItem("user");
        const storedUserData = JSON.parse(storedUserDataString);
        console.log(storedUserData.check);
        if( sessionStorage.getItem("user_mode")=="enable"){
            navigateToPage("/user/my_information/my_information.html");
            const userData = {
                "name": 'admin',
                "pass": 'AN ADMIN',
                "confpass": 'AN ADMIN',
                "mail": "admin@admin.com",
                "check": "admin"
            };
            const userDataString = JSON.stringify(userData);
            localStorage.setItem("user", userDataString);
        }
        else if(storedUserData.check == false){
        
        navigateToPage('/user/my_information/my_information.html');
    }
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
