function doFirst() {
    var button = document.getElementById("button");
    button.addEventListener("click", saveLogin, false);
}
window.addEventListener("load", doFirst, false);

function saveLogin() {
    var inputId = document.getElementById("idNum").nodeValue;
    var inputCourse = document.getElementById("inputGroupSelect01").nodeValue;
    sessionStorage.setItem(inputId, inputCourse);
}

function checkLogin(Courses) {
    var id = sessionStorage.getItem(inputId);
    
    
}


function Student(studentId, courses, evalId, status) {
    this.studentId = studentId;
    this.courses = courses;
    this.evalId = evalId;
    this.status = status;
}

var Courses = {
    course1 = {
        classRoster: ["123456"]
    },
    course2 = {
        classRoster: ["000000"]
    },
    course3 = {
        classRoster: ["111111"]
    }
}

