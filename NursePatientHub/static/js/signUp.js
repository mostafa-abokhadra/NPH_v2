// document.forms[0].onclick = function (event) {
//     // event.preventDefault();
//     mydata = {}
//     let fname = document.querySelector("[name='firstName']")
//     let lname = document.querySelector("[name='lastName']")
//     let email = document.querySelector("[name='email']")
//     let pass = document.querySelector(".pass")
//     let mydata = {
//         "firstName": fname.value,
//         "lastName": lname.value,
//         "email": email.value,
//         "password": pass.value
//     }
// }
let fname = document.querySelector("[name='firstName']")
for (let i = 0; i < fname.value.length; i++) {
    if (fname.value[i] >= 'a' && fname.value[i] <= 'z') {
        continue;
    } else {
        let inp = document.querySelector('.firstName');
        console.log(inp);
    }
}
let lname = document.querySelector("[name='lastName']")
let email = document.querySelector("[name='email']")
let pass = document.querySelector(".pass")



