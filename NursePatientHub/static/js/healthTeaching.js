try {
    let arrow = document.querySelector(".arrow")
    arrow.addEventListener('click', arrowClick)
    async function arrowClick() {
        location.href = "#questionsToAnswer"
    }
} catch (err) {
    console.log('some error')
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