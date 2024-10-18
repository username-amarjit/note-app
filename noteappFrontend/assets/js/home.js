
const card = (id,title,miniDesc) => {
    return `<div class="bg-white overflow-hidden shadow rounded-lg" id="card${id}">
                <a href="/noteappFrontend/detail.html?note=${id}">
                    <div class="px-4 py-5 sm:p-6" >
                        <h3 class="text-lg leading-6 font-medium text-gray-900">${title}</h3>
                        <p class="mt-1 text-sm text-gray-500">${miniDesc}...</p>
                    </div>
                </a>
            </div>`
}  

function setAllNotes(notes){
    const noteContainer =  document.querySelector('#notes-container');
    console.log(notes.length > 0,"tyuio");
    console.log(notes,"tyuio");
    
    if (notes.length > 0){
        noteContainer.innerHTML =  notes.map((note) => {
            return card(note.id,note.title,note.description)             
        }).join("   ")
    }
    else{
        noteContainer.innerHTML = card("","No Notes found.","")
    }

}

let notesData = [];
 function getAllNotes(){
    axios.get(`http://localhost:8000/notetakingapp/getallnotes/`,{},{headers: {
        Authorization: `Bearer ${localStorage.getItem('access')}`
      }})
    .then(function (response) {
        notesData = response.data.data        
        localStorage.setItem('allNotes',JSON.stringify(notesData))
        setAllNotes(notesData)
      })
    .catch(function (error) {
        console.log(error);
      })
    console.log(notesData,'gbnm');
    
}

getAllNotes()

function createNote(){
    console.log('creating note')
    window.location.href = "/noteappFrontend/detail.html"
}


function logoutUser() {
    localStorage.clear()
    window.location.href = '/noteappFrontend/index.html';
    console.log('clicked')
}


document.querySelector('#logout-button').addEventListener('click',logoutUser)
document.querySelector('#create-button').addEventListener('click',createNote)

