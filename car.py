class Car(object):
    def __init__ (self,model, color, company,speed_limit):
        self.color = color
        self.company = company
        self.model = model
        self.speed_limit = speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerating...")
        "accelerater functionality here"

    def change_gear(self,gear_type):
        print("gear changed")
        "gear related functionalities here"

audi = Car("A6", "red", "audi", "120")

print(audi.accelerate())