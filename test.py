import json, os
from salesman import *

dirPath = os.path.dirname(os.path.realpath(__file__))
dirPath = dirPath + '/salesman.json'

rawData = open(dirPath)
data = json.load(rawData)
rawData.close()


def funcInput():
    number = input("Enter a Salesman Number: ")
    return number


def funcSearch(number):
    for i in data:
        if(i['Number'] == number):
            return True
        else:
            print("Salesman Number not found")
            print("Please input another number", end='\n\n')
            return False


def funcEdit(number):
    for i in data:
        if(i["Number"] == number):
            name = input("Enter another Name: ")
            q1 = int(input("Enter Q1 sales: "))
            q2 = int(input("Enter Q2 sales: "))
            q3 = int(input("Enter Q3 sales: "))
            q4 = int(input("Enter Q4 sales: "))
            placeholder = {"Name":name, "Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4}
            i.update(placeholder)   
    return data
   

while True:
    number = funcInput()
    if(funcSearch(number) == True):
        updatedData = funcEdit(number)
        updatedData = funcComputeTotal(updatedData)
        updatedData = funcComputeCommission(updatedData)
        funcWriteToFile(updatedData, dirPath)
        print("Process done...")
        break
