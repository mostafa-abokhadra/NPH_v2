/*if user is not authenticated then this code run if he tries to access populate healtTeaching
or ask a question properities, he must singUp first*/
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
/*end*/

/*if current user is nurse or employer and tries to ask question as patients this code run*/
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
/*end*/

/* whan a nurse click on answer link to a patient questoin, small window will popUp */
let answer_link = document.querySelector('.answer-link')
let popup = document.querySelector('.populate-popup')
try {
    let goTo = document.querySelectorAll('.go-to-popup')
    let questions = document.querySelectorAll('.a-question')
    let title = document.querySelector('.title-input')
    for (let i = 0; i < goTo.length; i++) {
        goTo[i].onclick = async function () {
            let myQ = questions[i].firstElementChild.textContent
            title.value = myQ
            let attr = document.createAttribute('disabled')
            title.setAttributeNode(attr)
            popup.setAttribute('style', 'display: block;')
        }
    }


    // let goTo = document.querySelectorAll('.go-to-popup')
    // goTo.addEventListener('click', goToPopUp)
    // async function goToPopUp() {
    //     let myQ = document.querySelector('.a-question h4')
    //     let myInput = document.querySelector('.title-input')
    //     myInput.value = myQ.textContent
    //     let myAttr = document.createAttribute('autofocus')
    //     let myArea = document.querySelector('.text-area-input')
    //     myArea.setAttributeNode(myAttr)
    //     popup.setAttribute('style', 'display: block;')
    // }
} catch (err) {
    console.log(err)
}
/*end*/

/* closing popUp health teaching window of nurses */
try {
    let close = document.querySelector('.lable-x i')
    close.addEventListener('click', closeIt)
    async function closeIt() {
        popup.setAttribute('style', 'display: none;')
    }
} catch (err) {
    console.log(err)
}
/* end */

/* if a patient or employer tries to populate healthTeaching this code runs*/
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
/* end */

/* if a patient or employer tries to answer patient question this code runs */
try {
    let no_popup = document.querySelectorAll('.no-popup')
    let place = document.querySelector('#answer_me')
    let parent = document.querySelector('#questionsToAnswer')

    let new_elem = document.createElement('div')
    new_elem.setAttribute('class', 'only-nurses')

    for (let i = 0; i < no_popup.length; i++) {
        no_popup[i].onclick = async function () {
            new_elem.textContent = 'only Nurses can answer patients questions'
            parent.insertBefore(new_elem, place)
        }
    }
} catch (err) {
    console.log(err)
}
/* end */

/* when patient click on ask question small input window shows */
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
    console.log(err)
}
/* end */