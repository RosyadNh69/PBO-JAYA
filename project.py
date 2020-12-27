import sqlite3

koneksi = sqlite3.connect('D:/Semester 3/PBO/Project/PBO-JAYA/data.db')

class karyawan:
    jenis_pekerjaan = []

    def tambahKaryawan(self):
        global koneksi
        nama = input('Masukkan nama karyawan : ')
        jenis = input('Jenis Pekerjaan : ')
        id_gaji = input('ID gaji : ')
        karyawan.jenis_pekerjaan.append(jenis)
        query = f'INSERT INTO karyawan(nama, jenis_Pekerjaan, id_gaji) VALUES ("{nama}", "{jenis}","{id_gaji}")'
        koneksi.execute(query)
        koneksi.commit()

    def tambahGaji(self, bonus, potongan):
        self.bonus = bonus
        self.potongan = potongan
        x = 0
        p = 0
        a = 0
        c = 1000000
        y = 2000000
        global koneksi
        jenis = input('Jenis Pekerjaan : ')
        if jenis == 'Manager':
            p = 8000000
        elif jenis == 'Divisi':
            p = 6000000
        elif jenis == 'Karyawan':
            p = 4000000
        elif jenis == 'Cleaning':
            p = 2000000
        for q in range (1,11):
            if self.potongan == q:
                a = c * 10/100
        for q in range (10,21):
            if self.potongan == q:
                a = c * 20/100
        for q in range (20,31):
            if self.potongan == q:
                a = c * 30/100
        for q in range (30,41):
            if self.potongan == q:
                a = c * 40/100
        for q in range (40,51):
            if self.potongan == q:
                a = c * 50/100
        for q in range (50,61):
            if self.potongan == q:
                a = c * 60/100
        for q in range (60,71):
            if self.potongan == q:
                a = c * 70/100
        for q in range (70,81):
            if self.potongan == q:
                a = c * 80/100
        for q in range (80,91):
            if self.potongan == q:
                a = c * 90/100
        for q in range (90,101):
            if self.potongan == q:
                a = c * 100/100
        for q in range (1,11):
            if self.bonus == q:
                x = y * 10/100
        for q in range (10,21):
            if self.bonus == q:
                x = y * 20/100
        for q in range (20,31):
            if self.bonus == q:
                x = y * 30/100
        for q in range (30,41):
            if self.bonus == q:
                x = y * 40/100
        for q in range (40,51):
            if self.bonus == q:
                x = y * 50/100
        for q in range (50,61):
            if self.bonus == q:
                x = y * 60/100
        for q in range (60,71):
            if self.bonus == q:
                x = y * 70/100
        for q in range (70,81):
            if self.bonus == q:
                x = y * 80/100
        for q in range (80,91):
            if self.bonus == q:
                x = y * 90/100
        for q in range (90,101):
            if self.bonus == q:
                x = y * 100/100
        t = (p + x - a)
        query = f'INSERT INTO gaji(gaji_Pokok, bonus, potongan, total_GAji) VALUES ("{p}","{x}","{a}","{t}")'
        koneksi.execute(query)
        koneksi.commit()

    def dataKaryawan(self):
        global koneksi
        for row in koneksi.execute('SELECT * FROM karyawan'):
            print(row)

    def tampilGaji(self):
        global koneksi
        for row in koneksi.execute('SELECT karyawan.id, karyawan.nama, karyawan.jenis_Pekerjaan, gaji.gaji_Pokok, gaji.bonus, gaji.potongan, gaji.total_Gaji FROM karyawan INNER JOIN gaji ON karyawan.id=gaji.id'):
            print(row)

    def tampilGajiJenis(self):
        jenis = input('Jenis Pekerjaan : ')
        global koneksi
        if jenis == 'Manager':
            for row in koneksi.execute("SELECT karyawan.id, karyawan.nama, karyawan.jenis_Pekerjaan, gaji.gaji_Pokok, gaji.bonus, gaji.potongan, gaji.total_Gaji FROM karyawan INNER JOIN gaji ON karyawan.id=gaji.id WHERE karyawan.jenis_Pekerjaan='Manager' AND gaji.gaji_Pokok=8000000"):
                print(row)
        if jenis == 'Divisi':
            for row in koneksi.execute("SELECT karyawan.id, karyawan.nama, karyawan.jenis_Pekerjaan, gaji.gaji_Pokok, gaji.bonus, gaji.potongan, gaji.total_Gaji FROM karyawan INNER JOIN gaji ON karyawan.id=gaji.id WHERE karyawan.jenis_Pekerjaan='Divisi' AND gaji.gaji_Pokok=6000000"):
                print(row)
        if jenis == 'Karyawan':
            for row in koneksi.execute("SELECT karyawan.id, karyawan.nama, karyawan.jenis_Pekerjaan, gaji.gaji_Pokok, gaji.bonus, gaji.potongan, gaji.total_Gaji FROM karyawan INNER JOIN gaji ON karyawan.id=gaji.id WHERE karyawan.jenis_Pekerjaan='Karyawan' AND gaji.gaji_Pokok=4000000"):
                print(row)
        if jenis == 'Cleaning':
            for row in koneksi.execute("SELECT karyawan.id, karyawan.nama, karyawan.jenis_Pekerjaan, gaji.gaji_Pokok, gaji.bonus, gaji.potongan, gaji.total_Gaji FROM karyawan INNER JOIN gaji ON karyawan.id=gaji.id WHERE karyawan.jenis_Pekerjaan='Karyawan' AND gaji.gaji_Pokok=2000000"):
                print(row)

a = karyawan()

while True :
    print("\n")
    print("====== Pilihan Menu ======")
    print("""
        1. Tambahkan data Karyawan
        2. Tambahkan data Gaji Karyawan
        3. Tampilkan data Karyawan
        4. Tampilkan data Gaji karyawan
        5. Tampilkan gaji karyawan menurut jenis pekerjaan
        99. Exit
    """)
    pilihan = int(input('Pilihan: '))
    if (pilihan == 1):
        a.tambahKaryawan()
    elif (pilihan == 2):
        a.tambahGaji(80, 40)
    elif (pilihan == 3): 
        a.dataKaryawan()
    elif (pilihan == 4):
        a.tampilGaji()
    elif (pilihan == 5):
        a.tampilGajiJenis()
    elif (pilihan == 99):
        break
    else:
        print('Menu tidak valid!')