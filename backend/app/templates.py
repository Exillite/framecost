"""



                             W
                   _______________________
                  |  ___________________  |
                  | |   _               | |
                H | |  ( )    (=)       | |         IS_HORISITAL == TRUE
                  | |  ( )    -|-       | |
                  | |___|_____/_\_______| |
                  |_______________________|
                  
"""


class BaseTemplate:
    width: float
    height: float
    is_horisontal: bool


class WithOut_Paspartu(BaseTemplate):
    rama: float
    osnova: float
    zadnik: float
    steklo: float
    natazka: float
    tros: float
    
    def __init__(self, width: float, height: float, is_horisontal: bool, baget_width: float):
        self.is_horisontal = is_horisontal
        self.width = width
        self.height = height
        if self.is_horisontal and self.width < self.height:
            self.width, self.height = self.height, self.width
            
        if not self.is_horisontal and self.width > self.height:
            self.width, self.height = self.height, self.width
            
        self.baget_width = baget_width
        
        self.calculate()

    def calculate(self):
        self.rama = (self.width + 1.5 + self.baget_width*2) * 2 + (self.height + 1.5 + self.baget_width*2) * 2
        self.osnova = (self.width + 2) * (self.height + 2)
        self.zadnik = self.osnova
        self.steklo = (self.width + 4) * (self.height + 4)
        self.natazka = (self.width + self.width) * 2
        self.tros = 20 + self.width
    
    def get_data(self) -> dict:
        return {
            "rama": self.rama,
            "osnova": self.osnova,
            "zadnik": self.zadnik,
            "steklo": self.steklo,
            "natazka": self.natazka,
            "tros": self.tros,
        }


class With_Paspartu(BaseTemplate):
    rama: float
    paspartu: float
    pricleyca: float
    dvoynoe: float
    troynoe: float
    osnova: float
    zadnik: float
    steklo: float
    natazka: float
    tros: float
    
    def __init__(self, width: float, height: float, is_horisontal: bool, baget_width: float, paspartu_width: float):
        self.is_horisontal = is_horisontal
        self.width = width
        self.height = height
        if self.is_horisontal and self.width < self.height:
            self.width, self.height = self.height, self.width
            
        if not self.is_horisontal and self.width > self.height:
            self.width, self.height = self.height, self.width
            
        self.baget_width = baget_width
        self.paspartu_width = paspartu_width
        
        self.calculate()
        
    def calculate(self):
        self.rama = (self.width + 2 + self.paspartu_width * 2 + self.baget_width) * 2 + (self.height + 2 + self.paspartu_width * 2 + self.baget_width) * 2
        self.paspartu = (self.width +  2 + (self.paspartu_width * 2)) * (self.height + 2 + (self.paspartu_width * 2))
        self.pricleyca = ((self.width + 2) + (self.height + 2)) * 2
        self.dvoynoe = ((self.width + 2) + (self.height + 2)) * 2
        self.troynoe =  ((self.width + 2) + (self.height + 2)) * 2 + ((self.width + 3) + (self.height + 3) * 2)
        self.osnova = (self.width + 2) * (self.height + 2)
        self.zadnik = self.paspartu
        self.steklo = (self.width + 4 + self.paspartu_width * 2) * (self.height + 4 + self.paspartu_width * 2)
        self.natazka = (self.width + self.width) * 2
        self.tros = 20 + self.width + self.paspartu_width * 2

    def get_data(self) -> dict:
        return {
            "rama": self.rama,
            "paspartu": self.paspartu,
            "pricleyca": self.pricleyca,
            "dvoynoe": self.dvoynoe,
            "troynoe": self.troynoe,
            "osnova": self.osnova,
            "zadnik": self.zadnik,
            "steklo": self.steklo,
            "natazka": self.natazka,
            "tros": self.tros,
        }


class Rama_With_Cant(BaseTemplate):
    rama: float
    osnova: float
    zadnik: float
    steklo: float
    natazka: float
    cant: float
    tros: float
    
    def __init__(self, width: float, height: float, is_horisontal: bool, baget_width: float):
        self.is_horisontal = is_horisontal
        self.width = width
        self.height = height
        if self.is_horisontal and self.width < self.height:
            self.width, self.height = self.height, self.width
            
        if not self.is_horisontal and self.width > self.height:
            self.width, self.height = self.height, self.width
            
        self.baget_width = baget_width
        
        self.calculate()
        
    def calculate(self):
        self.rama = ((self.width + 1 + 3.6 + self.baget_width * 2) + (self.height + 1 + 3.6 + self.baget_width * 2)) * 2
        self.osnova = (self.width + 2) * (self.height + 2)
        self.zadnik = (self.width + 2 + 4 + 4) * (self.height + 2 + 4 + 4)
        self.steklo = (self.width + 2 + 3.6) * (self.height + 2 + 3.6)
        self.natazka = (self.width + self.width) * 2
        self.cant = (self.width + 3 + 3.6 + self.height + 3 + 3.6) * 2
        self.tros = 20 + self.width + 4 * 2
        
    def get_data(self) -> dict:
        return {
            "rama": self.rama,
            "osnova": self.osnova,
            "zadnik": self.zadnik,
            "steklo": self.steklo,
            "natazka": self.natazka,
            "cant": self.cant,
            "tros": self.tros,
        }


class Double_Rama(BaseTemplate):
    rama1: float
    rama2: float
    osnova: float
    zadnik: float
    steklo: float
    natazka: float
    tros: float

    def __init__(self, width: float, height: float, is_horisontal: bool, baget1_width: float, baget2_width: float):
        self.is_horisontal = is_horisontal
        self.width = width
        self.height = height
        if self.is_horisontal and self.width < self.height:
            self.width, self.height = self.height, self.width
            
        if not self.is_horisontal and self.width > self.height:
            self.width, self.height = self.height, self.width
            
        self.baget1_width = baget1_width
        self.baget2_width = baget2_width
        
        self.calculate()
        
    def calculate(self):
        self.rama1 = ((self.width + 1.5 + self.baget1_width * 2) + (self.height + 1.5 + self.baget1_width * 2)) * 2
        self.rama2 = (self.width + 1 + self.baget1_width * 2 + self.baget2_width * 2 + self.height + 1 + self.baget1_width * 2 + self.baget2_width * 2) * 2
        self.osnova = (self.width + 2) * (self.height + 2)
        self.zadnik = (self.width + 2 + self.baget1_width + self.baget1_width + 3) * (self.height + 2 + self.baget1_width + self.baget1_width + 3)
        self.steklo = (self.width + 4 + self.baget1_width * 2) * (self.height + 4 + self.baget1_width * 2)
        self.natazka = (self.width + self.width) * 2
        self.tros = 20 + self.width + self.baget1_width * 2

    def get_data(self) -> dict:
        return {
            "rama1": self.rama1, 
            "rama2": self.rama2, 
            "osnova": self.osnova, 
            "zadnik": self.zadnik, 
            "steklo": self.steklo, 
            "natazka": self.natazka, 
            "tros": self.tros, 
        }


class Rama_With_Natazka_Na_Podramnik(BaseTemplate):
    rama: float
    podramnic: float
    podramnic60: float
    tros: float
    steklo: float
    less_storona: float
    
    def __init__(self, width: float, height: float, is_horisontal: bool, baget_width: float):
        self.is_horisontal = is_horisontal
        self.width = width
        self.height = height
        if self.is_horisontal and self.width < self.height:
            self.width, self.height = self.height, self.width
            
        if not self.is_horisontal and self.width > self.height:
            self.width, self.height = self.height, self.width
            
        self.baget_width = baget_width
        self.less_storona = min(self.width, self.height)
        
        self.calculate()
        
    def calculate(self):
        self.rama = ((self.width + 1.5 + self.baget_width * 2) + (self.height + 1.5 + self.baget_width * 2)) * 2
        self.podramnic = (self.width + 2 + self.height + 2) * 2
        self.podramnic60 = (self.width + 2 + self.height + 2) * 2 + self.less_storona
        self.tros = 20 + self.width
        self.steklo = (self.width + 4) * (self.height + 4)

    def get_data(self) -> dict:
        return {
            "rama": self.rama,
            "podramnic": self.podramnic,
            "podramnic60": self.podramnic60,
            "tros": self.tros,
            "steklo": self.steklo, 
        }


class Double_Rama_With_Paspartu(BaseTemplate):
    rama1: float
    rama2: float
    paspartu: float
    nakleyka: float
    dvoynoe: float
    troynoe: float
    osnova: float
    zadnik: float
    steklo: float
    natazka: float
    tros: float
    
    def __init__(self, width: float, height: float, is_horisontal: bool, baget1_width: float, baget2_width: float, paspartu_width: float):
        self.is_horisontal = is_horisontal
        self.width = width
        self.height = height
        if self.is_horisontal and self.width < self.height:
            self.width, self.height = self.height, self.width
            
        if not self.is_horisontal and self.width > self.height:
            self.width, self.height = self.height, self.width
            
        self.baget1_width = baget1_width
        self.baget2_width = baget2_width
        
        self.paspartu_width = paspartu_width
        
        self.calculate()
        
    def calculate(self):
        self.rama1 = ((self.width + 1.5 + self.baget1_width * 2 + self.paspartu_width * 2) + (self.height + 1.5 + self.baget1_width * 2 + self.paspartu_width * 2)) * 2
        self.rama2 = (self.width + 4 + self.paspartu_width * 2 + self.baget1_width * 2 + self.baget2_width * 2) * 2 + (self.height + 4 + self.paspartu_width * 2 + self.baget1_width * 2 + self.baget2_width * 2) * 2
        self.paspartu = (self.width + 2 + self.paspartu_width * 2) * (self.height + 2 + self.paspartu_width * 2)
        self.nakleyka = ((self.width + 2) + (self.height + 2)) * 2
        self.dvoynoe = ((self.width + 2) + (self.height + 2)) * 2
        self.troynoe = ((self.width + 2) + (self.height + 2)) * 2 + ((self.width + 3) + (self.height + 3))
        self.osnova = (self.width + 2) * (self.height + 2)
        self.zadnik = (self.width + 2 + self.paspartu_width + self.paspartu_width + self.baget1_width + self.baget1_width + 3) * (self.height + 2 + self.paspartu_width + self.paspartu_width + self.baget1_width + self.baget1_width + 3)
        self.steklo = (self.width + 4 + self.paspartu_width * 2 + self.baget1_width * 2) * (self.height + 4 + self.paspartu_width * 2 + self.baget1_width * 2)
        self.natazka = (self.width + self.height) * 2
        self.tros = 20 + self.width + self.paspartu_width * 2 + self.baget1_width * 2

    def get_data(self) -> dict:
        return {
            "rama1": self.rama1,
            "rama2": self.rama2,
            "paspartu": self.paspartu,
            "nakleyka": self.nakleyka,
            "dvoynoe": self.dvoynoe,
            "troynoe": self.troynoe,
            "osnova": self.osnova,
            "zadnik": self.zadnik,
            "steklo": self.steklo,
            "natazka": self.natazka,
            "tros": self.tros,
        }


class Rama_With_Cant_And_Single_Paspartu(BaseTemplate):
    rama: float
    papartu: float
    prikleyka: float
    cant: float
    osnova: float
    zadnik: float
    steklo: float
    natazka: float
    tros: float
    
    def __init__(self, width: float, height: float, is_horisontal: bool, baget_width: float, paspartu_width: float):
        self.is_horisontal = is_horisontal
        self.width = width
        self.height = height
        if self.is_horisontal and self.width < self.height:
            self.width, self.height = self.height, self.width
            
        if not self.is_horisontal and self.width > self.height:
            self.width, self.height = self.height, self.width
            
        self.baget_width = baget_width
        self.paspartu_width = paspartu_width
        
        self.calculate()
    
    def calculate(self):
        self.rama = ((self.width + 1.5) + (self.baget_width * 2) + (self.paspartu_width * 2)) * 2 + ((self.height + 1.5) + (self.baget_width * 2) + (self.paspartu_width)) * 2
        self.papartu = (self.width + 2 + self.paspartu_width * 2) * (self.height + 2 + self.paspartu_width * 2)
        self.prikleyka = ((self.width + 2) + (self.height + 2)) * 2
        self.cant = (self.width + 3) * 2 + (self.height + 3) * 2
        self.osnova = (self.width + 2) * (self.height + 2)
        self.zadnik = (self.width + 1 + 2 + self.paspartu_width + self.paspartu_width + 3) * (self.height + 1 + 2 + self.paspartu_width + self.paspartu_width + 3)
        self.steklo = (self.width + 4 + self.paspartu_width * 2 + self.baget_width * 2) * (self.height + 4 + self.paspartu_width * 2 + self.baget_width * 2)
        self.natazka = (self.width + self.height) * 2
        self.tros = 20 + self.width + self.paspartu_width * 2 + self.baget_width * 2

    def get_data(self) -> dict:
        return {
            "rama": self.rama,
            "papartu": self.papartu,
            "prikleyka": self.prikleyka,
            "cant": self.cant,
            "osnova": self.osnova,
            "zadnik": self.zadnik,
            "steklo": self.steklo,
            "natazka": self.natazka,
            "tros": self.tros,
        }


class Rama_With_Cant_And_Double_Paspartu(BaseTemplate):
    rama: float
    paspartu: float
    pricleyka: float
    dvoynoe: float
    cant: float
    osnova: float
    zadnik: float
    steklo: float
    natazka: float
    tros: float
    
    def __init__(self, width: float, height: float, is_horisontal: bool, baget_width: float, paspartu_width: float):
        self.is_horisontal = is_horisontal
        self.width = width
        self.height = height
        if self.is_horisontal and self.width < self.height:
            self.width, self.height = self.height, self.width
            
        if not self.is_horisontal and self.width > self.height:
            self.width, self.height = self.height, self.width
            
        self.baget_width = baget_width
        self.paspartu_width = paspartu_width
        
        self.calculate()

    def calculate(self):
        self.rama = (self.width + 1.5 + self.baget_width * 2 + self.paspartu_width * 2) * 2 + (self.height + 1.5 + self.baget_width * 2 + self.paspartu_width * 2) * 2
        self.paspartu = (self.width + 2 + self.paspartu_width * 2) * (self.height + 2 + self.paspartu_width * 2)
        self.pricleyka = ((self.width + 3) + (self.height + 3)) * 2
        self.dvoynoe = ((self.width + 3) + (self.height + 3)) * 2
        self.cant = (self.width + 5) * 2 + (self.height + 5) * 2
        self.osnova = (self.width + 2) * (self.height + 2)
        self.zadnik = (self.width + 2 + self.paspartu_width * 2 + self.baget_width * 2) * (self.height + 2 +  self.paspartu_width * 2 + self.baget_width * 2)
        self.steklo = (self.width + 4 + self.paspartu_width * 2) * (self.height + 4 + self.paspartu_width * 2)
        self.natazka = (self.width + self.height) * 2
        self.tros = 20 + self.width + self.paspartu_width * 2 + 3

    def get_data(self) -> dict:
        return {
            "rama": self.rama,
            "paspartu": self.paspartu,
            "pricleyka": self.pricleyka,
            "dvoynoe": self.dvoynoe,
            "cant": self.cant,
            "osnova": self.osnova,
            "zadnik": self.zadnik,
            "steklo": self.steklo,
            "natazka": self.natazka,
            "tros": self.tros,
        }


class Volume_Dezigne(BaseTemplate):
    rama: float
    osnova: float
    zadnik: float
    paspar_baget: float
    paspar_osnova: float
    paspar_obshee: float
    steklo: float
    natazka: float
    tros: float
    rabota: float
    
    def __init__(self, width: float, height: float, is_horisontal: bool, baget_width: float, baget_height: float):
        self.is_horisontal = is_horisontal
        self.width = width
        self.height = height
        if self.is_horisontal and self.width < self.height:
            self.width, self.height = self.height, self.width
            
        if not self.is_horisontal and self.width > self.height:
            self.width, self.height = self.height, self.width
            
        self.baget_width = baget_width
        self.baget_height = baget_height
        
        self.calculate()

    def calculate(self):
        self.rama = (self.width + 1,5 + self.baget_width * 2) * 2 + (self.height + 1,5 + self.baget_width * 2) * 2
        self.osnova = (self.width + 2) * (self.height + 2)
        self.zadnik = ((self.width * 4) * 2 + (self.height * self.baget_height) * 2) * 2 + self.osnova
        self.paspar_baget = (self.width * self.baget_height) * 2 + (self.height * self.baget_height) * 2
        self.paspar_osnova = (self.width + 2) * (self.height + 2)
        self.paspar_obshee = self.paspar_baget + self.paspar_osnova
        self.steklo = (self.width + 2) * (self.height + 2)
        self.natazka = (self.width + self.height) * 2
        self.tros = 20 + self.width
        self.rabota = self.width * 2 + self.height * 2

    def get_data(self) -> dict:
        return {
            "rama": self.rama,
            "osnova": self.osnova,
            "zadnik": self.zadnik,
            "paspar_baget": self.paspar_baget,
            "paspar_osnova": self.paspar_osnova,
            "paspar_obshee": self.paspar_obshee,
            "steklo": self.steklo,
            "natazka": self.natazka,
            "tros": self.tros,
            "rabota": self.rabota,
        }


class Volume_Dezigne_With_Paspartu(BaseException):
    rama: float
    osnova: float
    zadnik: float
    paspar_baget: float
    paspartu_okno: float
    paspartu_osnova: float
    paspar_osnova_bokov: float
    steklo: float
    natazka: float
    dvoynoe_paspartu: float
    troynoe_pasprtu: float
    tros: float
    rabota: float
    
    def __init__(self, width: float, height: float, is_horisontal: bool, baget_width: float, baget_height: float, paspartu_width: float):
        self.is_horisontal = is_horisontal
        self.width = width
        self.height = height
        if self.is_horisontal and self.width < self.height:
            self.width, self.height = self.height, self.width
            
        if not self.is_horisontal and self.width > self.height:
            self.width, self.height = self.height, self.width
            
        self.baget_width = baget_width
        self.baget_height = baget_height
        self.paspartu_width = paspartu_width
        
        self.calculate()

    def calculate(self):
        self.rama = (self.width + 1,5 + self.paspartu_width * 2 + self.baget_width * 2) * 2 + (self.height + 1,5 + self.paspartu_width * 2 + self.baget_width * 2) * 2
        self.osnova = (self.width + 2) * (self.height + 2)
        self.zadnik = (((self.width + 1,5) * self.baget_height) * 2 + ((self.height + 1,5) * self.baget_height) * 2) * 2 + ((self.width + 1,5 + self.paspartu_width * 2) * (self.height + 1,5 + self.paspartu_width * 2))
        self.paspar_baget = ((self.width + 1,5) * self.baget_height) * 2 + ((self.height + 1,5) * self.baget_height) * 2
        self.paspartu_okno = ((self.width + 2) + self.paspartu_width * 2) * ((self.height + 2) + self.paspartu_width * 2)
        self.paspartu_osnova = ((self.width + 2) + self.paspartu_width * 2) * ((self.height + 2) + self.paspartu_width * 2)
        self.paspar_osnova_bokov = self.paspar_baget + self.paspartu_osnova
        self.steklo = (self.width + 4 + self.paspartu_width * 2) * (self.height + 4 + self.paspartu_width * 2)
        self.natazka = (self.width + self.height) * 2
        self.dvoynoe_paspartu = ((self.width + 4) + (self.height + 4)) * 2
        self.troynoe_pasprtu = self.dvoynoe_paspartu * 2
        self.tros = self.width + self.paspartu_width * 2 + 20
        self.rabota = (self.width + self.paspartu_width * 2) * 2 + (self.height + self.paspartu_width * 2) * 2

    def get_data(self) -> dict:
        return {
            "rama": self.rama,
            "osnova": self.osnova,
            "zadnik": self.zadnik,
            "paspar_baget": self.paspar_baget,
            "paspartu_okno": self.paspartu_okno,
            "paspartu_osnova": self.paspartu_osnova,
            "paspar_osnova_bokov": self.paspar_osnova_bokov,
            "steklo": self.steklo,
            "natazka": self.natazka,
            "dvoynoe_paspartu": self.dvoynoe_paspartu,
            "troynoe_pasprtu": self.troynoe_pasprtu,
            "tros": self.tros,
            "rabota": self.rabota,
        }
