let editPage = true

const urlParams = new URLSearchParams(window.location.search);
const currNote = urlParams.get('note');

console.log(urlParams);
console.log(currNote);

if(currNote){
    editPage = true
    fetchNoteDetails(currNote)
}
function reRenderPage(){
if (editPage){
    const editButton = document.querySelector('#edit-button')
    const saveButton = document.querySelector('#save-button')
    const rawMarkdown = document.querySelector('#raw-markdown')
    const markdownPreview = document.querySelector('#markdown-preview')
    editButton.setAttribute('class' ,editButton.getAttribute('class').replace("hidden",""))
    saveButton.setAttribute('class' ,"hidden "+saveButton.getAttribute('class'))
    rawMarkdown.setAttribute('class' ,"hidden "+rawMarkdown.getAttribute('class'))
    markdownPreview.setAttribute('class' ,markdownPreview.getAttribute('class').replace("hidden","").replace('w-1/2','w-full'))

}else{
    const editButton = document.querySelector('#edit-button')
    const saveButton = document.querySelector('#save-button')
    const rawMarkdown = document.querySelector('#raw-markdown')
    const markdownPreview = document.querySelector('#markdown-preview')
    saveButton.setAttribute('class' ,saveButton.getAttribute('class').replace("hidden",""))
    editButton.setAttribute('class' ,"hidden "+editButton.getAttribute('class'))
    rawMarkdown.setAttribute('class' ,rawMarkdown.getAttribute('class').replace("hidden","").replace('w-full','w-1/2'))
    markdownPreview.setAttribute('class' ,markdownPreview.getAttribute('class').replace("hidden","").replace('w-full','w-1/2'))

}}

// document.querySelector("#markdown-input").addEventListener("selectionchange",(e) => {
//     saveNote()
// })createnote

function fetchNoteDetails(noteid){
    if (noteid){
        const allNotesData = JSON.parse(localStorage.getItem('allNotes'))
        const currNoteData = allNotesData.filter((note) => note.id == currNote)
        const mdText = document.querySelector('#markdown-input')
        console.log(currNoteData[0].html_text);
        
        mdText.innerHTML = currNoteData[0].html_text
    }   
}

function saveNote() {
    const mdText = document.querySelector('#markdown-input').value
    console.log(mdText);
    if(!currNote){
        const sampleTitle = "sample title "+(Math.floor(Math.random()*100+1))
        axios.post(`http://localhost:8000/notetakingapp/createnote/`,{"title":sampleTitle,"desc":sampleTitle,"markdown_text":mdText},{headers: {
            Authorization: `Bearer ${localStorage.getItem('access')}`
      }})
      .then( (response)=> {
          console.log(response)
        })
        .catch((err) => {
            console.log(err)
        })
    }
    else{
        axios.post(`http://localhost:8000/notetakingapp/updatenote/${currNote}`,{"markdown_text":mdText},{headers: {
            Authorization: `Bearer ${localStorage.getItem('access')}`
      }})
      .then( (response)=> {
          console.log(response)
        })
        .catch((err) => {
            console.log(err)
        })
    }
    editPage = true
}

function logoutUser() {
    localStorage.clear()
    window.location.href = '/noteappFrontend/index.html';
    console.log('clicked')
}
reRenderPage()

document.querySelector('#logout-button').addEventListener('click',logoutUser)
document.querySelector('#save-button').addEventListener('click',saveNote)
document.querySelector('#edit-button').addEventListener('click',()=>{editPage=false;reRenderPage()})
