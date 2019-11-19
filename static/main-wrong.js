//THIS IS THE WRONG FILE


function doFirst() {
    document.getElementById("button").addEventListener("click", validate);
    //document.getElementById("submit").addEventListener("click", combineQuestions);
}
window.addEventListener("load", doFirst, false);
//window.addEventListener("load", doFirst, false);

function validate() {
    var inputId = document.getElementById("idNum").value;
    var inputCourse = document.getElementById("inputGroupSelect01").Value;
    //sendData('/api/courses', inputId);
    console.log(inputId);
    console.log(inputCourse);
    console.log("Done");
    fetchCourses(inputId);
    
}

function combineQuestions() {
        //var inputId = document.getElementById("idNum").value;
        //var inputCourse = document.getElementById("inputGroupSelect01").Value;
        var a1= firstQuestion();
        var a2= secondQuestion();
        var a3= thirdQuestion()
        var answerList = [a1, a2, a3];
        const answers= sendData('/api/finishedResponse', answerList);
        console.log(answers);
    }

async function fetchCourses(sid) {
    //var temp={studentId: 123456}
    const response = await sendData('/api/courses', sid);
    console.log(response);
} 

async function sendData(url, data) {
    console.log("data sent");
    console.log(url);
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

// function doFirst() {
//     document.getElementById("button").addEventListener("click", validate);
//     //document.getElementById("submit").addEventListener("click", combineQuestions);
// }
// window.addEventListener("load", doFirst, false);
// window.addEventListener("load", doFirst, false);

// function validate() {
//     var inputId = document.getElementById("idNum").value;
//     var inputCourse = document.getElementById("inputGroupSelect01").Value;
//     //sendData('/api/courses', inputId);
//     console.log(inputId);
//     console.log(inputCourse);
//     console.log("Done");
//     fetchCourses(inputId);
    
// }

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

// async function fetchCourses(sid) {
//     //var temp={studentId: 123456}
//     console.log("In fetch course");
//     console.log(sid);
//     const response = await sendData('/api/courses', sid);
//     //var dropDown =document.getElementById("inputGroupSelect01");
//     //console.log(dropDown);
//     /* for(var i = 0; i < response.length; i++) {
//         var opt = document.createElement('option');
//         opt.innerHTML = response[i];
//         opt.value = response[i];
//         dropDown.appendChild(opt);
//     } */
//     console.log(response);
// } 

// async function sendData(url, data) {
//     console.log("data sent");
//     console.log(url);
//     console.log(data);
//     const response = await fetch(url,
//         {
//             method: 'POST',
//             headers: {
//                 "content-type": "application/json"
//             },
//             body: JSON.stringify(data)
//         }
//     );
//     return await response.json();
// }



