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

try {
    let plus_logo = document.querySelector('.ask .plus-logo')
    plus_logo.addEventListener('click', popQuestion)
    let ques = document.querySelector('.q-form')
    async function popQuestion() {
        ques.setAttribute('style', 'display: block;')
    }
    let myBtn = document.querySelector('.q-submit')
    myBtn.addEventListener('click', sendQuestion)
    async function sendQuestion() {
        ques.setAttribute('style', 'display: none;')

    }
} catch (err) {
    console.log("can't popUp question input")
}

let elem = document.createElement('small')
elem.textContent = "login to access this service"
elem.setAttribute('style', 'color: red; align-self: center; padding-left: 5px;')
let parent = document.querySelectorAll('.styling-div')

try {
    let plus_not_populate = document.querySelector('.populate .plus-logo-not')
    let plus_not_ask = document.querySelector('.ask .plus-logo-not')
    plus_not_ask.addEventListener('click', popDownAsk)
    plus_not_populate.addEventListener('click', popDownPopulate)

    async function popDownPopulate() {
        parent[0].appendChild(elem)
    }
    async function popDownAsk() {
        parent[1].appendChild(elem)
    }

} catch (err) {
    console.log("some thing went wrong with error message of 'you need to login first'")
}

try {
    let notNurse = document.querySelector('.plus-logo-notNurse')
    let notPatient = document.querySelector('.plus-logo-not-patient')
    // console.log(notNurse)
    // console.log(notPatient)
    notNurse.addEventListener('click', invlide_user_nurse)
    notPatient.addEventListener('click', invlide_user_patient)

    async function invlide_user_nurse() {
        elem.textContent = "only Nurses have access to this page"
        parent[0].appendChild(elem)
    }
    async function invlide_user_patient() {
        elem.textContent = "only patinets have access to this page"
        parent[1].appendChild(elem)
    }
} catch (err) {
    console.log("error in error message of 'invalide user type to access this page!'")
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