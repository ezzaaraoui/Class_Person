from abc import ABCMeta,abstractmethod

class Person(metaclass = ABCMeta):
    pCount = 0
    def __init__(self,ID = 1, fname = "M", lname = "A", age = 22):
        self._id = ID
        self._fname = fname
        self._lname = lname
        self._age = age
        Person.pCount = Person.pCount + 1

    # def __init__(self,old):
    #     self._id = old._id
    #     self._fname = old._fname
    #     self._lname = old._lname
    #     self._age = old._age
    #     Person.pCount = Person.pCount + 1

    @property
    def getId(self):
        return self._ID 
    
    def setID(self,id):
        self._id = id
    
    @property
    def getFname(self):
        return self._fname
    
    def setFname(self,Fname):
        self._fname = Fname
    
    @property
    def getLname(self):
        return self._lname
    def setLname(self,Lname):
        self._lname = Lname
    
    @property
    def getId(self):
        return self._id
    def setID(self,id):
        self._id = id
    
    @abstractmethod
    def toString():
        pass
    
    @abstractmethod
    def equals():
        pass

class Emp(Person):
    eCount = 0
    def __init__(self, ID = 1, fname = "M", lname = "A", age = 22, grade = "mid"):
        super().__init__(ID, fname, lname, age)
        Emp.eCount = Emp.eCount + 1

        self.grade = grade

    # def __init__(self,old):
    #     self._id = old._id
    #     self._fname = old._fname
    #     self._lname = old._lname
    #     self._age = old._age
    #     self.grade = old.grade

    #     Emp.eCount = Emp.eCount + 1


    @property
    def getGrade(self):
        return self.grade
    
    def setGrade(self,grade):
        self.grade = grade

    def toString(self):
        return str(self._id) + self._fname + self._lname + str(self._age) + self.grade
    
    def equals(self,emp):
        if self._id == emp._id :
            return True
        else:
            return False

class Student(Person):
    sCount = 0
    def __init__(self, ID = 1, fname = "M", lname = "A", age = 22, level ="A", note = 20):
        super().__init__(ID, fname, lname, age)
        Student.sCount = Student.sCount + 1
        self.level = level
        self.note = note

    # def __init__(self,old):
    #     self._id = old._id
    #     self._fname = old._fname
    #     self._lname = old._lname
    #     self._age = old._age
    #     self.level = old.level
    #     Student.sCount = Student.sCount + 1


    @property
    def getNote(self):
        return self.note
    def setNote(self,note):
        self.note = note

    @property
    def getLevel(self):
        return self.level
    def setLevel(self,level):
        self.level = level

    def toString(self):
        return str(self._id) + self._fname + self._lname + str(self._age) + self.level + str(self.note)
    
    def equals(self,emp):
        if self._id == emp._id :
            return True
        else:
            return False
        
e1 = Emp()
e2 = Emp()
# e3 = Emp(e2)

s1 = Student()
s2 = Student()
#s3 = Student(s2)


print(e1.toString())
print(e2.toString())
# print(s3.toString())

if(e1.equals(e2)):
    print("equals")
else:
    print("not equals")


print(s1.toString())
print(s2.toString())
if(e1.equals(e2)):
    print("equals")
else:
    print("not equals")


print(Emp.eCount,"employer declared")
print(Person.pCount,"person declared")
print(Student.sCount,"students declared")
