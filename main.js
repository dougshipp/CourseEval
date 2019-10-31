function doFirst() {
    document.getElementById("button").addEventListener("click", validate);
}
window.addEventListener("load", doFirst, false);

function validate() {
    var inputId = document.getElementById("idNum").nodeValue;
    var inputCourse = document.getElementById("inputGroupSelect01").nodeValue;
    console.log(inputId);
    console.log(inputCourse);
    console.log("Done");
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

