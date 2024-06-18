let p_sec = document.querySelector(".a-patient");
p_sec.onclick = function () {
    let type = { 'userType': "p" }
    fetch("http://127.0.0.1:5000/userType", {
        mehtod: "POST",
        headers: {
            "Conternt-type": "application/json"
        },
        type
    });
}
// let n_sec = document.querySelector(".a-nurse type-sec");

// let e_sec = document.querySelector(".an-employer type-sec");

// let s_sec = document.querySelector(".a-student type-sec");