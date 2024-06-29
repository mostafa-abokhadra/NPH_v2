function for_media_1200(media_1200) {
    if (media_1200.matches) {
        let site_name = document.querySelector("header .container .logo-links .logo-div .site-name span");
        site_name.textContent = "NPH";

        let logo_div = document.querySelector(".logo-links .logo-div");
        logo_div.style.width = '25%';

        let link_div = document.querySelector('.logo-links ');
        link_div.style.width = '50%';

        let main_h2 = document.querySelector('.landingNurseParagraph');
        main_h2.style.width = "50%";

        let main_photo = document.querySelector('.container .home-photo');
        main_photo.style.width = "50%";
    }
}
// function for_media_992(media_992) {
//     if (media_992.matches) {
//     }
// }

let media_1200 = window.matchMedia('(max-width: 1200px)');
for_media_1200(media_1200);
media_1200.addEventListener(for_media_1200, for_media_1200);


let logo_div = document.querySelector(".logo-div");
logo_div.onclick = function () {
    let url = "https://nph-785eb2775630.herokuapp.com/";
    location.href = url;
}
