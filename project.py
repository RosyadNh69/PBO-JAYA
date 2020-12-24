class karyawan():
    def __init__(self, nama, jenis, bonus, potongan):
        self.nama = nama
        self.jenis = jenis
        self.bonus = bonus
        self.potongan = potongan
    
    def getPekerjaan(self):
        if self.jenis == 'Manager':
            return (8000000)
        elif self.jenis == 'Divisi':
            return (6000000)
        elif self.jenis == 'Karyawan':
            return (4000000)
        elif self.jenis == 'cleaning':
            return (2000000)
        return self.jenis
    
    def Bonus(self):
        y = 2000000
        for q in range (0,11):
            if self.bonus == q:
                return (y * 10/100)
        for q in range (10,21):
            if self.bonus == q:
                return (y * 20/100)
        for q in range (20,31):
            if self.bonus == q:
                return (y * 30/100)
        for q in range (30,41):
            if self.bonus == q:
                return (y * 40/100)
        for q in range (40,51):
            if self.bonus == q:
                return (y * 50/100)
        for q in range (50,61):
            if self.bonus == q:
                return (y * 60/100)
        for q in range (60,71):
            if self.bonus == q:
                return (y * 70/100)
        for q in range (70,81):
            if self.bonus == q:
                return (y * 80/100)
        for q in range (80,91):
            if self.bonus == q:
                return (y * 90/100)
        for q in range (90,101):
            if self.bonus == q:
                return (y * 100/100)
        return self.bonus

    def Potongan(self):
        y = self.getPekerjaan()
        for q in range (0,11):
            if self.potongan == q:
                return (y * 10/100)
        for q in range (10,21):
            if self.potongan == q:
                return (y * 20/100)
        for q in range (20,31):
            if self.potongan == q:
                return (y * 30/100)
        for q in range (30,41):
            if self.potongan == q:
                return (y * 40/100)
        for q in range (40,51):
            if self.potongan == q:
                return (y * 50/100)
        for q in range (50,61):
            if self.potongan == q:
                return (y * 60/100)
        for q in range (60,71):
            if self.potongan == q:
                return (y * 70/100)
        for q in range (70,81):
            if self.potongan == q:
                return (y * 80/100)
        for q in range (80,91):
            if self.potongan == q:
                return (y * 90/100)
        for q in range (90,101):
            if self.potongan == q:
                return (y * 100/100)
        return self.potongan
        
    def cetak(self):
        print(
            'Nama karyawan  \t:',self.nama,
            '\nJenis Pekerjaan :',self.jenis,
            '\nBonus \t\t:',self.bonus,'%',
            '\nPotongan \t:',self.potongan,'%',
            '\nGaji pokok \t:',self.getPekerjaan(),
            '\nJumlah Bonus \t:',self.Bonus(),
            '\nJumlah Potongan :',self.Potongan(),
            '\nTotal Gaji \t:', self.getPekerjaan() + self.Bonus() - self.Potongan()
        )
class gajiKedua(karyawan):
    def __init__(self, nama, jenis, bonus, potongan):
        super().__init__(nama, jenis, bonus, potongan)

    def getGaji_Kedua(self):
        return (self.getPekerjaan() + self.Bonus() - self.Potongan())
        
    def cetak(self):
        super().cetak()


rtf = karyawan('Rosyad', 'Manager', 6, 50)
rtf.cetak()
rtf2 = gajiKedua('Rosyad', 'Divisi',5,10)
rtf2.cetak()