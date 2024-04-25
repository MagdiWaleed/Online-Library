
function signpress(){
    sign = document.getElementById('sign');
    namehold = document.getElementById('user');
    pass = document.getElementById('pass');
    conf = document.getElementById('confpass');
    mail = document.getElementById('mail');
    check = document.getElementById('check');
    if((!mail.value.includes('@')) || (pass.value != conf.value)){
        window.alert('wrong entrey');
    }
    else{
        
    const userData = {
        "name": namehold.value,
        "pass": pass.value,
        "confpass": confpass.value,
        "mail": mail.value,
        "check": check.checked
    };
    const userDataString = JSON.stringify(userData);
    sessionStorage.setItem("user", userDataString);
    sessionStorage.setItem("isloged","true");
    if(check.checked == false){
    document.getElementById('link').href = "/user/main/main.html";}
    else{
        document.getElementById('link').href = "/admin/main/main.html";
    }
}
    
}