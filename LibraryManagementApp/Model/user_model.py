#import database

class User:
    def __init__(self, user_id=None, name=None, username=None, email=None, password=None, date_of_birth=None, role="user", status="Activated"):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.date_of_birth = date_of_birth
        self.role = role
        self.status = status
        #self.db = Database() #Conncet khi có db
    def save(self):
        pass
    def login(email, password):
        pass
    def change_pass():
        pass
    def edit_account_info():
        pass
    



        