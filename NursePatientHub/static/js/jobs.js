let add_job = document.querySelector('.add-an-opportunity')
add_job.onclick = function () {
    let url = "http://127.0.0.1:5000/applications";
    location.href = url
}