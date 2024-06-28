// let popup = document.querySelector('.populate-popup')
// try {
//     let populate_plus_logo = document.querySelector('.populate .plus-logo')
//     populate_plus_logo.addEventListener('click', popItUp)
//     async function popItUp() {
//         popup.setAttribute('style', 'display: block;')
//     }
//     let close = document.querySelector('.lable-x i')
//     close.addEventListener('click', closeIt)
//     async function closeIt() {
//         popup.setAttribute('style', 'display: none;')
//     }

// } catch (err) {
//     console.log(err)
// }

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
/**/
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
/**/
try {
    let notNurse = document.querySelector('.plus-logo-notNurse')
    notNurse.addEventListener('click', invlide_user_nurse)
    async function invlide_user_nurse() {
        elem.textContent = "only Nurses have access to this page"
        parent[0].appendChild(elem)
    }
} catch (err) {
    console.log(err)
}
/**/
try {
    let notPatient = document.querySelector('.plus-logo-not-patient')
    notPatient.addEventListener('click', invlide_user_patient)
    async function invlide_user_patient() {
        elem.textContent = "only patinets have access to this page"
        parent[1].appendChild(elem)
    }
} catch (err) {
    console.log(err)
}
/**/
let answer_link = document.querySelector('.answer-link')
try {
    let goTo = document.querySelector('.go-to-popup')
    goTo.addEventListener('click', goToPopUp)
    async function goToPopUp() {
        let myQ = document.querySelector('.a-question h4')
        let myInput = document.querySelector('.title-input')
        myInput.value = myQ.textContent
        let myAttr = document.createAttribute('autofocus')
        let myArea = document.querySelector('.text-area-input')
        myArea.setAttributeNode(myAttr)
        popup.setAttribute('style', 'display: block;')
    }
} catch (err) {
    console.log(err)
}
/**/
try {
    let no_popup = document.querySelector('.no-popup')
    no_popup.addEventListener('click', noPopUp)
    async function noPopUp() {
        elem.textContent = 'only Nurses can answer patients questions'
        answer_link.insertBefore(elem, answer_link.firstChild)
    }
} catch (err) {
    console.log(err)
}