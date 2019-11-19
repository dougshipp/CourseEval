from flask import Flask, request, g, render_template, jsonify
from helperFunctions import *
from EvalScript import main
#import helperFunctions as do
#from EvalScript import getNewStudentID

app = Flask(__name__,
	 		static_url_path='/static', 
            static_folder='static')
app.config["DEBUG"] = True
DATABASE = 'evalDB.db'


@app.route("/api/courses", methods=["POST","GET"])
def getCoruses():
    requestBody= request.get_json()
    #sid=requestBody['studentId']
    sid=requestBody[0:len(requestBody)]
    if(validSID(sid)):
        print("Stuent Id: ", sid)
        courses= getValidClasses(sid)
        print("response: ", courses)
        #nextPage("questionsOne.html")
        return jsonify(courses)
    else:
        errorMessage="Invalid Student ID Number"
        return jsonify(errorMessage)
#def nextPage(page):
#    return render_template(page)

#@app.route("/api/courses", methods=["POST","GET"])
#def selectedCourse():


@app.route("/api/finishedResponse", methods=["POST"])
def getRespnse():
    print("Getting Response")
    # requestBody= request.get_json()
    # print(requestBody)
    # finshedResponse=requestBody['listOfAnswersWithStudentID&CourseStringInFront']
    # print("Response: ", finshedResponse)
    # store= storeResponse(finshedResponse)
    requestBody= request.get_json()
    answers=requestBody[0:len(requestBody)]
    tempstoreResponse(answers)
    print("answers: ",answers)
    returnable="Successful?"
    return jsonify(returnable)
     




# @app.route("/student", methods=["Get"])
# def getStudentData():
# 	# go get some data from the db

def render_static():
    return render_template('index.html')

if __name__ == '__main__':
    main()
    app.run(host="localhost", port=5500, debug=True)
