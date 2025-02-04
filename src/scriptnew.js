




function evaluateField(event){
    var index = document.getElementById("Inputindex").value;
    
    var index_str = index.slice(-1);
    var index_num = parseInt(index.slice(0,-1));
    console.log("str = "+index_str+"num = "+index_num);
    
    
    if (230000>index_num ||index_num>=240000 || !(/^[a-zA-Z]+$/.test(index_str))){
        alert("Index "+index+"is invalid !");
        return false;
    }
    const GPA = parseFloat(document.getElementById("InputGPA").value);
    const rank = parseInt(document.getElementById("Inputrank").value);
    
    if (0>GPA || GPA>4){
        alert("GPA: "+GPA +"is invalid!");
        return false;
    }

    
    
    if (1>rank || rank>1000){
        alert("Rank: "+rank+" is invalid!");
        return false;
    }
    
    
    

    fetch("http://127.0.0.1:5000/predict",{
        
        method:"POST",
        headers:{"Content-Type":'application/json'
        },
        body:JSON.stringify({GPA:GPA,Rank:rank})

    })
    .then(response=>response.json()) /*The response is converted to a JSON format */
    .then(data=> {
        if (data.error){
            openDialog(`JS1Error:${data.error}`);
            return;
        
        }
        let resultMsg = "Top 3 predicted Departments:<br>";
        for(const [dept,prob] of Object.entries(data)){
            resultMsg+=`✅<b>${dept}</b>: ${(prob*100).toFixed(2)}%<br>`;
        }

        openDialog(resultMsg);
    })
    .catch(error=>{
        console.error("JSError:",error);
        openDialog("Error:"+error);
    });
    event.preventDefault();
    return true;
    
}



function openDialog(message){
    var dialog = document.getElementById("dialog");
    const dialogMessage = document.getElementById("customMessage");
    dialogMessage.innerHTML = message;
    
    
    dialog.classList.add("visible");
}

function closeDialog(){
    var dialog = document.getElementById("dialog");
    dialog.classList.remove("visible");
}
