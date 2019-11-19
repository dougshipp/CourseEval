import numpy as np
import pyexcel as p
import sqlite3
from EvalScript import main


def main():
	#resetEvalStatus(1)
	testAnswers=[503445, "2019FA TEST-101 1", 0, 1, 2, 3, 4, 5, "I really liked this class", 0, 0, 0, "Word Question" ]
	blank=["","","","","","","",""]
	storeResponse(testAnswers)
	
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	cur.execute("SELECT * FROM Classes")
	asd= cur.fetchall()
	print("All stdents in all classes ",asd)

	#a= getValidClasses(123456)
	#print("getValidClasses: ",a)
	#b= getStudentInClassID(123456,a[0])
	#print("getStudentInClassID ",b)
	#c=hasNotTakenEval(b)
	#print(c)
	#d=getCourseInfo(1)
	#e=getStudentInClassID(123456,"2019FA TEST-101 1")
	#print("getCourseInfo: ",d)
	#print("getStudentInClassID: ",e)





def getValidClasses(sid):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	#print("sid: ",sid)
	if(validSID(sid)):
		cur.execute("SELECT * FROM Classes WHERE StudentID=? AND EvalStatus=?", (sid,0,))
		sidClasses= cur.fetchall()
		print("sidclasses: ",sidClasses)
		classList=[]
		if(sidClasses!=0):
			for i in range(len(sidClasses)):
				temp=sidClasses[i]
				cur.execute("SELECT * FROM Courses WHERE CourseId=?", (temp[2],))
				a= cur.fetchall()
				fullClass=" ".join(a[0][1:4])
				classList.append(fullClass)
			return classList
		print("Student ID not enroled in any classes.")
		return False
	print("Invalid Student ID")
	return False

def getCourseID(term, course, section):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	Term= str(term)
	CourseName= str(course)
	Section= str(section)
	print("input ",Term,CourseName,Section)

	cur.execute("SELECT * FROM Courses WHERE Section=? AND CourseName=? AND Term=?", (Section, CourseName, Term,))
	isCourse= cur.fetchall()
	print("Course Info: ",isCourse)
	if len(isCourse)!=0:
		print("course ID: ",isCourse[0][0])
		return isCourse[0][0]
	else:
		print("Invalid Course")
		return False

def getCourseInfo(studentInClassID):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	#print("studentInClassID: ",studentInClassID)
	cur.execute("SELECT * FROM Courses WHERE CourseId=? ", (studentInClassID,))
	studentincourseInfo= cur.fetchall()
	#print("studentincourseInfo: ",studentincourseInfo)
	if len(studentincourseInfo)!=0:
		#print("course ID: ",isCourse[0][0])
		return studentincourseInfo[0]
	else:
		print("Invalid Course")
		return False

def getStudentInClassID(studentID,courseString):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	#print("studentID: ",studentID)
	#print("courseString: ",courseString)
	listOfClassInfo=courseString.split(' ')
	courseID=getCourseID(listOfClassInfo[0],listOfClassInfo[1],listOfClassInfo[2])
	#print("courseID   : ",courseID)
	cur.execute('SELECT * FROM Classes WHERE StudentID=? AND Course=?', (studentID,courseID))
	isStudentInClass=cur.fetchall()
	#print("isStudentInClass: ",isStudentInClass[0][2])
	if (len(isStudentInClass)!=0):
		return isStudentInClass[0][2]
	else:
		print("Student not registered in that class")
		return False

def validSID(sid):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	#print("sid: ",sid)
	cur.execute("SELECT * FROM Students WHERE StudentID=?", (sid,))
	isStudent= cur.fetchall()
	if(len(isStudent)!=0):
		return True
	else:
		return False

def validStudentInClassId(studentInClassID):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	cur.execute("SELECT * FROM Classes WHERE ClassID=?", (studentInClassID,))
	isValid= cur.fetchall()
	if(len(isValid)!=0):
		return True
	else:
		return False

def changeEvalStatus(studentID,courseID):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	sid=studentID
	cid=courseID
	cur.execute('SELECT * FROM Classes WHERE StudentID=? AND Course=?', (sid,cid))	
	temp=cur.fetchall()
	if (len(temp)!=0 & temp[0][3]==0):
		cur.execute('UPDATE Classes SET EvalStatus = 1 WHERE StudentID=? AND Course=?', (sid,cid))
		connect.commit()
		print("Eval Status changed")
	else:
		print("EvalStatus Not Changed")

def changeEvalStatusByClass(studentInClassID):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	cur.execute('SELECT * FROM Classes WHERE ClassID=?', (studentInClassID,))	
	temp=cur.fetchall()
	if (len(temp)!=0):
		cur.execute('UPDATE Classes SET EvalStatus = 1 WHERE ClassID=?', (studentInClassID,))
		connect.commit()
		print("Eval Status changed")
	else:
		print("EvalStatus Not Changed")

def resetEvalStatus(studentInClassID):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	cur.execute('UPDATE Classes SET EvalStatus = 0 WHERE ClassID=?', (studentInClassID,))
	connect.commit()
	print("Eval Status changed")

def hasNotTakenEval(studentInClassID):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	if(validStudentInClassId(studentInClassID)):
		cur.execute('SELECT * FROM Classes WHERE ClassID=?', (studentInClassID,))
		temp=cur.fetchall()
		if(temp[0][3]==0):
			return True
		else:
			return False

	else:
		print("Invalid ID")
		return False

def tempstoreResponse(response):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	print("response: ",response)
	if(validSID(response[0])):
		studentClass=getStudentInClassID(response[0],response[1])
		courseInfo=getCourseInfo(studentClass)
		courseID=courseInfo[0]
		print("studentClassID: ",studentClass)
		print("courseInfo: ",courseInfo)
		print("courseID: ",courseID)
		response[0]=courseID
		print(response)



def storeResponse(response):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	if(validSID(response[0])):
		studentClass=getStudentInClassID(response[0],response[1])
		courseInfo=getCourseInfo(studentClass)
		courseID=courseInfo[0]
		# print("studentClassID: ",studentClass)
		# print("courseInfo: ",courseInfo)
		# print("courseID: ",courseID)
		if (hasNotTakenEval(studentClass)):
			#changeEvalStatus(response[0],courseID)
			changeEvalStatusByClass(studentClass)
			#cur.execute("INSERT INTO Responses VALUES (null, ?, ?)", (courseID, response[0],response[1],...))
			#connect.commit()
			print("Stored Response")
			return True
		else:
			print("Student has already taken eval")
			return False
	else:
		print("Invalid Student ID Number")
		return False


def returnClassResponses(courseID):
	connect = sqlite3.connect('evalDB.db')
	cur = connect.cursor()
	#cur.execute('SELECT * FROM Responses WHERE ClassID=?', (courseID,))
	temp=cur.fetchall()

	#for i in range(len(response)):

	#Parse Input 
	#Breakup data to get studentID,classID
	#cur.execute("INSERT INTO Responses VALUES (null, classID, studentID, courseString, answer1, answer2, answer3...)
	#Change Eval Status


#main()



