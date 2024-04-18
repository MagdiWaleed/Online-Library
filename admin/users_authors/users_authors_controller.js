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
  
  
  var rowDetails="  <tr class=\"odd\" onclick=\"navigateToPage('/admin/single_user_author/single_user_author.html')\"><td><div>Magdi waleed mohamed khalaf allah</div></td><td><div>50</div></td></tr>";

  function buildSingleRow(isEven,singleUserAuthorData){
    backgroundStyle="odd";
    if(isEven){
        backgroundStyle="even";
    }
   singleRow="<tr class="+backgroundStyle+" onclick=\"navigateToPage('/admin/single_user_author/single_user_author.html')\"><td><div>"+singleUserAuthorData.name+"</div></td><td><div>"+singleUserAuthorData.getNumberOfBooks()+"</div></td></tr>"
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
   


  
