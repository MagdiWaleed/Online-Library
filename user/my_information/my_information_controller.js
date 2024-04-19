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