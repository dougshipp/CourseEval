import numpy as np
import pyexcel as p
import sqlite3

connect = sqlite3.connect('evalDB.db')
cur = connect.cursor()

def main():
	a= getClasses(123456)
	print(a)
	b= getStudentInClassID(123456,a[0])
	print(b)
	c=hasNotTakenEval(b)
	print(c)





def getValidClasses(sid):
	if(validSID(sid)):
		cur.execute("SELECT * FROM Classes WHERE StudentID=? AND EvalStatus=?", (sid,0,))
		sidClasses= cur.fetchall()
		classList=[]
		if(sidClasses!=0):
			for i in range(len(sidClasses)):
				temp=sidClasses[i]
				cur.execute("SELECT * FROM Courses WHERE CourseId=?", (temp[2],))
				a= cur.fetchall()
				fullClass=" ".join(a[i][1:4])

				classList.append(fullClass)
			return classList
		print("Student ID not enroled in any classes.")
		return False
	print("Invalid Student ID")
	return False

def getCourseID(term, course ,section):
	Term= str(term)
	CourseName= str(course)
	Section= str(section)
	#print("input ",Term,CourseName,Section)

	cur.execute("SELECT * FROM Courses WHERE Section=? AND CourseName=? AND Term=?", (Section, CourseName, Term,))
	isCourse= cur.fetchall()
	#print("Course Info: ",isCourse)
	if len(isCourse)!=0:
		#print("course ID: ",isCourse[0][0])
		return isCourse[0][0]
	else:
		print("Invalid Course")
		return False

def getStudentInClassID(studentID,courseString):
	listOfClassInfo=courseString.split(' ')
	courseID=getCourseID(listOfClassInfo[0],listOfClassInfo[1],listOfClassInfo[2])
	cur.execute('SELECT * FROM Classes WHERE StudentID=? AND Course=?', (studentID,courseID))
	isStudentInClass=cur.fetchall()
	if (len(isStudentInClass)!=0):
		return isStudentInClass[0][0]
	else:
		print("Student not registered in that class")
		return False

def validSID(sid):
	cur.execute("SELECT * FROM Students WHERE StudentID=?", (sid,))
	isStudent= cur.fetchall()
	if(len(isStudent)!=0):
		return True
	else:
		return False

def validStudentInClassId(studentInClassID):
	cur.execute("SELECT * FROM Classes WHERE ClassID=?", (studentInClassID,))
	isValid= cur.fetchall()
	if(len(isValid)!=0):
		return True
	else:
		return False

def changeEvalStatus(studentID,courseID):
	sid=studentID
	cid=classID
	cur.execute('SELECT * FROM Classes WHERE StudentID=? AND Course=?', (sid,cid))	
	temp=cur.fetchall()
	if (len(temp)!=0 & temp[0][3]==0):
		cur.execute('UPDATE Classes SET EvalStatus = 1 WHERE StudentID=? AND Course=?', (sid,cid))
		print("Eval Status changed")
	else:
		print("EvalStatus Not Changed")

def changeEvalStatus(studentInClassID):
	cur.execute('SELECT * FROM Classes WHERE ClassID=?', (studentInClassID,))	
	temp=cur.fetchall()
	if (len(temp)!=0):
		cur.execute('UPDATE Classes SET EvalStatus = 1 WHERE ClassID=?', (studentInClassID,))
		print("Eval Status changed")
		return True
	else:
		print("EvalStatus Not Changed")
		return False

def hasNotTakenEval(studentInClassID):
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

def storeResponse(response):
	print("I'm useless until I know what type of input I'm getting.")
	#Parse Input 
	#Breakup data to get studentID,classID
	#cur.execute("INSERT INTO Responses VALUES (null, classID, studentID, courseString, answer1, answer2, answer3...)
	#Change Eval Status



#main()