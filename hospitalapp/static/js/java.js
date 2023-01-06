



function show(){
var error_box=null;




var first_name = document.getElementById("form1Example1").value;
var last_name = document.getElementById("form2Example2").value;
var email = document.getElementById("form3Example3").value;
var password = document.getElementById("form4Example4").value;
var re_password = document.getElementById("form5Example5").value;
var at_position = email.indexOf("@");
var dot_position = email.lastIndexOf(".");
if( first_name == null || first_name == ""){
error_box="First-Name box not be blank";
}
else if( last_name == null || last_name==""){
error_box="Last_Name box not be blank";
}

else if(at_position<1 || dot_position < at_position + 2 || dot_position + 2 >= email.length){

error_box="You have entered a valid email address!";
}



else if ( password.length < 4 ){
error_box="password must be 4 letters ";
}
else if ( password != re_password ){
error_box="password must be same to the re_password";

}
else{
error_box=null;
}
if( error_box != null){
document.getElementById("error_msg").innerHTML=error_box;
document.getElementById("error_msg").setAttribute("style","color:red");
}
}

