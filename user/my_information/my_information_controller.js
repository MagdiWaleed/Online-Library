
function AM_I_IN_USER_MODE(){
    
    try{
        data =sessionStorage.getItem("user_mode");
    }catch(error){
        console.log(error);
        data="";
    }
    if(data!="enable"){
        document.getElementById("end_user_mode_button").style.display='none';
    }
    console.log(data);
}
function endUseerMode(){
    sessionStorage.removeItem("user_mode");
    window.location.href='/admin/main/main.html';
}
function add_text(){
    nameZep = document.getElementById("name");
    mailhold = document.getElementById('email');
    passhold = document.getElementById('password');
    confpasshold = document.getElementById('confpassword');
    const storedUserDataString = sessionStorage.getItem("user");
    const storedUserData = JSON.parse(storedUserDataString);
    console.log(storedUserData["name"]);
    nameZep.placeholder = storedUserData["name"];
    mailhold.placeholder = storedUserData["mail"];
    passhold.placeholder = storedUserData["pass"];
    confpasshold.placeholder = storedUserData["confpass"];
}
function save_cahnge(){
    namehold = document.getElementById("name");
    mail = document.getElementById('email');
    pass = document.getElementById('password');
    confpass = document.getElementById('confpassword');
    ////
    if((!mail.value.includes('@')) || (pass.value != confpass.value)){
        window.alert('wrong entrey');
    }
    else{
        console.log(namehold.value);
    const userData = {
        "name": namehold.value,
        "pass": pass.value,
        "confpass": confpass.value,
        "mail": mail.value,
    };
    const userDataString = JSON.stringify(userData);
    sessionStorage.setItem("user", userDataString);}
    console.log(sessionStorage.getItem("user"));
}
function delete_acc(){
sessionStorage.removeItem("user");
sessionStorage.setItem("isloged","false");
window.location.href = "/user/main/main.html";
}
add_text();
AM_I_IN_USER_MODE();
