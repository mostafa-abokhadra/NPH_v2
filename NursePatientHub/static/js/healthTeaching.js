try {
    let popup = document.querySelector('.populate-popup')
    let populate_plus_logo = document.querySelector('.populate .plus-logo')
    populate_plus_logo.addEventListener('click', popItUp)
    async function popItUp() {
        popup.setAttribute('style', 'display: block;')
    }
    let close = document.querySelector('.lable-x i')
    close.addEventListener('click', closeIt)
    async function closeIt() {
        popup.setAttribute('style', 'display: none;')
    }

} catch (err) {
    console.log("can't popUp window")
}


// let populate = document.querySelector('.populate .plus-logo')
// let ask = document.querySelector('.ask .plus-logo')
// ask.addEventListener('click', pop_question)

// async function pop_question() {
//     let populate = document.querySelector('.populate')
//     let ask_logo = document.querySelector('.ask .plus-logo')

//     let parent = document.querySelector('.ask')
//     let div = document.createElement('div')
//     let textarea = document.createElement('textarea')
//     let submit = document.createElement('input')

//     populate.setAttribute('style', 'display: none;')
//     ask_logo.setAttribute('style', 'display: none;')

//     div.setAttribute('style', 'display: flex; flex-wrap: wrap; z-index: 1; transition: 0.3s; width: 100%;')

//     textarea.setAttribute('name', 'patient-question')
//     textarea.setAttribute('placeholder', 'write your question')
//     textarea.setAttribute('maxlength', '100')
//     textarea.setAttribute('style', 'width: 100%;')

//     submit.setAttribute('type', 'submit')
//     submit.setAttribute('value', 'send')
//     submit.setAttribute('style', 'margin-top: 5px;')
//     div.appendChild(textarea)
//     div.appendChild(submit)
//     parent.appendChild(div)

// }