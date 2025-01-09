




function evaluateField(event){
    var index = document.getElementById("Inputindex").value;
    
    var index_str = index.slice(-1);
    var index_num = parseInt(index.slice(0,-1));
    console.log("str = "+index_str+"num = "+index_num);

    if (230000>index_num ||index_num>=240000 || !(/^[a-zA-Z]+$/.test(index_str))){
        alert("Index "+index+"is invalid !");
        return false;
    }

    var GPA = parseFloat(document.getElementById("InputGPA").value);
    if (0>GPA || GPA>4){
        alert("GPA: "+GPA +"is invalid!");
        return false;
    }

    var rank = parseInt(document.getElementById("Inputrank").value);
    
    if (1>rank || rank>1000){
        alert("Rank: "+rank+" is invalid!");
        return false;
    }
    
    

    var message = departmentPredictor(GPA,rank)
    
    openDialog(message);
    event.preventDefault();
    return true;
    
}


function departmentPredictor(GPA,rank){
    if (GPA >3.7){
        var message =  "You can apply to any department of preference. For more details of each department check the links below."
    }else if (GPA >=3.5){
        var message =  "You are eligible to be selected to any department excluding ENTC."
    }else if(GPA>=3.4){
        var message = "You are eligible to be selected to any department excluding ENTC and BME."
    }else{
        var message =  "You are eligible to be selected to any department excluding ENTC, BME, CSE and EE."
    }
    message="Congratulations on your results! "+message;
    return message
}

function openDialog(message){
    var dialog = document.getElementById("dialog");
    const dialogMessage = document.getElementById("customMessage");
    dialogMessage.textContent = message;
    
    
    dialog.classList.add("visible");
}

function closeDialog(){
    var dialog = document.getElementById("dialog");
    dialog.classList.remove("visible");
}
