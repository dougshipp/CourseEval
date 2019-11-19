function doFirst() {
    console.log("started");
    document.getElementById("button").addEventListener("click", validate);
    //document.getElementById("submit").addEventListener("click", combineQuestions);
    //var sid=window.location.search.substr(1);
    var oldSid=sessionStorage.sid;
    var cList=JSON.parse(sessionStorage.courses);
    console.log(cList);
    console.log(oldSid);
    var select = document.getElementById("inputGroupSelect01"); 

    for(var i = 0; i < cList.length; i++) {
        var opt = cList[i];
        var el = document.createElement("option");
        el.text = opt;
        el.value = opt;
        select.add(el);
    }

}
window.addEventListener("load", doFirst, false);

function validate() {
    var e= document.getElementById("inputGroupSelect01");
    var inputCourse = e.options[e.selectedIndex].text;
    console.log(inputCourse);
    if (!(inputCourse === "" | inputCourse ==="Choose..." )){
        sessionStorage.selectedCourse = JSON.stringify(inputCourse);
    newLocation();
    }
    //var temp=JSON.parse(sessionStorage.selectedCourse);
    //console.log(temp);
}

// function combineQuestions() {
//     //var inputId = document.getElementById("idNum").value;
//     //var inputCourse = document.getElementById("inputGroupSelect01").Value;
//     var a1= firstQuestion();
//     var a2= secondQuestion();
//     var a3= thirdQuestion()
//     var answerList = [a1, a2, a3];
//     const answers= sendData('/api/finishedResponse', answerList);
//     console.log(answers);
// }

function newLocation() {
    console.log("in newLocation");
    window.location="http://127.0.0.1:5500/static/questionsOne.html";
}
async function sendData(url, data) {
    console.log("data sent");
    console.log(url);
    //data=document.getElementById("idNum").value;
    console.log(data);
    const response = await fetch(url,
        {
            method: 'POST',
            headers: {
                "content-type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );
    return await response.json();
}


function Student(studentId, courses, evalId, status) 
{
    this.studentId = studentId;
    this.courses = courses;
    this.evalId = evalId;
    this.status = status;
}


    course1 = {
        classRoster: ["123456"]
    },
    course2 = {
        classRoster: ["000000"]
    },
    course3 = {
        classRoster: ["111111"]
    }

