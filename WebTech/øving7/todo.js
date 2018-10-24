document.querySelector("#addBtn").addEventListener("click", addTask);

let numberOfTasks = 0;
let tasks = [];

function addTask() {
    let newCheck = document.createElement("input");
    newCheck.type = "checkbox";
    newCheck.name = "newCheck";
    newCheck.className = "newCheck";
    newCheck.addEventListener("click", function() {
        
        document.querySelector("#antChk").innerHTML = document.querySelectorAll("input[type='checkbox']:checked").length;


    });
    let newLi = document.createElement("li");
    newLi.id = "newLi" + numberOfTasks
    newLi.appendChild(newCheck);
    let newLabel = document.createElement("label");
    newLabel.control = "newCheck";
    newLabel.innerHTML = document.querySelector("#inpField").value;
    newLi.appendChild(newLabel);

    document.querySelector("#elList").insertAdjacentElement("afterbegin", newLi);
    document.querySelector("#inpField").value = "";
    document.querySelector("#inpField").focus();
    numberOfTasks +=1;
    let d = new Date();
    let n = d.getTime();
    let strName = newLabel.innerHTML;
    let task = {name:strName, id:n};
    tasks.push(task);
    console.log(tasks);
    document.querySelector("#antTot").innerHTML = tasks.length;
}
let antChk = 0;
function calculatoPotato() {
    for (let i=0;i<tasks.length;i++) {
        if(document.querySelectorAll(".newCheck")[i].checked == true) {
            newArray.push(document.querySelectorAll(".newCheck")[i]);
        } else if(document.querySelectorAll(".newCheck")[i].checked == true) {
            newArray.splice(indexOf(document.querySelectorAll(".newCheck")[i]));
        }
       //document.querySelector("#" + this.parentElement.children[1]).;
        //document.querySelector("#antChk").innerHTML =
    }
}