document.getElementById("get_form").addEventListener('submit', getName);

function getName(e){
    e.preventDefault();
    var xhr = new XMLHttpRequest();
    var search_name = document.getElementById("search_name").value;
    xhr.open('GET','/api/users?username=' + search_name, true);
    xhr.onload = function(){
        if(this.status == 200){
            console.log(`xhr this.responseText: ${this.responseText}`)
            var user = JSON.parse(this.responseText)
            var output = '';
            console.log(`user.data/xhr JSON.parse(this.responseText): ${user.data}`) //[object Object]
            output = JSON.stringify(user.data.name).replace('"', "").replace('"', "");
            console.log(`xhr name (output): ${output}`)  
            //output = this.responseText;
            
        }
        // if (output){
            document.getElementById("show_name").textContent = (`${output} (${search_name})`);
            // let span = document.createElement("span")
            // span.setAttribute("id", "show_username");
            // document.getElementById("show_name").appendChild(span);
            // document.getElementById("show_name").textContent = (`${output}`);
            // console.log(`name: ${name}`);
            // console.log(`search_name: ${document.getElementById("search_name").value}`)
            // console.log(`show_username: ${document.getElementById("show_username")}`)
            // document.getElementsByTagName("span")[0].textContent = (`(${search_name})`);
        // }else if (user.data === null){
        //     document.getElementById("show_name").textContent = (`查無此人`);
        // }
    }
    xhr.send();
    document.getElementById("show_name").textContent.value = "";
}

// function postName(e){
//     e.preventDefault();
//     var xhr = new XMLHttpRequest();

//     var name = document.getElementById("search_name").value;
//     var params = 'username=' + name
//     xhr.open('POST','/api/users', true);
//     xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
//     xhr.onload = function(){
//         console.log(this.responseText)
//     }
//     xhr.send();
// }




// function loadUser(){
//     var xhr = new XMLHttpRequest();
//     var name = document.getElementById("search_name").value;

//     xhr.open('GET','/api/users?username=' + name, true);
//     xhr.onload = function(){
//         if(this.status == 200){
//             console.log(this.responseText.data)
//             var user = JSON.parse(this.responseText)
//             var output = '';
//             output = this.responseText;
//         }
//         document.getElementById("user").innerHTML = output;
//     }
//     xhr.send();
// }





// fetch('http://127.0.0.1:3000/api/users?username=${g.username}')
// //fetch('https://reqres.in/api/users')
//     .then(response => {
//         if(!response.ok){
//             throw Error("ERROR");
//         }
//         return response.json();
//     }) 
//     .then(data => {
//         console.log(data);
//         console.log(data.data.name);
//         console.log('hello')
//         document
//             .getElementById("search_api")
//             .textContent = (data.data.name);
//     })
//     // .catch(error =>{
//     //     console.log(error);
//     // })
