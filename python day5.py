class car:
    someclassdummyvar="dummy"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.someclassdummyvar)
carObj= car( )
carObj.sample_car_instance_method("hello agaiin!")
carObj= car( )
carObj.sample_car_instance_method(2)


class carsample:
    dummyvar1 = "dummyvar1"
    dummyvar2 = "dummyvar2"
    def init (self,name,model):
        self.name=name
        self.model=model
    def displaycardetails(self):
        print(self.name)
        print(self.model)
list=[5,4,3,2,1]
print(list[-5:-2:2])

list_A=[1,2,3,4]
list_B=list_A.append(6)
print(list_B)