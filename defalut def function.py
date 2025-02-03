class school():
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def bb(self):
        self.name=input("enter the name")
        self.mark=int(input("enter the mark"))
    def cc(self):
        print(self.name,self.mark)
class student(school):
    def apple(self):
        print("ello")
obj=student('','')
obj.bb()
obj.cc()
obj.apple()
    
