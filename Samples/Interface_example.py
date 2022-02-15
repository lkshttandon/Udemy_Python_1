from Vehicle_Interface import Vehicle


class Audi(Vehicle):
    def __init__(self, accessories, make, model, year):
        super(Audi, self).__init__(make, model, year)
        self.accessories = accessories

    def start(self): return "Audi Started"

    def stop(self): return "Audi Stopped"


v1 = Audi(['PowerBrake','V12'],'R8', '2020X', '2020')
print([x for x in v1.accessories],v1.start(),v1.stop())
