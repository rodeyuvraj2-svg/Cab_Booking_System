class Ride:
    def __init__(self,id,pickup,drop,customers_id,status,v_type,fair):
        self.id = id
        self.pickup = pickup
        self.drop = drop
        self.customers_id = customers_id
        self.status = status
        self.v_type = v_type
        self.fair = fair
        self.distance = 0
        self.driver = None

    def struct(self):
        return{
            "id" : self.id,
            "pickup" : self.pickup,
            "drop" : self.drop,
            "customers_id" : self.customers_id,
            "status" : self.status,
            "v_type" : self.v_type,
            "fair" : self.fair,
            "distance" : self.distance,
            "driver" : self.driver
        }