class Shaxs:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya


class Professor(Shaxs):
    def __init__(self, ism, familiya, unvoni):
        super().__init__(ism, familiya)
        self.unvoni = unvoni

    def get_info(self):
        return f""" 
Ismi:       {self.ism}
Familiyasi: {self.familiya}
Unvoni:     {self.unvoni}
"""


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, paroli):
        super().__init__(ism, familiya)
        self.paroli = paroli

    def get_info(self):
        return f""" 
Ismi:       {self.ism}
Familiyasi: {self.familiya}
Paroli:     {self.paroli}
"""


class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, mahsulot):
        super().__init__(ism, familiya)
        self.mahsulot = mahsulot

    def get_info(self):
        return f""" 
Ismi:       {self.ism}
Familiyasi: {self.familiya}
Mahsuloti:  {self.mahsulot}
"""


class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, paroli):
        super().__init__(ism, familiya, paroli)

    def ban_users(self):
        return f"{self.ism} - foydalanuvchi bloklandi!!!"


admin_1 = Admin("Ibrohim", "turgunov", "54321")
print(admin_1.ban_users())