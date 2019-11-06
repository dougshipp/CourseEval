from flask import Flask, request, g, render_template, jsonify
from helperFunctions import *
#import helperFunctions as do
#from EvalScript import getNewStudentID

app = Flask(__name__,
	 		static_url_path='', 
            static_folder='public')
app.config["DEBUG"] = True
DATABASE = 'evalDB.db'



@app.route("/api/courses", methods=["POST"])
def getCourses():
    print("hello!!!")
    requestBody= request.get_json()
    sid=requestBody['studentId']
    print("Student Id: ", sid)
    courses= getValidClasses(sid)
    return jsonify(courses)

@app.route("/api/finishedResponse", methods=["POST"])
def getResponse():
    requestBody= request.get_json()
    finshedResponse=requestBody['listOfAnswersWithStudentID&CourseStringInFront']
    print("Response: ", finshedResponse)
    store= storeResponse(finshedResponse)
    return 



# @app.route("/student", methods=["Get"])
# def getStudentData():
# 	# go get some data from the db

def render_static():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
