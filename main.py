class Attraction():
    def __init__(self, name, capacity):
        self._name=name
        self._capacity=capacity
    def get_details(self):
        return(f"Attraction: {self._name}, Capacity: {self._capacity}.")
    def start(self):
        print(" The attraction is starting. ")

class ThrillRide(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)
        self._min_height=min_height

    def start(self):
        return(f"Thrill Ride {self._name} is now starting. Hold on tight!")

    def is_eligible(self,height):
        if height<self._min_height:
            print(f"Sorry you can't ride {self._name}, the minimum height is {self._min_height}.")
            return False

        else:
            print("You meet the height requirment! Yeh! ")
            return True
        
class FamilyRide (Attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)
        self._min_age=min_age

    def start(self):
        return(f"Family Ride {self._name} is now starting. Enjoy the fun!")

    def is_eligible(self, age):
        if age < self._min_age:
            print("Sorry, you don't meet the minimum age requirment. ")
            return False
        else:
            print("Yeh! you meet the minimum age requirment. ")
            return True

class Staff ():
    def __init__(self, name, role):
        self._name= name
        self._role= role
    def work(self):
        print(f"Staff {self._name} is performing their role: {self._role}.")

class Vistor():
    def __init__(self, name, age, height):
        self._name=name
        self._age=age
        self._height=height

    def ride_ThrillRide(self,ThrillRide):
        if ThrillRide.is_eligible(self._height) == True :
            print(ThrillRide.start())


    def ride_FamilyRide(self,FamilyRide):
        if FamilyRide.is_eligible(self._age) == True :
            print(FamilyRide.start())

class Manger(Staff):
    def __init__(self, name, role,team):
        super().__init__(name, role)
        self._team = team

    def add_staff(self,staff):
        self.team.append(staff)

    def get_team_summary(self):
        print(self.team)

Ride1 = ThrillRide("Dragon Coaster",26,160)
Ride2 = FamilyRide("Merry-Go-Round", 44, 5)
Ride3 = ThrillRide("Dinosaur Coaster",8,100)
Ride4 = FamilyRide("Peace ride",7,129)

person1=Vistor("Fathima", 17, 140)


person1.ride_ThrillRide(Ride1)
person1.ride_FamilyRide(Ride2)
person1.ride_ThrillRide(Ride3)
person1.ride_FamilyRide(Ride4)
