mydata = {}
document.forms[0].onclick = function (event) {
    event.preventDefault();
    let fname = document.querySelector("[name='firstName']")
    let lname = document.querySelector("[name='lastName']")
    let email = document.querySelector("[name='email']")
    let pass = document.querySelector(".pass")
    let mydata = {
        "firstName": fname.value,
        "lastName": lname.value,
        "email": email.value,
        "password": pass.value
    }
}
