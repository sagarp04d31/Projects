function validateForm(){
                    var x = document.forms["MyForm"]["username"].value;
                    var y = document.forms["MyForm"]["useremail"].value;
                    if(x !== "" || y !== "" ){
                        alert("Thank you for your feedback");
                    }  
                } 