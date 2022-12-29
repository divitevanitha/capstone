class Public_Sample_AccessModifier:
    def __init__(self,course,duration):
        self.course=course
        self.duration=duration
    def display_public_class_method(self):
        print("couse:{} - duration:{}".format(self.course,self.duration))
public