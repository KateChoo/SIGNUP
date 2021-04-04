const container = document.querySelector(".story");
const btn = document.querySelector("button");
const message = document.querySelector(".message");
btn.addEventListener("click", create);
var today = new Date();
var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
var dateTime = date+' '+time;

window.addEventListener('load', pressHint)
btn.addEventListener('click', hintToggle)
function create(){
  let text = document.createElement("INPUT"); 
  let textarea = document.createElement("TEXTAREA");
  let delete_btn = document.createElement("BUTTON");
  let add_btn = document.createElement("BUTTON");
  container.appendChild(text);
  container.appendChild(textarea);
  container.appendChild(delete_btn);
  container.appendChild(add_btn);
  text.setAttribute("placeholder", "Name");
  textarea.setAttribute("placeholder", "Message us?");
  delete_btn.textContent = "刪除內容";
  add_btn.textContent = "寫到留言板";
    
    add_btn.addEventListener("click", addToMessage)
    delete_btn.addEventListener("click", del_textarea)


    function del_textarea(){
        text.value="";
        textarea.value ="";
    }

    btn.disabled = true;
    function addToMessage(){
        if(textarea.value){
            btn.disabled = false;
            let showName = document.createElement("SPAN");
            let showMessage = document.createElement("SPAN");
            let delMessage = document.createElement("BUTTON");
            let editMessage = document.createElement("BUTTON");
            let showTime = document.createElement("SPAN");
            message.appendChild(showName);
            message.appendChild(showMessage);
            message.appendChild(delMessage);
            message.appendChild(editMessage);
            message.appendChild(showTime);
            delMessage.textContent = "刪除留言";
            editMessage.textContent = "編輯留言";
            showName.innerHTML = text.value +"說:";
            showMessage.classList.add("edit");
            showMessage.innerHTML = textarea.value;
            textarea.value = "";
            showTime.textContent = dateTime;
            delete_btn.remove();
            text.remove();
            textarea.remove();
            add_btn.remove();
            
            delMessage.addEventListener("click", function(){
                this.remove();
                showName.remove();
                showMessage.remove();
                editMessage.remove();
                showTime.remove();
            })

            editMessage.addEventListener("click", function(e){
                let editMessageText = e.target.previousElementSibling.previousElementSibling;
                if(editMessageText.classList.contains('edit')){
                    let message_text = e.target.closest("div.message").querySelector("span.edit").innerText;
                    //let editMessageText =   e.target.previousElementSibling.previousElementSibling;
                    editMessageText.innerHTML = '<input type="text" value="' + message_text + '">';
                    editMessageText.classList.remove('edit')
                    
                }else if(!editMessageText.classList.contains('edit')){
                    editMessageText.classList.add('edit')
                    let message_text = e.target.closest("div.message").querySelector("span.edit").innerText;
                    editMessageText.textContent = 'HI還沒加上';//editMessageText.....
                    //editMessageText.textContent = message_text
                }
            })
        }
        //localStorage
        let task = {
        "item_id": dateTime,
        "name": text.value,
        "topic": textarea.value, 
        };
        let tasks = JSON.parse(localStorage.getItem("tasks"));
        if (tasks) { 
        tasks.unshift(task);  //exist
        } else { 
        tasks = [task];       //not
        }
        localStorage.setItem("tasks", JSON.stringify(tasks));
        return;
        //localStorage
    }  
}

    function pressHint(){
        btn.classList.add('pressHint')
    }
    function hintToggle(){
        btn.classList.remove('pressHint')
    }
