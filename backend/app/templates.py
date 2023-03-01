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
