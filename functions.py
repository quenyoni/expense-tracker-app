import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from tabulate import tabulate
from prettytable import PrettyTable as pt



# def loadData():
#     null = None 
#     with open('data.json') as f:
#         data = json.load(f)
#         return data


# data = loadData()
  
  

def report_viz(value,userName,data):
    # 1: Income Pie Chart 
    # \n2:Expense Pie Chart 
    # \n3:Expense/Income Graph")
    match value:
        case 1:
            return displayPie("income",userName,data)
        case 2:
            return displayPie("expense",userName,data)
              
        case 3:
            return expense_incomegraph(userName,data)
              
        case _:
             print("Invalid Option")
             

def displayPie(typ,userName,data):

    ypoints=[]    
    xpoints = [] 
    labels=[]
 
    
    for user in data:
            if user['user'].lower() == userName.lower():
                income = user["income"]
                expense = user["expenses"]
    
    
    if(typ == "income"):
             for i in income:
                    xpoints.append(i["time"])
                    ypoints.append(i["value"]) 
                    labels.append(i["ref"])  
    elif(typ == "expense"):
            for e in expense:
                    xpoints.append(e["time"])
                    ypoints.append(abs(e["value"]))
                    labels.append(e["ref"])  


   
    plt.pie(ypoints, labels=labels,startangle = 90,autopct='%1.2f%%')
    plt.show()  
    
    print("Close Report Window to proceed")
    


def  expense_incomegraph(userName,data) :
    ypointsI=[]
    ypointsE=[]
    xpointsI=[]
    xpointsE=[]
    labels=[]
    
    for user in data:
            if user['user'].lower() == userName.lower():
                income = user["income"]
                expense = user["expenses"]
    
    
   
                for i in income:
                    xpointsI.append(i["time"])
                    ypointsI.append(i["value"]) 
                    labels.append(i["ref"])  
 
                for e in expense:
                    xpointsE.append(e["time"])
                    ypointsE.append(abs(e["value"]))

    plt.title("Income/Expense Graph")
  
    plt.legend(labels=['CS','IT','E&TC'])
    plt.bar(xpointsE, ypointsE, width = 0.1)
    plt.bar(xpointsI, ypointsI, width = 0.1)
    plt.grid()
    plt.show()                    
                    
                   
    
    
                   
        
        
        
    
    
   
    
    
               
            
            
def checkAvailability(userName,data):
            for user in data:
                if user["user"].lower() == userName.lower():
                    return True
            return False      

def add_income(userName,data):
 
    income = float(input("How much income would you like to add?\n"))
    ref= input("Source of funds: ")
    for user in data:
        if user['user'].lower() == userName.lower():
             currTime = f"{datetime.now().isoformat()} " 
             user["income"].append({"ref":ref,"value":income, "time":currTime, })   
    i= "{:0,.2f}".format(float(income))
    print(f"{userName} you have added ${i} to your income")
    updateInfo(data)
    
 
def add_expense(userName,data):
    userName = userName
    expense = float(input("How much did you use?"))
    ref = input("What did you use if for?\n")
    
    if(expense <= 0 or len(ref)<3):
        print("let's try again")
        add_expense(userName)
    
    else:
        for user in data:
            if user['user'].lower() == userName.lower():
                     currTime = f"{datetime.now().isoformat()} " 
                     user["expenses"].append({"ref":ref ,"value":-expense ,"time":currTime})   
    ex= "{:0,.2f}".format(float(expense))        
    print(f"{userName} you have added an expense of   -${ex} for {ref} ")
    updateInfo(data)
        
def view_statement(userName,data):
    
    for user in data:
            if user['user'].lower() == userName.lower():
                transactions = user["expenses"] + user['income']
                
                myTable =  pt(["Reference","Type","Date","Value($)"])
                # f"{value:.2f}"
                for t in transactions:
                    typ  = "Expense" if t["value"] < 0 else "Income"
                    myTable.add_row([t["ref"].capitalize(),typ , t["time"],"{:0,.2f}".format(t["value"])])
                myTable.add_row(["-------","---------","------------------","------------------"])
                myTable.add_row(["Current Savings","","","{:0,.2f}".format(calculate_savings(userName,data))])
                print(myTable)
                
                
#for ddata persistence and updating the json file             
def updateInfo(data):
    #  users.append({'user':self.user,'userId':self.userId,"trans":[],"job":None,"salary":None })    
         with open('./data.json', 'w') as output_file:
             json.dump(data, output_file, indent=4)        
                       
def calculate_savings(userName,data):
    
    totalIncome = 0
    expenses = 0
    
    for user in data:
            if user['user'].lower() == userName.lower():
                income = user["income"]
                expense = user["expenses"]
                
                for e in expense:
                    expenses += e["value"]
                
                for i in income:
                   totalIncome += i["value"]
    
    return totalIncome + expenses          
    

def generate_report(userName,data) :
    
    
    
    choice = int(input("Which report would you like \n1: Income Pie Chart \n2:Expense Pie Chart \n3:Expense/Income Graph"))
    report_viz(choice,userName,data)  
    
    
    

   

