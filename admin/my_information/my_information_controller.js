function enterUserMode(){
    sessionStorage.setItem("user_mode","enable");
    window.location.href='/user/main/main.html';
}