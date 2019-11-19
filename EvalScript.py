from __future__ import print_function
from googleapiclient import errors
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
import pandas as pd
import numpy as np
import pyexcel as p
import sqlite3
import json
from flask import Flask, jsonify, g, redirect, request, url_for
import http.client


#api key=AIzaSyDcP4DeUolqv5liM5xmus0eArmG0xdXz5c
#Current API ID:
#MUc_fNSsqUCUHD9t-hgeICJaQPOQEcK-0
#MUc_fNSsqUCUHD9t-hgeICJaQPOQEcK-0

#One isue is we need to give eval update a term, coursename, and section 

#textFile= "TestRoster.xlsx"
my_dict = p.get_array(file_name="TestRoster.xlsx", name_columns_by_row=0)
#print(my_dict[1])



connect = sqlite3.connect('evalDB.db')
cur = connect.cursor()
def main():

	# cur.execute("CREATE TABLE Courses(CourseId    INTEGER PRIMARY KEY, Term  TEXT NOT NULL, CourseName  TEXT NOT NULL, Section  TEXT NOT NULL, Instructor INTEGER NOT NULL, FOREIGN KEY(Instructor) REFERENCES Instructors(InstructorID));")
	# cur.execute("CREATE TABLE Instructors(InstructorID    INTEGER PRIMARY KEY AUTOINCREMENT, Name  TEXT NOT NULL, Email  TEXT NOT NULL);")
	# cur.execute("CREATE TABLE Students(ID INTEGER PRIMARY KEY, StudentID  INTEGER NOT NULL, Email  TEXT NOT NULL );")
	# cur.execute("CREATE TABLE Classes(ClassID INTEGER PRIMARY KEY, StudentID  INTEGER NOT NULL, Course  INTEGER NOT NULL, EvalStatus  INTEGER DEFAULT 0, FOREIGN KEY(StudentID) REFERENCES Students(StudentID) FOREIGN KEY(Course) REFERENCES Courses(CourseId) );")
	#cur.execute("CREATE TABLE Responses(ID INTEGER PRIMARY KEY, StudentID  INTEGER NOT NULL, Email  TEXT NOT NULL );")
	#dropTableStatement = "DROP TABLE Classes"
	#cur.execute(dropTableStatement)
	# dropTableStatement = "DROP TABLE Eval"
	# cur.execute(dropTableStatement)

	#cur.execute("CREATE TABLE Eval(EvalID INTEGER PRIMARY KEY, classID  INTEGER NOT NULL, EvalStatus  INTEGER DEFAULT 0, FOREIGN KEY(classID) REFERENCES Classes(ClassID));")


	addStudents()
	addInstructors()
	addCourse()
	addStudentToClass()
	#changeEvalStatus(555555,0)
	#createEvalList()
	connect.commit()
	#print(my_dict)

	#print("new student id: ",getNewStudentID(123456))
	# print("get studentinclass id ",getStudentInClassID(my_dict[1][7], getCourseID(str(my_dict[1][0]),str(my_dict[1][1]),str(my_dict[1][2]))))
	# print(getClasses(123456))

	# cur.execute('SELECT * FROM Students')
	# a = cur.fetchall()
	# print ("Students ", a)

	# cur.execute('SELECT * FROM Instructors')
	# b = cur.fetchall()
	# print ("Instructors ", b)

	# cur.execute('SELECT * FROM Courses')
	# c= cur.fetchall()
	# print ("Courses ", c)

	# cur.execute('SELECT * FROM Classes')
	# d= cur.fetchall()
	# print ("Students In Classes ", d)


#Function to fill Students tables from a given class roster.
def addStudents():
	#print(my_dict)
	#Iterates through the every student in the class roster
	for i in range(1, len(my_dict)):
		#print(len(my_dict))
		studentID=my_dict[i][7]	#gets the student's ID from the file
		email=my_dict[i][8]	#gets the student's email from the file
		#print (studentID,email)
		cur.execute('SELECT * FROM Students WHERE StudentID=?', (studentID,)) #checks to make sure the student doesnt already exist
		isStudent = cur.fetchall()
		if len(isStudent)==0:
			cur.execute("INSERT INTO Students VALUES (null, ?, ?)", (studentID, email))
		else:	
			print("Student Already Exsists")
			

	
		#cur.execute("DELETE FROM Students WHERE email LIKE 'k16ns01@kzoo.edu'")

	cur.execute('SELECT * FROM Students')
	data_3 = cur.fetchall()
	print ("Students ", data_3)

def addInstructors():
		instructorName=my_dict[1][5]
		email="fake@email.com"
		#print("Instructor name",instructorName)
		cur.execute("SELECT * FROM Instructors WHERE Name=?", (instructorName,))
		isInstructor = cur.fetchall()
		#print(isInstructor)
		if len(isInstructor)==0:	
			cur.execute("INSERT INTO Instructors VALUES (null, ?, ?)", (instructorName, email))
			#cur.execute("DELETE FROM Instructors WHERE email LIKE 'fake@email.com'")
		else:
			print("Instructor Already Exsists")

		# cur.execute('SELECT * FROM Instructors')
		# data_5 = cur.fetchall()
		# print ("Instructors ", data_5)
			
def addCourse():
	for i in range(1, len(my_dict)):
		Term= str(my_dict[i][0])
		CourseName= str(my_dict[i][1])
		Section= str(my_dict[i][2])
		instructorName=my_dict[i][5]
		cur.execute("SELECT * FROM Instructors WHERE Name=?", (instructorName,))
		InstructorID = cur.fetchall()[0]

		cur.execute("SELECT * FROM Courses WHERE Section=? AND CourseName=? AND Term=?", (Section, CourseName, Term,))
		isClass = cur.fetchall()
		#print("class info: ", isClass)
		if len(isClass)==0:
			#print(Term, CourseName, instructorName, InstructorID[0])
			cur.execute("INSERT INTO Courses VALUES (null, ?, ?, ?, ?)", (Term, CourseName, Section, InstructorID[0]))

		print("Course Already Exsists")
	#cur.execute("DELETE FROM Courses WHERE CourseId LIKE '1'")
	# cur.execute('SELECT * FROM Courses')
	# data_6= cur.fetchall()
	# print ("Courses ", data_6)

def getCourseID(t, c ,s):
	Term= str(t)
	CourseName= str(c)
	Section= str(s)
	#print("input ",Term,CourseName,Section)

	cur.execute("SELECT * FROM Courses WHERE Section=? AND CourseName=? AND Term=?", (Section, CourseName, Term,))
	isCourse= cur.fetchall()
	#print("Course Info: ",isCourse)
	if len(isCourse)!=0:
		#print("course ID: ",isCourse[0][0])
		return isCourse[0][0]
	else:
		print("No Course Found")
		return

def getNewStudentID(idnum):
	sid= idnum

	cur.execute('SELECT * FROM Students WHERE StudentID=?', (sid,))	
	isStudent= cur.fetchall()
	#print("Course Info: ",isCourse)
	if len(isStudent)!=0:
		#print("course ID: ",isCourse[0][0])
		return isStudent[0][0]
	else:
		print("No Student Found")
		return

def getStudentInClassID(idnum,courseID):
	sid= idnum
	c=courseID
	cur.execute('SELECT * FROM Classes WHERE StudentID=? AND Course=?', (sid,c))	
	found= cur.fetchall()
	#print("Course Info: ",isCourse)
	if len(found)!=0:
		#print("course ID: ",isCourse[0][0])
		return found[0][0]
	else:
		print("Student Not In Class")
		return


def changeEvalStatus(studentID,classID):
	sid=studentID
	cid=classID
	cur.execute('SELECT * FROM Classes WHERE StudentID=? AND Course=?', (sid,cid))	
	temp=cur.fetchall()
	if (len(temp)!=0 & temp[0][3]==0):
		cur.execute('UPDATE Classes SET EvalStatus = 1 WHERE StudentID=? AND Course=?', (sid,cid))
		print("Eval Status changed")
	else:
		print("EvalStatus Not Changed")


def addStudentToClass():
	for i in range(1, len(my_dict)):
		studentID=my_dict[i][7]
		Term= str(my_dict[i][0])
		CourseName= str(my_dict[i][1])
		Section= str(my_dict[i][2])
		coID=getCourseID(Term,CourseName,Section)

		#print("course ID: ",coID)
		#print("Student ID", studentID)
		cur.execute("SELECT * FROM Classes WHERE StudentID=? AND Course=?", (studentID, coID,))
		inClass= cur.fetchall()
		#print("In Class: ",inClass)
		if len(inClass)==0:
			cur.execute("INSERT INTO Classes VALUES (null, ?, ?, 0)", (studentID, coID))
			# print("Student Already In Class")

def getClasses(sid):
	cur.execute("SELECT * FROM Classes WHERE StudentID=?", (sid,))
	sidClasses= cur.fetchall()
	classList=[]
	if(sidClasses!=0):
		for i in range(len(sidClasses)):
			temp=sidClasses[i]
			print(temp)
			cur.execute("SELECT * FROM Courses WHERE CourseId=?", (temp[2],))
			a= cur.fetchall()
			print(a)
			classList.append(a)
		return classList
	return None

def validSID(sid):
	cur.execute("SELECT * FROM Students WHERE StudentID=?", (sid,))
	isStudent= cur.fetchall()
	if(len(isStudent)!=0):
		return True
	else:
		return False
	#cur.execute("DELETE FROM Classes WHERE CourseId LIKE '1'")
	# cur.execute('SELECT * FROM Classes')
	# data_6= cur.fetchall()
	# print ("Courses ", data_6)
		
# def createEvalList():
# 	cur.execute('SELECT * FROM Classes')
# 	clid= cur.fetchall()
# 	for i in clid:
# 		tempID=cur.fetchall()[0][0]
		
# 		cur.execute("SELECT * FROM EvalStatus WHERE classID=?", (tempID,))
# 		s= cur.fetchall()
# 		if len(s)==0:
# 			cur.execute("INSERT INTO EvalStatus VALUES (null, ?, ?)", (tempID,0,))
# 		else:
# 			print("Eval Already created")

# 	cur.execute('SELECT * FROM EvalStatus')
# 	data_6= cur.fetchall()
# 	print ("EvalStatus ", data_6)

#main()


#126155353869
#autoformmaker project Id
#AutoFormMaker
#https://script.google.com/macros/s/AKfycbwWYKyWtmedmGCHgh0HU6vZ3A6aB292StRp2QsTt9EKfX_7xYQ/exec
#Deployment ID: AKfycbxx7d7WtpdO3Xn5Ge5OnRYnf16FCf2eU3kKvqK1R8AJOHxcI8THMf2WEI6xaCPszW12
#def incomingResponses():



