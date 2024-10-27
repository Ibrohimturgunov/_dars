 class Shaxs:
    def __init__(self, ism, familiya):
        self.is m =ism
        self.familiy a =familiya

class Talaba(Shaxs):
    def __init__(self, ism, familiya):
        super().__init__(ism, familiya)
        self.fanla r =[]

    def fanga_yozil(self, fani):
        self.fanlar.append(fani)

    def remove_fan(self, r_fan):
        if r_fan in self.fanlar:
            self.fanlar.remove(r_fan)
        else:
            print("Siz bu fanga yozilmagansiz")

    def get_info(self):
        fanlar_ruyxati = ', '.join([fan.nomi for fan in self.fanlar]) if self.fanlar else "Hozircha fan yo'q"
        return f"""       
Ismi:           {self.ism}
Familiyasi:     {self.familiya}
Fanlari:        {fanlar_ruyxati}
        """

class Fan:
    def __init__(self, nomi):
        self.nom i =nomi

fan 1 =Fan("Matematika")
fan 2 =Fan("Dasturlash")
fan 3 =Fan("Kimyo")

talaba_ 1 =Talaba("Turgunov" ,"Ibrohim")
talaba_1.fanga_yozil(fan1)
talaba_1.fanga_yozil(fan2)
talaba_1.fanga_yozil(fan3)

talaba_1.remove_fan(fan1)

print(talaba_1.get_info())
