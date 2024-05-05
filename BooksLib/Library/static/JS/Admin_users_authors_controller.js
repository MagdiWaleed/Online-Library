class SingleUserAuthorModel{
    constructor(name="#",id="#",books=[]){
        this.name=name;
        this.id=id;
        this.books=books;
    }
    getNumberOfBooks(){    
         return this.books.length; 
    }
}
  
  
  var rowDetails="  <tr class=\"odd\" onclick=\"WHERE_IM_GOING()\"><td><div>Magdi waleed mohamed khalaf allah</div></td><td><div>50</div></td></tr>";

  function buildSingleRow(isEven,singleUserAuthorData){
    backgroundStyle="odd";
    if(isEven){
        backgroundStyle="even";
    }
   singleRow="<tr class="+backgroundStyle+" onclick=\"WHERE_IM_GOING()\"><td><div>"+singleUserAuthorData.name+"</div></td><td><div>"+singleUserAuthorData.getNumberOfBooks()+"</div></td></tr>"
    return singleRow;    
}

    function getTableRows(numberOfelements){  
            tableRows="";
        for(i=0;i<numberOfelements;i++){
           m= new SingleUserAuthorModel();
            m.book_id="0";
            m.name= "Magdi waleed mohame khalaf allah";
            m.books=['book 1', "book 2", "book 3"]
            tableRows+=" "+buildSingleRow(i%2==0,m);
        }
        document.write(tableRows);
        delete s; 
    }


    
    function HOW_IAM_HERE(){
        try{
            comingFrom=sessionStorage.getItem("users_authors_screen");
        }catch(error){
            console.log(error);
            comingFrom="";
        }
        // console.log(comingFrom);
        // console.log(document.getElementById("owner_text").value)
        if(comingFrom=="show_users_button"){
            document.getElementById("owner_text").innerHTML="Users Brrowed books";
        }
        else if(comingFrom=="show_authors_button"){
            document.getElementById("owner_text").innerHTML="Authors books";
        }
        else{
            document.getElementById("owner_text").innerHTML='[some error occur]';   
        }

    }

    function WHERE_IM_GOING(){
        goingToSinlgeMemberScreenFrom='';
        try{
        comingFrom= sessionStorage.getItem("users_authors_screen") ;      
        }catch(error){
            console.log(error);
        }
        if(comingFrom=="show_users_button"){
            goingToSinlgeMemberScreenFrom="users_table";
        }
        else if(comingFrom=="show_authors_button"){
            goingToSinlgeMemberScreenFrom="authors_table";
        }
        else{
            goingToSinlgeMemberScreenFrom="[some error occur]";
        }
        sessionStorage.setItem("single_user_author",goingToSinlgeMemberScreenFrom);
        window.location.href ="Admin_single_user_author.html"
    }
   


  
