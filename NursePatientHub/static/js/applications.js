let logo_div = document.querySelector(".logo-div");
logo_div.onclick = function () {
    let url = "http://127.0.0.1:5000/";
    location.href = url;
}
let countries = document.querySelector('.position')
countries.onclick = function () {
    fetch("https://countriesnow.space/api/v0.1/countries",
        // {method: "POST",
        // headers: { 'Content-Type': 'application/json' },
        // body: JSON.stringify({ "country": "egypt" })}
    )
        .then((res) => {
            if (!res.ok) {
                console.log('cant fetch an api')
                throw new Error("can't fetch an api")
            }
            return res.json()
        }).then((data) => {
            let arr = Array.from(data["data"])
            // console.log(arr)
            for (let i = 0; i < arr.length; i++) {
                console.log(arr[i]["country"])
                // console.log(arr[0])
                // console.log(arr[i]["data"]["country"] + "::: " + arr[i]]["data"]["country"]["cities"])
            }
        })
        .catch((error) => {
            console.error("fetch problem")
        });
}
let hospitals = document.querySelector('.org-name')
hospitals.onclick = function () {
    fetch('http://www.communitybenefitinsight.org/api/get_hospital_data.php?hospital_id=1000', { mode: 'no-cors' })
        .then(async (res) => {
            if (!res.ok) {
                console.log("failed to fetch hospitals");
                return;
            }
            let data = await res.text()
            console.log(data)
        }).catch((err) => {
            console.error("error fetching hospitals: ", err)
        })
}
