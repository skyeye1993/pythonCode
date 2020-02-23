class Student(object):
    score = 0
    passline = 60

    def __init__(self, score):
        self.score = score

    def setscore(self, score):
        self.score = score

    def getscore(self):
        return self.score

    @staticmethod
    def cmp(s1, s2):
        return s1.getscore() >= s2.getscore()

    @classmethod
    def ispas(cls, obj):
        return obj.getscore() >= cls.passline


s1 = Student(80)
s2 = Student(90)
print(s1.getscore())
print(Student.cmp(s1, s2))
print(Student.ispas(s1))
