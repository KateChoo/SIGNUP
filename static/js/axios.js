// axios.get('http://127.0.0.1:3000/api/users?username=1')
// .then(res =>{
//     console.log(res.data.data.name)
// })
// .catch(err =>{
//     console.log("ERROR")
// })
const fetch_name = async()=>{
    try{
        const res = await axios.get('http://127.0.0.1:3000/api/users?username=1')
        console.log(res.data.data.name)
    }catch(e){
        console.log("ERROR", e)
    }
}
fetch_name()