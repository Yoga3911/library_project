import json, os, time, sys, csv
from datetime import datetime as dt
from colorama import Fore as F
from colorama import Style as S

uname = "admin123"
pword = "admin123"
tampung_admin = []
karcis = list()
file_json = "data_perpus.json"

def menu_awal():
    os.system("cls")
    print("1. Pinjam buku\n2. Daftar buku yang sudah dipinjam\n3. Perbarui daftar\n4. Hapus buku\n5. Bayar Buku\n6. Ganti warna teks\n7. Log out")
    tanya = input("Pilihanmu: ")
    if tanya == "1":
        create_data()
    elif tanya == "2":
        read_data()
    elif tanya == "3":
        update_data()
    elif tanya == "4":
        delete_data()
    elif tanya == "5":
        bayar_buku()
    elif tanya == "6":
        warna_teks()
    elif tanya == "7":
        keluar()
    else:
        menu_awal()
        
def create_data():
    os.system("cls")
    tampung_list = list()
    tampung_dict = dict()
    try:
        karcis.pop(0)
    except:
        pass
    try:
        tampung_dict["Nama"] = input("Masukkan nama: ")
        try:
            tampung_dict["Kode Buku"] = int(input("Masukkan kode buku: "))
        except:
            print("Kode buku hanya berupa angka")
            input("Enter untuk mengisi ulang data")
            create_data()
        tampung_dict["Judul Buku"] = input("Masukkan judul buku: ")
        date =  dt.now()
        a = date.day + 10
        b = date.month
        c = date.year
        d = a, b, c
        tampung_dict["Tanggal Peminjaman"] = dt.now().strftime("(%d, %m, %Y)")
        tampung_dict["Tanggal Pengembalian"] = str(d)
        try:
            tampung_dict["Harga Buku"] = int(input("Masukkan harga buku: "))
        except:
            print("Harga buku hanya berupa angka")
            input("Enter untuk mengisi ulang data")
            create_data()
        try:
            with open(file_json, "r") as js:
                    data = json.load(js)
                    for i in data:
                        tampung_list.append(i)
        except:
            pass
        tampung_list.append(tampung_dict)
        karcis.append(tampung_dict)
        with open(file_json, "w") as jss:
            tulis = json.dump(tampung_list, jss, indent=2)
    except:
        print("Mohon isi data dengan benar")
    menu_awal()

def view():
    os.system("cls")
    daftar_sementara = list()
    try:
        with open(file_json, "r") as js:
            baca = json.load(js)
            for b in baca:
                daftar_sementara.append(b)
    except:
        pass
    print(f"{'No' : ^6} {'Kode Buku' : ^6} {'Nama' : ^15} {'Judul Buku' : ^10} {'Tanggal Peminjaman' : ^19} {'Tanggal Pengembalian' : ^17} {'Harga Buku' : ^17}")
    index = 1
    for d in daftar_sementara:
        harga = ("Rp. {0:,}".format(d['Harga Buku']))
        print(f"{index : ^6} {d['Kode Buku'] : ^6} {d['Nama'] : ^15} {d['Judul Buku'] : ^10} {d['Tanggal Peminjaman'] : ^19} {d['Tanggal Pengembalian'] : ^17} {harga : ^17}")
        index += 1
        
def read_data():
    os.system("cls")
    daftar_sementara = list()
    try:
        with open(file_json, "r") as js:
            baca = json.load(js)
            for b in baca:
                daftar_sementara.append(b)
    except:
        pass
    print(f"{'No' : ^6} {'Kode Buku' : ^6} {'Nama' : ^15} {'Judul Buku' : ^10} {'Tanggal Peminjaman' : ^19} {'Tanggal Pengembalian' : ^17} {'Harga Buku' : ^17}")
    index = 1
    for d in daftar_sementara:
        harga = ("Rp. {0:,}".format(d['Harga Buku']))
        print(f"{index : ^6}{d['Kode Buku'] : ^6} {d['Nama'] : ^15} {d['Judul Buku'] : ^10} {d['Tanggal Peminjaman'] : ^19} {d['Tanggal Pengembalian'] : ^17} {harga : ^17}")
        index += 1
    input("Enter untuk kembali")
    menu_awal()
    
def update_data():
    os.system("cls")
    tampung_list = list()
    tampung_dict = dict()
    if username == uname:
        if password == pword:
            view()
            try:
                tanya = int(input("Data no: "))
                tanya -= 1
                with open(file_json, "r") as jsn:
                    data = json.load(jsn)
                    for i in data:
                        tampung_list.append(i)
                tampung_list.pop(tanya)
                tampung_dict["Nama"] = input("Masukkan nama: ")
                try:
                    tampung_dict["Kode Buku"] = int(input("Masukkan kode buku: "))
                except:
                    print("Kode buku hanya berupa angka")
                    input("Enter untuk mengisi ulang data")
                    create_data()
                tampung_dict["Judul Buku"] = input("Masukkan judul buku: ")
                date =  dt.now()
                a = date.day + 10
                b = date.month
                c = date.year
                d = a, b, c
                tampung_dict["Tanggal Peminjaman"] = dt.now().strftime("(%d, %m, %Y)")
                tampung_dict["Tanggal Pengembalian"] = str(d)
                try:
                    tampung_dict["Harga Buku"] = int(input("Masukkan harga buku: "))
                except:
                    print("Harga buku hanya berupa angka")
                    input("Enter untuk mengisi ulang data")
                    update_data()
                tampung_list.insert(tanya, tampung_dict)
                with open(file_json, "w") as jsnn:
                    tulis = json.dump(tampung_list, jsnn, indent=2)
            except:
                print("Data tidak ada pada daftar")
        else:
            pass
    else:
        print("Maaf hanya admin yang boleh mengakses menu ini")
    input("Enter untuk kembali")
    menu_awal()
        
def delete_data():
    os.system("cls")
    tampung_list = list()
    tampung_dict = dict()
    if username == uname:
        if password == pword:
            view()
            try:
                tanya = int(input("Data no: "))
                if tanya == 0:
                    pass
                tanya -= 1
                with open(file_json, "r") as jsn:
                    baca = json.load(jsn)
                    for b in baca:
                        tampung_list.append(b)
                tampung_list.pop(tanya)
                with open(file_json, "w") as jsnn:
                    tulis = json.dump(tampung_list, jsnn, indent=2)
            except:
                print("Data yang anda maksud tidak ada")
        else:
            pass
    else:
        print("Maaf hanya admin yang bisa mengakses menu ini")
    input("Enter untuk kembali")
    menu_awal()

def bayar_buku():
    os.system("cls")
    baca_karcis()
    tampungan_list = list()
    try:
        tanya = int(input("Masukkan kode buku: "))
        with open(file_json, "r") as js:
            baca = json.loads(js.read())
            tampungan_list.append(baca)
        for b in baca:
            if b['Kode Buku'] == tanya:
                cetak_karcis()
    except:
        pass
    print("Buku tidak ditemukan")
    input("Enter untuk kembali")
    menu_awal()

def baca_karcis():
    print(f"{'No' : ^6} {'Kode Buku' : ^6} {'Nama' : ^15} {'Judul Buku' : ^10} {'Tanggal Peminjaman' : ^19} {'Tanggal Pengembalian' : ^17} {'Harga Buku' : ^17}")
    index = 1
    for d in karcis:
        harga = ("Rp. {0:,}".format(d['Harga Buku']))
        print(f"{index : ^6}{d['Kode Buku'] : ^6} {d['Nama'] : ^15} {d['Judul Buku'] : ^10} {d['Tanggal Peminjaman'] : ^19} {d['Tanggal Pengembalian'] : ^17} {harga : ^17}")
        index += 1
    
def cetak_karcis():
    os.system("cls")
    for d in karcis:
        print("Nama:",d["Nama"])
        print("Kode buku:",d["Kode Buku"])
        print("Judul buku:",d["Judul Buku"])
        print("Tanggal peminjaman:",d["Tanggal Peminjaman"])
        print("Tanggal pengembalian:",d["Tanggal Pengembalian"])
        print("Harga buku:",d["Harga Buku"])
        tanya = input("Bayar buku [y/t]: ")
        if tanya == "y":
            try:
                karcis.pop(0)
            except:
                pass
            print("Buku berhasil dibayar")
        else:
            pass
    input("Enter untuk kembali")
    menu_awal()

def keluar():
    for i in range(1):
        print("Sampai jumpa ...")
        print(S.RESET_ALL, end = "")
        break
    
def warna_teks():
    os.system("cls")
    print("1. Merah\n2. Kuning\n3. Hijau\n4. Biru\n5. Cyan\n6. Default")
    warna = input("Pilihanmu: ")
    if warna == "1":
        print(F.RED, S.BRIGHT, end = "")
    elif warna == "2":
        print(F.YELLOW, S.BRIGHT, end = "")
    elif warna == "3":
        print(F.GREEN, S.BRIGHT, end = "")
    elif warna == "4":
        print(F.BLUE, S.BRIGHT, end = "")
    elif warna == "5":
        print(F.CYAN, S.BRIGHT,end = "")
    elif warna == "6":
        print(F.WHITE, end = "")
    else:
        warna_teks()
    input("Enter untuk kembali")
    menu_awal()
            
blok = 0
valid = 0
while True:
    os.system("cls")
    tampung_admin.append([uname, pword])
    with open("{}.csv".format(uname), "w", newline="") as reg:
        tulis = csv.writer(reg)
        for t in tampung_admin:
            tulis.writerow(t)
    print("1. Login\n2. Register\n3. Exit")
    tanya = input("Pilih: ")
    if tanya == "1":
        os.system("cls")
        username = input("Username: ")
        password = input("Password: ")
        tampung1 = []
        try:
            with open("{}.csv".format(username), "r", newline="") as log:
                baca = csv.reader(log)
                for b in baca:
                    tampung1.append(b)
            if username == tampung1[0][0] and password == tampung1[0][1]:
                menu_awal()
            else:
                blok += 1
                print("Username atau Password salah")
            if blok == 3:
                print("Terblokir selama 10 detik")
                input("Enter")
                blok -= blok
                waktu = 10*"1"
                index = 1
                for i in waktu:
                    os.system("cls")
                    print(index)
                    sys.stdout.flush()
                    time.sleep(1)
                    index += 1
        except:
            print("Username tidak ditemukan")
        input("Enter untuk kembali")
        
    elif tanya == "2":
        os.system("cls")
        tampung2 = []
        username = input("Username: ")
        password = input("Password: ")
        cek1 = username.isalnum()
        cek2 = password.isalnum()
        try:
            cek3 = username[0].islower()
        except:
            pass
        if username == "" or username == " ":
            valid += 1
            print("Username tidak boleh kosong")

        if password == "" or password == " ":
            valid += 1
            print("Password tidak boleh kosong")

        if len(username) < 6:
            valid += 1
            print("Username minimal harus terdiri dari 6 karakter")

        if len(password) < 6:
            valid += 1
            print("Password minimal harus terdiri dari 6 karakter")

        if cek1 == False:
            valid += 1
            print("Username hanya berupa huruf dan angka saja")

        if cek2 == False:
            valid += 1
            print("Password hanya berupa huruf dan angka saja")
        
        try:
            if cek3 == True:
                valid += 1
                print("Username harus dimulai dari huruf kapital")
        except:
            pass

        if username == password:
            valid += 1
            print("Username dan password tidak boleh sama")

        if valid == 0:
            tampung2.append([username, password])
            with open("{}.csv".format(username), "w", newline="") as reg:
                tulis = csv.writer(reg)
                for t in tampung2:
                    tulis.writerow(t)
            print("Akun berhasil dibuat")
        valid -= valid
        input("Enter untuk kembali")
    elif tanya == "3":
        exit()
    else:
        pass