
class Box:
    def __init__(self, name, roll, cgpa):
        self.name = name 
        self.roll = roll 
        self.cgpa = cgpa 
        
    def __lt__(self, other):
        # Sorting based on CGPA (Ascending order), in case if there is any tie, 
        # then it sortes based on roll (Ascending order)
        if self.cgpa != other.cgpa:
            return self.cgpa < other.cgpa
        return self.roll < other.roll 
 
def printObjects(objects):
    print("##################")
    for obj in objects:
        print("Name is:", obj.name)
        print("Roll no is:", obj.roll)
        print("CGPA is:", obj.cgpa)
        print() 
    print("##################")
        
        
names = ["kiran", "Arun", "Chandu", "Vinod"]
rollNumbers = [567, 543, 555, 101]
cgpa = [8.9, 6.7, 9.1, 9.1]
objects = []

for index in range(len(names)):
    obj = Box(names[index], rollNumbers[index], cgpa[index])
    objects.append(obj)
    
printObjects(objects)
objects.sort()
#objects = sorted(objects)
printObjects(objects)
