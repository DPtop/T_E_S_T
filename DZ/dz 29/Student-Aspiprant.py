class Student:
    def __init__(self, firstName:str='', lastName:str='', group:str='', averageMark:float=0.0):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__group = group
        self.__averageMark = averageMark

    def getScholarship(self):
        if self.__averageMark == 5.0:
            return 2000
        else:
            return 1900


class Aspirant(Student):
    def getScholarship(self):
        if self._Student__averageMark == 5.0:
            return 2500
        else:
            return 2200


stud1 = Student('first-1', 'last-1', 'group-1', 4.5)
stud2 = Student('first-2', 'last-2', 'group-2', 5.0)
stud3 = Student('first-3', 'last-3', 'group-3', 4.9)
aspir1 = Aspirant('1-first', '1-last', 'a1-group', 5.0)
aspir2 = Aspirant('2-first', '2-last', 'a2-group', 4.8)

print('stud1', stud1.getScholarship())
print('stud2', stud2.getScholarship())
print('stud3', stud3.getScholarship())
print('aspir1', aspir1.getScholarship())
print('aspir2', aspir2.getScholarship())

