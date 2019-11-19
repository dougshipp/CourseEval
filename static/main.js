function doFirst() {
    document.getElementById("button").addEventListener("click", validate);
    //document.getElementById("submit").addEventListener("click", combineQuestions);
}
window.addEventListener("load", doFirst, false);

function validate() {
    var inputId = document.getElementById("idNum").value;
    //sendData('/api/courses', inputId);
    console.log(inputId);
    console.log("Done");
    fetchCourses(inputId);
    
}


async function fetchCourses(sid) {
    //var temp={studentId: 123456}
    console.log("In fetch course");
    console.log(sid);
    const response = await sendData('/api/courses', document.getElementById("idNum").value);
    //var dropDown =document.getElementById("inputGroupSelect01");
    //console.log(dropDown);
    /* for(var i = 0; i < response.length; i++) {
        var opt = document.createElement('option');
        opt.innerHTML = response[i];
        opt.value = response[i];
        dropDown.appendChild(opt);
    } */
    console.log(response);
    if (!(response === "Invalid Student ID Number")){
        newLocation(sid,response);
    }
} 
function newLocation(sid,courses) {
    //sessionStorage.setItem('sid', sid)
    sessionStorage.sid = sid;
    
    sessionStorage.courses = JSON.stringify(courses);
    console.log(sessionStorage.courses);
    console.log("in newLocation");
    //window.location="http://127.0.0.1:5500/static/dropdown.html?Name="+sid;
    window.location="http://127.0.0.1:5500/static/dropdown.html";
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

