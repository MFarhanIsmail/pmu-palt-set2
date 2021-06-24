#palt python set 2
#question2
#Mohamad farhan bin ismail (20ddt19f1085)
class Converter:
    def __init__(self,weight,unit):
        self.weight = int(weight)
        self.unit = unit

    def kg_to_pound_convert(self):
        kgpound = 2.20462
        total_kgpound = self.weight * kgpound
        print("kg to Pound: " + str(total_kgpound) + "Pound")

    def pound_to_kg_convert(self):
        poundkg = 0.45
        total_poundkg = self.weight * poundkg
        print("pound to kg: " + str(total_poundkg) + "kg")

    def convert_selection(self):
        if self.unit == "kg":
            self.kg_to_pound_convert()
        elif self.unit == "pound":
            self.pound_to_kg_convert()
        else:
            print("please enter the unit (kg/pound) only.")

b = Converter(154.324,"pound")
c = Converter(70,"kg")

b.convert_selection()
c.convert_selection()
