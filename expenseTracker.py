# Python 101

# Project Title: Personal Finance Tracker
# Project Description:
import json
import keyboard
from createUser import  create_New_User
from functions import add_income, add_expense, view_statement, generate_report

from datetime import datetime




# Open and read the JSON file


class App :
    
        currUser=''
        data=''
    
        def __init__(self) :
           self.data= self.loadData()
           self.print_statement()
           print(self.data)
           
           
        def loadData (self):
            try:

                with open('./data.json', 'r') as input_file:
                    data = json.load(input_file)
                    print("Data successfully")
                    return data
            
            except FileNotFoundError :
                print("The file does not exist.Check directory")
                exit()
            except json.JSONDecodeError:
                print("Error decoding JSON from the file.")
                exit()
            except Exception as e:
                print(f"An error occurred: {e}")
                exit()
        


   
         

        def logout(self):
            print("Logging out...")
            self.currUser=''
            self.print_statement()
      
        
        def print_statement(self):
    
            data = self.data
            print("welcome to PowerLearn Expense Tracker. Kindly enter Your userName")
            print(f"Current Date : {datetime.now().ctime()}" )  
            userName = (input("User Name :")).strip()
            
            findUser = self.find_user(self.data,userName)
            
            if(len(findUser)>0):
                #user found, run the program
                self.currUser = userName
                self.services()
                
              
                
            else:
               
              
                #user not found, Try again ,Create User or Quit
                res = input(f"{userName}:Not Found .\nPress Y to create a new account.\nPress N to try again \nPress ESC to Quit \n Y/N/ESC ") 
                if(res =="y" or res == "Y"):
                    #create new Account
                    print('Creating new Account')
                    create_New_User(userName,self.data)
                    self.print_statement()
                    
                
                elif (res=="n" or res =="N"):
                    
                    print("Trying Again") 
                    self.print_statement()  
                 
                else:
                    exit()
     
        def find_user(self,users_list,userName):

            return [user for user in users_list if user['user'].lower().strip() == userName.lower().strip()]
           
    
        def services(self):
            print(f"Hello  again, {self.currUser}.  Select the following options")
            choice = int(input("\n1: Add income\n2: Add Expense\n3: View Statement\n4: Generate Report \n5:Logout\n6: Quit \n:"))
            
            self.serviceChoice(choice)
            
            c = input("Would you like to perform any other action? Y/N")
            if(c=="Y" or c=="y"):
              self.services() 
            
            else:
                print('See you later!') 
                exit()  
            
            
        
        def serviceChoice(self,value):
            print(value)
            match value:
                case 1:
                    return add_income(self.currUser,self.data)
                case 2:
                        return add_expense(self.currUser,self.data)
                case 3:
                     return view_statement(self.currUser,self.data)
                case 4:
                     return generate_report(self.currUser,self.data)
                case 5:
                     return self.logout()
                case 6:
                     exit()
                case _:
                         print("Invalid Option")
                         self.services()


            
            # print("1:  \n2: Add Expense \n3:  \n4: Generate Report \n")

            


app = App()


print(app)



# Step 8: Categories and Reports

# Allow the user to categorize expenses and generate reports based on categories, monthly summaries, or custom date ranges. Implement functions to calculate and display these reports.
# Step 9: Data Visualization (Optional)

# Use external libraries such as Matplotlib or Plotly to create graphical representations of financial data. Generate charts or graphs to visualize income, expenses, and savings over time.
# Step 10: Error Handling and Validation

# Implement error handling and validation mechanisms to handle incorrect inputs or invalid operations. Provide appropriate error messages and guide the user to enter the correct information.
# Step 11: Test and Refine

# Test the finance tracker by adding various transactions, checking reports, and ensuring the calculations are accurate. Refine the code based on user feedback and testing results.
# Step 12: Conclusion

# Print a closing message and thank the user for using the personal finance tracker.
# BONUS: JSON Introduction


# JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is widely used for data serialization and communication between web services and clients.



# JSON Syntax:

# JSON data is represented in key-value pairs.
# Data is enclosed in curly braces {} and organized into multiple key-value pairs.
# Each key is a string enclosed in double quotes, followed by a colon :, and the corresponding value.
# Values can be strings, numbers, booleans, arrays, or nested objects.
# Arrays are enclosed in square brackets [] and can contain multiple values separated by commas.
# Nested objects are objects within objects, represented as key-value pairs within curly braces.