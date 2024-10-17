// import getCurrentHost from "./common.js"

// console.log(document.querySelector("#email").value);
// console.log(document.querySelector("#email"));

document.querySelector("#username").addEventListener("selectionchange",(e) => {
    console.log(document.querySelector("#username").value)
})


document.querySelector("#login-form").addEventListener("submit",(e) => {
    e.preventDefault()
    const username = document.querySelector("#username").value
    const password = document.querySelector("#password").value

    console.log(username,password)
    // url = getCurrentHost()
    
    axios.post(`http://localhost:8000/api/token/`,{username:username,password:password})
    .then(function (response) {
        localStorage.setItem("loginApiResponse",JSON.stringify(response.data));
        if(JSON.parse(localStorage.getItem('loginApiResponse'))?.access){
          localStorage.setItem("access",JSON.parse(localStorage.getItem('loginApiResponse')).access);
          window.location.href = '/noteappFrontend/home.html';
        }
        console.log(localStorage.getItem('loginApiResponse'))
      })
      .catch(function (error) {
        localStorage.setItem("apiError",error);
      })
      
})