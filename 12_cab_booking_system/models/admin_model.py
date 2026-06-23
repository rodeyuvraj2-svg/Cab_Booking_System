class Admin:
    def __init__(self,id,name,mobile,email,password):
        self.id = id
        self.name = name
        self.mobile = mobile
        self.email = email
        self.password = password
        

    def struct(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "mobile" : self.mobile,
            "email" : self.email,
            "password" : self.password
        }