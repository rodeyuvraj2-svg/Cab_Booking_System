class Location:
    def __init__(self,id,place,c_id):
        self.id = id
        self.place = place
        self.c_id = c_id

    def struct(self):
        return{
            "id" : self.id,
            "place" : self.place,
            "c_id" : self.c_id
        }