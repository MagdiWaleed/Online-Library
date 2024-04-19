
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
        console.log('done1');
    const userData = {
        "name": name,
        "pass": pass,
        "confpass": confpass,
        "mail": mail,
        "check": check
    };
    const userDataString = JSON.stringify(userData);
    localStorage.setItem(name.value, userDataString);}
}