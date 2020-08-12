class design:
    def topDesign(self):
        print("--------------------------")
        print(".... Find Square Area ....")
        print("--------------------------")

class dataAndOperations:
    def lenWid(self):
        self.wid
        self.len

    def getInputs(self):
        self.wid=input("Enter width in feet :")
        self.len=input("Enter length in feet :")
        self.convertLen=int(self.len)
        self.convertWid=int(self.wid)


    def formula(self):
        self.f=self.convertLen * self.convertWid
        print("The square area is :"+str(self.f)+" sq ft")


class view(dataAndOperations):
    def getResult(self):
        self.getInputs()
        self.formula()



designOb=design()
designOb.topDesign()

viewOb=view()
viewOb.getResult()
