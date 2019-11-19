function doFirst() {
    document.getElementById("submit").addEventListener("click", combineQuestions);
}
window.addEventListener("load", doFirst, false);


function combineQuestions() {
    //var inputId = document.getElementById("idNum").value;
    //var inputCourse = document.getElementById("inputGroupSelect01").Value;
    var oldSid=sessionStorage.sid;
    var courseString=JSON.parse(sessionStorage.selectedCourse);
    console.log(oldSid);
    console.log(courseString);
    var a1= firstQuestion();
    var a2= secondQuestion();
    var a3= thirdQuestion();
    var answerList = [oldSid,courseString,a1, a2, a3];
    fetchCourses(answerList);
}

async function fetchCourses(answers) {
    //var temp={studentId: 123456}
    console.log("In fetch course");
    console.log(answers);
    const response = await sendData('/api/finishedResponse', answers);
    //var dropDown =document.getElementById("inputGroupSelect01");
    //console.log(dropDown);
    /* for(var i = 0; i < response.length; i++) {
        var opt = document.createElement('option');
        opt.innerHTML = response[i];
        opt.value = response[i];
        dropDown.appendChild(opt);
    } */
    console.log(response);
    newLocation();
} 
function newLocation() {
    console.log("in newLocation");
    window.location="http://127.0.0.1:5500/static/thanks.html";
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

