


function showErrorMessage(errorMsg) {
    const errorElement = document.querySelector('#error-message')
    let errorClass = errorElement.getAttribute('class')
    console.log(errorClass);
    const updatedErrClass = errorClass.replace("hidden","")
    errorElement.setAttribute('class',updatedErrClass)
    errorElement.children[1].innerHTML = `${errorMsg}`
    
    
}

// showErrorMessage("astyauioakspoaijskakls")

function registerUser(username,email,password){
    axios.post(`http://localhost:8000/register/`,{username:username,password:password,email:email})
    .then(function (response) {
        // localStorage.setItem("signupApiResponse",JSON.stringify(response.data));
        if(response.status_code == 200){          
            console.log('logged in sucessfully');
            window.location.href = '/noteappFrontend/index.html';
        }
      })
      .catch(function (error) {
        localStorage.setItem("apiError",error);
      })
}


document.querySelector('#signup-form').addEventListener('submit',(e)=>{
    e.preventDefault()
    const username = document.querySelector("#username").value
    const email = document.querySelector("#email").value
    const password = document.querySelector("#password").value
    const rePassword = document.querySelector("#re-password").value
    
    let errorMessage = ""

    if(password!==rePassword){
        errorMessage = "passwords do not match"
    }
    if (errorMessage!=""){
        showErrorMessage(errorMessage)
    }
    registerUser(username,email,password)
})


