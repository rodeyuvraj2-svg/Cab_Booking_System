class Driver:
    def __init__(self,id,name,mobile,email,password,l_num,v_type,v_num):
        self.id = id
        self.name = name
        self.mobile = mobile
        self.email = email
        self.password = password
        self.l_num = l_num
        self.v_type = v_type
        self.v_num = v_num
        self.mode = "offline"

    def struct(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "mobile" : self.mobile,
            "email" : self.email,
            "password" : self.password,
            "l_num" : self.l_num,
            "v_type" : self.v_type,
            "v_num" : self.v_num,
            "mode" : self.mode
        }