class student:
    marks_bonus=1.5
    total_marks=100
    value=""
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_bonus(self):
        self.marks=int(self.marks*self.marks_bonus)

    def dummy(self,section):
        self.value=self.marks+self.total_marks+section
