// logo link go to home page
let logo_div = document.querySelector(".logo-div");
logo_div.onclick = function () {
    let url = "http://127.0.0.1:5000/";
    location.href = url;
}
// declaring fetch list of objects
countries_cities = [];
// object contain countryName: [list of cities]
country_city = {}

// getting countries datalist element
let countries_list = document.querySelector('#countries-list')
// gettingg countries input element
let countries = document.querySelector('#countries')
countries.addEventListener('focus', adding_countries)

async function adding_countries() {
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
            for (let i = 0; i < arr.length; i++) {
                country_city = {
                    country: arr[i]["country"],
                    cities: arr[i]["cities"]
                }
                countries_cities.push(Object(country_city))
                // adding < option > countryName </option > to datalist
                let opt = document.createElement("option")
                opt.setAttribute('value', arr[i]["country"])
                opt.textContent = arr[i]["country"]
                countries_list.appendChild(opt)
            }
        })
        .catch((error) => {
            console.error("fetch problem")
        });
    // removing event so fetching data don't occur with every focus (only the first one)
    countries.removeEventListener('focus', adding_countries)
}
// countries.onchange = function () {
//     console.log(countries.value)
// }

// getting cities input element
let cities = document.querySelector('#cities')
// getting cities datalist element
let cities_list = document.querySelector('#cities-list')
cities.addEventListener('focus', adding_cities)

async function adding_cities() {
    if (countries.value == '') {
        // because fetching cities is depending on country value
        cities.setAttribute('placeholder', 'please choose country first')
        cities.setAttribute('style', 'outline: 1px solid red;')
    }
    else {
        cities.setAttribute('style', '')
        let flag = -1;
        for (let i = 0; i < countries_cities.length; i++) {
            if (countries_cities[i]["country"] == countries.value) {
                flag = i;
                break;
            }
        }
        if (flag === -1) {
            countries.setAttribute('placeholder', 'choose from the list')
            countries.setAttribute('style', 'outline: 1px solid red;')
        } else {
            for (let i = 0; i < countries_cities[flag].cities.length; i++) {
                let city_option = document.createElement('option');
                city_option.setAttribute('value', countries_cities[flag].cities[i]);
                city_option.textContent = countries_cities[flag].cities[i];
                cities_list.appendChild(city_option)
            }
        }
    }
}

// console.log('messi');
// console.log(countries_list.firstElementChild);
// let countries_opt = querySelector()


// function adding_cities() {
//     fetch("https://countriesnow.space/api/v0.1/countries",
//         {
//             method: "POST",
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify({ "country": "egypt" })
//         }
//     )
//         .then((res) => {
//             if (!res.ok) {
//                 console.log('cant fetch an api for cities')
//                 throw new Error("can't fetch cities api")
//             }
//             return res.json()
//         }).then((data) => {
//             let arr = Array.from(data["data"])
//             // console.log(arr)
//             for (let i = 0; i < arr.length; i++) {
//                 console.log(arr[i])
//                 let opt = document.createElement("option")
//                 opt.setAttribute('value', arr[i]["country"])
//                 opt.textContent = arr[i]["country"]
//                 countries_list.appendChild(opt)
//                 console.log(opt)
//                 console.log(arr[0])
//                 console.log(arr[i]["data"]["country"] + "::: " + arr[i]]["data"]["country"]["cities"])
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
