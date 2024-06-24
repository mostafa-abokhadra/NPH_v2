let logo_div = document.querySelector(".logo-div");
logo_div.onclick = function () {
    let url = "http://127.0.0.1:5000/";
    location.href = url;
}

let countries_list = document.querySelector('#countries-list')
let countries = document.querySelector('#countries')
countries.addEventListener('focus', adding_countries)

// let cities = document.querySelector('#cities')
// let cities_list = document.querySelector('#cities-list')
// cities.addEventListener('focus', adding_cities)

async function adding_countries() {
    console.log('in')
    fetch("https://countriesnow.space/api/v0.1/countries",
        // {method: "POST",
        // headers: { 'Content-Type': 'application/json' },
        // body: JSON.stringify({ "country": "egypt" })}
    )
        .then((res) => {
            if (!res.ok) {
                console.log('cant fetch an api for countries')
                throw new Error("can't fetch countries api")
            }
            return res.json()
        }).then((data) => {
            let arr = Array.from(data["data"])
            // console.log(arr)
            for (let i = 0; i < arr.length; i++) {
                let opt = document.createElement("option")
                opt.setAttribute('value', arr[i]["country"])
                opt.textContent = arr[i]["country"]
                countries_list.appendChild(opt)
                // console.log(opt)
                // console.log(arr[0])
                // console.log(arr[i]["data"]["country"] + "::: " + arr[i]]["data"]["country"]["cities"])
            }
        })
        .catch((error) => {
            console.error("fetch problem")
        });
    countries.removeEventListener('focus', adding_countries)
}
console.log('messi');
console.log(countries_list.firstElementChild);
// let countries_opt = querySelector()

// function adding_cities() {
//     fetch("https://countriesnow.space/api/v0.1/countries",
// {method: "POST",
// headers: { 'Content-Type': 'application/json' },
// body: JSON.stringify({ "country": "egypt" })}
// )
//     .then((res) => {
//         if (!res.ok) {
//             console.log('cant fetch an api for cities')
//             throw new Error("can't fetch cities api")
//         }
//         return res.json()
//     }).then((data) => {
//         let arr = Array.from(data["data"])
//         // console.log(arr)
//         for (let i = 0; i < arr.length; i++) {
//             console.log(arr[i])
// let opt = document.createElement("option")
// opt.setAttribute('value', arr[i]["country"])
// opt.textContent = arr[i]["country"]
// countries_list.appendChild(opt)
// console.log(opt)
// console.log(arr[0])
// console.log(arr[i]["data"]["country"] + "::: " + arr[i]]["data"]["country"]["cities"])
//             }
//         })
//         .catch((error) => {
//             console.error("fetch problem")
//         });
//     cities.removeEventListener('focus', adding_cities)
// }

// let hospitals = document.querySelector('.org-name')
// hospitals.onclick = function () {
//     fetch('http://www.communitybenefitinsight.org/api/get_hospital_data.php?hospital_id=1000', { mode: 'no-cors' })
//         .then(async (res) => {
//             if (!res.ok) {
//                 console.log("failed to fetch hospitals");
//                 return;
//             }
//             let data = await res.text()
//             console.log(data)
//         }).catch((err) => {
//             console.error("error fetching hospitals: ", err)
//         })
// }
