import json

from functions import updateInfo,checkAvailability
# from expenseTracker import loadData

# Open and read the JSON file
# data = loadData('./data.json')



class create_New_User :
    def __init__(self, user,data) :
        self.user = user
        self.data = data
        # self.welcome_new_User()
        self.addUser(self.data)
   
        
    def welcome_new_User(self) :
        print(f"Welcome {self.user}")
        
    def addUser(self,data):
        
        if(checkAvailability(self.user,data)) :
            print("User already exists")
            
        else:
            occupation = input(f"What is your occupation, {self.user}")
            data.append({'user': self.user, 'expenses': [], 'occupation':occupation, 'income': []})
            updateInfo(data)
                
            
      
        
        
      
           
    

        