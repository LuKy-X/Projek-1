import math

#===================================================================soal 1===============================================================
def hitung_mean():
    while True:
        try:
            angka = input("masukan angka-angkanya, dipisahkan dengan sepasi (1 2 3 dst)\t:")
            nilai = [float(x) for x in angka.split()]
            bil = 0
            jumlah = 0
            for y in nilai:
                bil += y
                jumlah += 1
            return f"mean dari angka yang anda masukan adalah {round(bil / jumlah, 2)}"
        except ValueError:
            print("inputan tidak valid, pastikan anda memasukan angka sesuai petunjuk\n")

#===================================================================soal 5===============================================================
def hitung_resistor():
    while True:
        try:
            print("1. Rangkaian seri")
            print("2. Rangkaian paralel")
            print("="*80)

            pilihan2 = int(input("pilih antara 1 dan 2\t:"))
            if pilihan2 not in range(1, 3):
                raise ValueError("pilihan tidak valid")
            break
        except ValueError as x:
            print(f"terjadi kesalahan {x}\n")
        
    while True:
        try:
            angka = input("masukan angka-angkanya, dipisahkan dengan sepasi (1 2 3 dst)\t:")
            nilai = [float(x) for x in angka.split()]
            if pilihan2 == 1:
                bil = 0
                for y in nilai:
                    bil += y
                return f"{round(bil, 2)} ohms"
            else:
                bil = 0
                for y in nilai:
                    bil += 1/y
                return f"{round(1/bil, 2)} ohms"
        except ValueError:
            print("inputan tidak valid, pastikan anda memasukan angka sesuai petunjuk\n")

#===================================================================soal 19===============================================================
def pythagoras_mencari_c():
    while True:
        try:
            a = float(input("masukan nilai a\t:"))
            b = float(input("masukan nilai b\t:"))
            c = math.sqrt((a**2 + b**2))
            return f"c = {round(c, 2)}"
        except ValueError:
            print("inputan tidak valid, pastikan anda memasukan angka sesuai petunjuk\n")

#===================================================================soal 20===============================================================
def sudut_pythagoras():
    while True:
        try:
            a = float(input("masukan nilai a\t:"))
            b = float(input("masukan nilai b\t:"))
            c = float(input("masukan nilai c\t:"))
            ab = (a**2 + b**2)
            C = c**2
            if  C == ab:
                return "segitiga abc memiliki sudut siku-siku pada ∠𝑐 (sudut 90°)"
            elif C < ab:
                return "segitiga abc memiliki sudut lancip pada ∠𝑐"
            else:
                return "segitiga abc memiliki sudut tumpul pada ∠𝑐"
        except ValueError:
            print("inputan tidak valid, pastikan anda memasukan angka\n")

#===================================================================soal 18===============================================================
def usaha_gravitasi():
    while True:
        try:
            m = float(input("masukan massanya [m] (dalam kilogram)     \t:"))
            g = float(input("masukan gravitasinya [g] (dalam m/s**2)  \t:"))
            h1 = float(input("masukan keinggian awal [h] (dalam meter)\t:"))
            h2 = float(input("masukan keinggian akhir [h] (dalam meter)\t:"))
            h = h2 - h1
            W = m * g * h
            return f"W = {round(W, 2)} Joule"
        except ValueError:
            print("inputan tidak valid, pastikan anda memasukan angka\n")

#===================================================================soal 12===============================================================
def pesawat_sederhana():
    while True:
        try:
            print("1. Gaya")
            print("2. Usaha")
            print("="*80)
            
            pilihan2 = int(input("pilih antara 1 dan 2\t:"))
            if pilihan2 not in range(1, 3):
                raise ValueError("pilihan tidak valid")
            break
        except ValueError as x:
            print(f"terjadi kesalahan {x}\n")

    while True:
        try:
            if pilihan2 == 1:
                m = float(input("masukan massanya [m] (dalam kilogram)\t:"))
                a = float(input("masukan percepatannya [a] (dalam m/s)\t:"))
                F = m*a
                return f"F = {round(F, 2)}N"
            else:
                F = float(input("masukan gayanya [F] (dalam Newton)\t:"))
                s = float(input("masukan jaraknya [s] (dalam meter)\t:"))
                W = F*s
                return f"W = {round(W, 2)} Joule"
        except ValueError:
            print("inputan tidak valid, pastikan anda memasukan angka\n")

#===================================================================soal 6===============================================================
def hitung_coulomb():
    while True:
        try:
            q1 = float(input("masukan muatan pertama [q1]                       \t:"))
            q2 = float(input("masukan muatan kedua [q2]                         \t:"))
            r = float(input("masukan jarak antara kedua muatan [r] (dalam meter)\t:"))
            if r == 0:
                raise ValueError("r tidak boleh bernilai 0, karena pembagian dengan 0 tidak didefinisikan")
            k = 8.99 * 10**9
            F = k * (q1 * q2) / (r**2)
            return f"Gaya Coulomb (F) adalah: {F:.2e}N"
        except ValueError:
            print("inputan tidak valid, pastikan anda memasukan angka\n")

def projek1():
    while True:
        print("="*80)
        print("1. Mean")
        print("2. Resistor")
        print("3. Pythagoras mencari c")
        print("4. Pythagoras mengkategorikan ∠𝑐")
        print("5. Usaha gravitasi")
        print("6. Pesawat sederhana")
        print("7. Coulomb")
        print("="*80)

        try:
            pilihan = int(input("pilih dari 1 sampai 7\t:"))
            if pilihan not in range(1, 8):
                raise ValueError("pilihan tidak valid")
            break
        except ValueError as x:
            print(f"terjadi kesalahan {x}\n")
    
    #mean
    if pilihan == 1:
        return hitung_mean()
    
    #resistor
    elif pilihan == 2:
        return hitung_resistor()
        
    #pythagoras mencari c
    elif pilihan == 3:
        return pythagoras_mencari_c()
        
    #pythagoras mencari sudut pada ∠𝑐
    elif pilihan == 4:
        return sudut_pythagoras()
    
    # usaha gravitasi 
    elif pilihan == 5:
        return usaha_gravitasi()
    
    #pesawat sederhana yang gaya dan usaha
    elif pilihan == 6:
        return pesawat_sederhana()
        
    #coulomb
    else:
        return hitung_coulomb()

while True:
    print(projek1())
    lanjut = input("ingin melanjutkan? (yes atau no)\t:").strip().lower()
    if lanjut != "yes":
        break