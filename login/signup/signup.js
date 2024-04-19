
function signpress(){
    sign = document.getElementById('sign');
    name = document.getElementById('user');
    pass = document.getElementById('pass');
    conf = document.getElementById('confpass');
    mail = document.getElementById('mail');
    check = document.getElementById('check');
    if((!mail.value.includes('@')) || (pass.value != conf.value)){
        window.alert('wrong entrey');
    }
    else{
    const userData = {
        "name": name.value,
        "pass": pass.value,
        "confpass": confpass.value,
        "mail": mail.value,
        "check": check.value
    };
    const userDataString = JSON.stringify(userData);
    localStorage.setItem(name.value, userDataString);}
}