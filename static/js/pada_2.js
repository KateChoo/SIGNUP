
const main_ = document.getElementById("taipei_fun");

fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json')
    .then(response => response.json())
    .then(data => {
        console.log(data.result)
        const main_ = document.getElementById("taipei_fun");
        const ul_ = document.createElement("ul");
        main_.appendChild(ul_)
        for(var i = 0; i<8;i++){
            let lis_ = document.createElement("li");
            let imgs = document.createElement("img");
            let ps = document.createElement("p");
            ul_.appendChild(lis_);
            lis_.appendChild(imgs);
            lis_.appendChild(ps);
            photo_http = 'http://www.travel.taipei/d_upload_ttn/'
            first_photo = data.result.results[i]['file'].split(photo_http)
            imgs.setAttribute("alt", data.result.results[i]['stitle']);
            imgs.setAttribute("src", photo_http + first_photo[1]);
            ps.textContent = data.result.results[i]['stitle']
        } 
    })
