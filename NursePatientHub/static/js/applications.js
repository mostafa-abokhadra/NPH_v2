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
// getting cities input element
let cities = document.querySelector('#cities')
// getting cities datalist element
let cities_list = document.querySelector('#cities-list')
// position element
let position = document.querySelector('#position')
let position_list = document.querySelector('#position_list')

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
// checking correct name of country
let countries_flag = -1; // making flag global to use in city function
// let cities_flag = -1; //
countries.onchange = async function () {
    if (countries.value === '') {
        countries.setAttribute('placeholder', "choose from the list")
        countries.setAttribute('style', 'outline: 1px solid red;')
        while (cities_list.childElementCount) {
            let ch = document.querySelector(cities_list.firstElementChild);
            cities_list.removeChild(ch);
            ch = document.querySelector(cities_list.firstElementChild);
        }
    } else {
        for (let i = 0; i < countries_cities.length; i++) {
            if (countries.value == countries_cities[i]["country"]) {
                countries_flag = i;
                break;
            }
        }
        if (countries_flag !== -1) {
            countries.setAttribute('placeholder', "Country")
            countries.setAttribute('style', '')
            // for (let i = 0; i < countries_cities.length; i++) {
            //     if (countries_cities[i]["country"] == countries.value) {
            //         cities_flag = i;
            //         break;
            //     }
            // }
            for (let i = 0; i < countries_cities[countries_flag].cities.length; i++) {
                let city_option = document.createElement('option');
                city_option.setAttribute('value', countries_cities[countries_flag].cities[i]);
                city_option.textContent = countries_cities[countries_flag].cities[i];
                cities_list.appendChild(city_option)
            }
            countries_flag = -1;
        }
        else {
            countries.setAttribute('style', 'outline: 1px solid red;')
            countries.setAttribute('placeholder', "choose from the list")
            while (cities_list.childElementCount) {
                let ch = document.querySelector(cities_list.firstElementChild);
                cities_list.removeChild(ch);
                ch = document.querySelector(cities_list.firstElementChild);
            }
        }
    }
}

cities.onfocus = async function () {
    if (countries.value === '') {
        cities.setAttribute('placeholder', 'please choose country first')
        cities.setAttribute('style', 'outline: 1px solid red;')
        while (cities_list.childElementCount) {
            console.log('still have')
            let ch = document.querySelector(cities_list.firstElementChild);
            cities_list.removeChild(ch);
            ch = document.querySelector(cities_list.firstElementChild);
        }
    } else {
        cities.setAttribute('placeholder', 'City')
        cities.setAttribute('style', '')
    }
}
pos_flag = -1;
position.onchange = function () {
    let i;
    for (i = 0; i < position_list.childElementCount; i++) {
        if (position.value === position_list.children[i].textContent) {
            pos_flag = 1;
            break;
        }
    }
    if (pos_flag === 1) {
        position.setAttribute('style', '')
        pos_flag = -1;
    } else {
        position.setAttribute('style', 'outline: 1px solid red; color: red;')
        pos_flag = -1;
    }
}