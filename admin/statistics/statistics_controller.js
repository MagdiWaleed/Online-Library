function numberOfUsersDetails(){
    sessionStorage.setItem("users_authors_screen","show_users_button");
    window.location.href="/admin/users_authors/users_authors.html";
}

function numberOfAuthorsDetails(){
    sessionStorage.setItem("users_authors_screen","show_authors_button");
    window.location.href="/admin/users_authors/users_authors.html";
}