function logoutUser() {
    localStorage.clear()
    window.location.href = '/noteappFrontend/index.html';
    console.log('clicked')
}


document.querySelector('#logout-button').addEventListener('click',logoutUser)