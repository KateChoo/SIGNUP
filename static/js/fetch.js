var url = new URL('http://127.0.0.1:3000/api/users?username=')
var params = document.getElementById("search_name").value;
url.search = new URLSearchParams(params).toString();
// fetch('http://127.0.0.1:3000/api/users?username=1')
fetch(url.search)
.then(response => {
            if(!response.ok){
                throw Error("ERROR");
            }
            return response.json();
        }) 
        .then(data => {
            console.log(data.data);
            console.log('hi');
            // var search_name = document.getElementById("search_name").value;
            // document.getElementById("user").innerHTML = 'get_form';
            // document.getElementById("show_name").innerHTML = search_name;
            // console.log(data.data.name);
            // console.log('hello')
            // document
            //     .getElementById("search_api")
            //     .textContent = (data.data.name);
        })
        .catch(error =>{
            console.log(error);
        })