function validateForm() {
    let x = document.getElementById('fname').value;
  //   let b = document.forms
  
  //   console.log(b['myForm'])
  
    if (x != "Shamim") {
      alert(`You are not the right user, you are ${x} `);
      return false
    }
    else{
     alert(x)
  
    }
  }