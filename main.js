function doFirst() {
    document.getElementById("button").addEventListener("click", validate);
}
window.addEventListener("load", doFirst, false);

async function fetchCourses(inputId) 
{
        const response = await sendData('/api/courses', {inputId});
        console.log(response);
} 
    
    async function sendData(url, data) {
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


function validate() 
{
    var inputId = document.getElementById("idNum").value;
    var inputCourse = document.getElementById("courses").value;
    console.log(sendData('/api/courses',inputId));
    console.log(inputId); 
    console.log(inputCourse);
    console.log("Done");
}


function Student(studentId, courses, evalId, status) {
    this.studentId = studentId;
    this.courses = courses;
    this.evalId = evalId;
    this.status = status;
}


let courses = {
    name: "course1",
    classRoster: "123456"
}
