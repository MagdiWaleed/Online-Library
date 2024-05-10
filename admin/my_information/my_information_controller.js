function enterUserMode(){
    sessionStorage.setItem("user_mode","enable");
    console.log(sessionStorage.getItem('isloged'));
    window.location.href='/user/main/main.html';
}
function add_text(){
    nameZep = document.getElementById("username");
    mailhold = document.getElementById('email');
    passhold = document.getElementById('password');
    confpasshold = document.getElementById('confirm_password');
    const storedUserDataString = sessionStorage.getItem("user");
    const storedUserData = JSON.parse(storedUserDataString);
    console.log(storedUserData["name"]);
    nameZep.placeholder = storedUserData.name;
    mailhold.placeholder = storedUserData["mail"];
    passhold.placeholder = storedUserData["pass"];
    confpasshold.placeholder = storedUserData["confpass"];
}
function save_cahnge(){
    namehold = document.getElementById("username");
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