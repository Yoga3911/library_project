import json, os, time, sys, csv
from datetime import date, timedelta, datetime
from colorama import Fore as F
from colorama import Style as S

uname = "admin123"
pword = "admin123"
daftar_buku = "daftar_buku_tersedia.json"
daftar_pinjam = "daftar_peminjam.json"
waktu_sekarang = datetime.now()
waktu_pengembalian = datetime.now() + timedelta(days=10)
blok = 0
struk = []
data_user = []
tampung_username = []    
tampung_password = []    
login = []
try:
    with open("database.csv", "r") as csvfile:
        baca = csv.reader(csvfile)
        for item in baca:
            login.append(item)
except:
    pass
if login == []:
    login.insert(0, [uname, pword])
with open("database.csv", "w", newline="") as reg:
    tulis = csv.writer(reg)
    for t in login:
        tulis.writerow(t)
        
def menu_awal():
    os.system("cls")
    print("="*100)
    print("||"+"Perpusku".center(96)+"||")
    print("="*100)
    print("|| "+"Daftar Menu".ljust(95)+"||")
    if uname in tampung_username:
        if pword in tampung_password:
            print("|| "+"[1] Tambahkan buku".ljust(95)+"||")
            print("|| "+"[2] Daftar buku yang dipinjam".ljust(95)+"||")
            print("|| "+"[3] Perbarui Daftar".ljust(95)+"||")
            print("|| "+"[4] Hapus buku".ljust(95)+"||")
            print("|| "+"[5] Baca Feedback".ljust(95)+"||")
            print("|| "+"[0] Keluar".ljust(95)+"||")
            print("="*100)
            print("||"+"By  : @Ardin & @Yugo".center(96)+"||")
            print("="*100)
            tanya = input("=> Masukkan pilihan anda = ")
            if tanya == "1":
                create_admin()
            elif tanya == "2":
                read_data()
            elif tanya == "3":
                update_data()
            elif tanya == "4":
                delete_data()
            elif tanya == "5":
                baca_feedback()
            elif tanya == "0":
                tanya_keluar = input("Apakah anda yakin ingin keluar? [y/t]: ")
                if tanya_keluar == "y":
                    print(S.RESET_ALL)
                    tampung_username.clear()
                    tampung_password.clear()
                    awal()
                else:
                    menu_awal()
    else:
        print("|| "+"[1] Pinjam buku".ljust(95)+"||")
        print("|| "+"[2] Kembalikan buku".ljust(95)+"||")
        print("|| "+"[3] Riwayat peminjaman buku".ljust(95)+"||")
        print("|| "+"[4] Ganti warna teks".ljust(95)+"||")
        print("|| "+"[5] Feedback".ljust(95)+"||")
        print("|| "+"[0] Keluar".ljust(95)+"||")
        print("="*100)
        print("||"+"By  : @Ardin & @Yugo".center(96)+"||")
        print("="*100)
        tanya = input("=> Masukkan pilihan anda = ")
        if tanya == "1":
            pinjam_buku()
        elif tanya == "2":
            kembalikan_buku()
        elif tanya == "3":
            riwayat_pinjam()
        elif tanya == "4":
            warna_teks()
        elif tanya == "5":
            feedback_user()
        elif tanya == "0":
            tanya_keluar = input("Apakah anda yakin ingin keluar? [y/t]: ")
            if tanya_keluar == "y":
                print(S.RESET_ALL)
                tampung_username.clear()
                tampung_password.clear()
                awal()
            else:
                menu_awal()
        else:
            menu_awal()

def create_admin():
    os.system("cls")
    print("="*100)
    print("||"+"Tambah buku".center(96)+"||")
    print("="*100)
    tampung_list = list()
    tampung_dict = dict()
    tambah_buku = input("Masukkan judul buku         : ").title()
    tampung_dict["Judul Buku"] = tambah_buku
    try:
        with open(daftar_buku, "r") as js:
                data = json.load(js)
                for i in data:
                    tampung_list.append(i)
    except:
        pass
    tampung_list.append(tampung_dict)
    struk.append(tampung_dict)
    with open(daftar_buku, "w") as jss:
        tulis = json.dump(tampung_list, jss, indent=2)
    print("Buku berhasil ditambahkan")
    input("\nEnter untuk kembali")
    menu_awal()
    
def pinjam_buku():
    os.system("cls")
    global struk
    print("="*100)
    print("||"+"Pinjam buku".center(96)+"||")
    print("="*100)
    daftar_sementara = list()
    tampung_list = list()
    tampung_dict = dict()
    try:
        with open(daftar_buku, "r") as js:
            baca = json.load(js)
            for b in baca:
                daftar_sementara.append(b)
                
        with open(daftar_pinjam, "r") as pj:
            baca_pinjam = json.load(pj)
            for bp in baca_pinjam:
                tampung_list.append(bp)
    except:
        pass
    print(f"{'No' : ^6} {'Judul Buku' : ^15}")
    print("="*100)
    index = 1
    tampung_index = []
    for d in daftar_sementara:
        print(f"{index : ^6}{d['Judul Buku'] : ^15}")
        tampung_index.append(index)
        index += 1
    try:
        tanya_pinjam = input("\nBuku mana yang ingin anda pinjam: ")
        tanya_nomer = int(tanya_pinjam)
        if int(tanya_pinjam) in tampung_index:
            tanya_pinjam = daftar_sementara[int(tanya_pinjam)-1]["Judul Buku"]
        tampung_dict["Nama"] = input("Masukkan nama: ")
        tampung_dict["Judul Buku"] = tanya_pinjam
        tampung_dict["Tanggal Peminjaman"] = waktu_sekarang.strftime("%Y-%m-%d")
        tampung_dict["Batas pengembalian"] = waktu_pengembalian.strftime("%Y-%m-%d")
        tampung_list.append(tampung_dict)
        struk.insert(0, tampung_dict)
        print("Buku berhasil dipinjam")
    except:
        pass
    with open(daftar_pinjam, "w") as jss:
        tulis = json.dump(tampung_list, jss, indent=2)
    tampung_list.clear()
    try:
        if tanya_nomer == 0:
            pass
        else:
            tanya_nomer -= 1
            with open(daftar_buku, "r") as jsn:
                baca = json.load(jsn)
                for b in baca:
                    tampung_list.append(b)
            tampung_list.pop(tanya_nomer)
            with open(daftar_buku, "w") as jsnn:
                tulis = json.dump(tampung_list, jsnn, indent=2)
    except:
        pass
    input("\nEnter untuk kembali")
    menu_awal()
    
def view():
    daftar_sementara = list()
    try:
        with open(daftar_buku, "r") as js:
            baca = json.load(js)
            for b in baca:
                daftar_sementara.append(b)
    except:
        pass
    print(f"{'No' : ^6} {'Judul Buku' : ^20}")
    print("="*120)
    index = 1
    for d in daftar_sementara:
        print(f"{index : ^6} {d['Judul Buku'] : ^20}")
        index += 1
    print("="*120)
    print("||"+"By  : @Ardin & @Yugo".center(116)+"||")
    print("="*120)
        
def read_data():
    os.system("cls")
    daftar_sementara = list()
    try:
        with open(daftar_pinjam, "r") as js:
            baca = json.load(js)
            for b in baca:
                daftar_sementara.append(b)
    except:
        pass
    print("="*123)
    print("|| "+"Daftar buku".ljust(118)+"||")
    print("="*123)
    print(f"||{'No' : ^5} {'Nama' : ^20} {'Judul Buku' : ^20} {'Tanggal Peminjaman' : ^25} {'Batas pengembalian' : ^17} ||")
    print("="*123)
    index = 1
    for d in daftar_sementara:
        print(f"||{index : ^6} {d['Nama'] : ^20} {d['Judul Buku'] : ^20} {d['Tanggal Peminjaman'] : ^25} {d['Batas pengembalian'] : ^21} ||")
        index += 1
    print("="*123)
    print("||"+"By  : @Ardin & @Yugo".center(119)+"||")
    print("="*123)
    input("Enter untuk kembali")
    menu_awal()

def update_data():
    os.system("cls")
    print("="*100)
    print("||"+"Perbarui Daftar".center(96)+"||")
    print("="*100)
    tampung_list = list()
    tampung_dict = dict()
    view()
    try:
        tanya = int(input("Data no: "))
        tanya -= 1
        with open(daftar_buku, "r") as jsn:
            data = json.load(jsn)
            for i in data:
                tampung_list.append(i)
        tampung_list.pop(tanya)
        tampung_dict["Judul Buku"] = input("Masukkan judul buku: ")
        tampung_list.insert(tanya, tampung_dict)
        with open(daftar_buku, "w") as jsnn:
            tulis = json.dump(tampung_list, jsnn, indent=2)
        print("Data berhasil diperbarui")
    except:
        print("Data tidak ada pada daftar")
    input("\nEnter untuk kembali")
    menu_awal()
        
def delete_data():
    os.system("cls")
    print("="*100)
    print("||"+"Hapus buku".center(96)+"||")
    print("="*100)
    tampung_list = list()
    tampung_dict = dict()
    view()
    try:
        tanya = int(input("Data no: "))
        if tanya == 0:
            pass
        else:
            tanya -= 1
            with open(daftar_buku, "r") as jsn:
                baca = json.load(jsn)
                for b in baca:
                    tampung_list.append(b)
            tampung_list.pop(tanya)
            with open(daftar_buku, "w") as jsnn:
                tulis = json.dump(tampung_list, jsnn, indent=2)
    except:
        print("Data yang anda maksud tidak ada")
    input("\nEnter untuk kembali")
    menu_awal()

def riwayat_pinjam():
    os.system("cls")
    print("="*100)
    print("||"+"Riwayat Peminjaman Buku".center(96)+"||")
    print("="*100)
    if struk != []:
        for d in struk:
            print("||"+"Nama                 :",d["Nama"].ljust(73)+"||")
            print("||"+"Judul buku           :",d["Judul Buku"].ljust(73)+"||")
            print("||"+"Tanggal peminjaman   :",d["Tanggal Peminjaman"].ljust(73)+"||")
            print("||"+"Batas pengembalian   :",d["Batas pengembalian"].ljust(73)+"||")
            break
    elif struk == []:
        print("Tidak ada buku yang akan dipinjam")
    print("="*100)
    input("\nEnter untuk kembali")
    menu_awal()

def kembalikan_buku():
    os.system("cls")
    print("="*100)
    print("||"+"Kembalikan buku".center(96)+"||")
    print("="*100)
    tampung = list()
    tampung_list = list()
    tampung_dict = dict()
    list_waktu = list()
    dict_waktu = dict()
    try:
        with open(daftar_pinjam, "r") as rr:
            baca= json.load(rr)
            for b in baca:
                tampung.append(b)
    except:
        print("Tidak ada buku yang dipinjam")
    found = []
    tanya = input("Masukkan judul buku: ")
    index = 0
    for data in tampung:
        if(data["Judul Buku"] == tanya):
            found = tampung[index]
        index += 1

    if len(found) > 0:
        print("Terlambat 1 hari denda Rp. 1000")
        print(f"Nama: {found['Nama']}")
        print(f"Judul buku: {found['Judul Buku']}")
        print(f"Tanggal peminjaman: {found['Tanggal Peminjaman']}")
        print(f"Batas pengembalian: {found['Batas pengembalian']}")
        print("="*100)
        print("Dikembalikan tanggal:",waktu_sekarang.strftime("%Y-%m-%d"))
        dict_waktu["Tanggal Sekarang"] = waktu_sekarang.strftime("%Y-%m-%d")
        list_waktu.append(dict_waktu)
        panggil_sekarang = list_waktu[0]["Tanggal Sekarang"]
        panggil_pengembalian = f"{found['Batas pengembalian']}"
        tanggal_sekarang = datetime.strptime(panggil_sekarang,"%Y-%m-%d")
        tanggal_pengembalian = datetime.strptime(panggil_pengembalian,"%Y-%m-%d")
        cast_sekarang = int(tanggal_sekarang.strftime("%Y%m%d"))
        cast_pengembalian = int(tanggal_pengembalian.strftime("%Y%m%d"))
        kurang = str(tanggal_sekarang - tanggal_pengembalian)
        ambil_digit = kurang[0:3]
        if cast_sekarang > cast_pengembalian:
            cek_kurang = ambil_digit.isnumeric()
            if cek_kurang == True:
                print("Denda: Rp.", int(kurang[0:3]) * 1000)
            elif cek_kurang == False: 
                print("Denda: Rp.", int(kurang[0:2]) * 1000)
        elif cast_sekarang == cast_pengembalian:
            print("Tidak ada denda")
        elif cast_sekarang < cast_pengembalian:
            print("Tidak ada denda")
    else:
        print("Cek nama buku anda dengan benar")
    try:
        with open(daftar_buku, "r") as db:
            bac = json.load(db)
            for ba in bac:
                tampung_list.append(ba)
        tampung_dict["Judul Buku"] = f"{found['Judul Buku']}"
        tampung_list.append(tampung_dict)
        with open(daftar_buku, "w") as dbb:
            tuli = json.dump(tampung_list, dbb, indent=2)
        hapus = int(tampung.index(found))
        tampung_list.clear()
        tampung_dict.clear()
        if hapus >= 0:
            with open(daftar_pinjam, "r") as jsn:
                baca = json.load(jsn)
                for b in baca:
                    tampung_list.append(b)
            tampung_list.pop(hapus)
            with open(daftar_pinjam, "w") as jsnn:
                tulis = json.dump(tampung_list, jsnn, indent=2)
    except:
        pass
    input("\nEnter untuk kembali")
    menu_awal()

def warna_teks():
    os.system("cls")
    print("="*100)
    print("||"+"Feedback".center(96)+"||")
    print("="*100)
    print("|| "+"[1] Merah".ljust(95)+"||")
    print("|| "+"[2] Kuning".ljust(95)+"||")    
    print("|| "+"[3] Hijau".ljust(95)+"||")
    print("|| "+"[4] Biru".ljust(95)+"||")
    print("|| "+"[5] Cyan".ljust(95)+"||")
    print("|| "+"[6] Default".ljust(95)+"||")
    print("="*100)
    print("||"+"By  : @Ardin & @Yugo".center(96)+"||")
    print("="*100)
    warna = input("=> Masukkan pilihan anda = ")
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
    input("Enter untuk kembali")
    menu_awal()

def feedback_user():
    os.system("cls")
    tampung_feedback = []
    feedback = dict()
    file_name = 'data_feedback.json'
    print("="*100)
    print("||"+"Feedback".center(96)+"||")
    print("="*100)
    print("|| "+"[1] Sangat baik".ljust(95)+"||")
    print("|| "+"[2] Baik".ljust(95)+"||")    
    print("|| "+"[3] Cukup".ljust(95)+"||")
    print("|| "+"[4] Kurang".ljust(95)+"||")
    print("="*100)
    print("||"+"By  : @Ardin & @Yugo".center(96)+"||")
    print("="*100)
    saran = input("Beri nilai kami        : ")
    komentar = input("Beri komentar          : ")
    if saran == '1':
        saran="Sangat Baik"
    elif saran == '2':
        saran = 'Baik'
    elif saran == '3':
        saran = 'Cukup'
    elif saran == '4':
        saran = 'Kurang'
    else:
        feedback_user()
    feedback['Nilai'] = saran
    feedback['Komentar'] = komentar
    try :
        with open(file_name,'r') as jsonread:
            reader=json.load(jsonread)
            for i in reader:
                tampung_feedback.append(i)
    except:
        pass
    tampung_feedback.append(feedback)
    with open(file_name,'w') as jsonfile:
        json.dump(tampung_feedback,jsonfile,indent=2)
    enter=input("Tekan enter untuk kembali...")
    menu_awal()

def baca_feedback():
    os.system("cls")
    print("="*80)
    print("||"+"Daftar Feedback".center(76)+"||")
    print("="*80)
    if uname in tampung_username:
        if pword in tampung_password:
            tampung_feedback = list()
            try:
                with open("data_feedback.json", "r") as bc:
                    baca = json.load(bc)
                    for b in baca:
                        tampung_feedback.append(b)
            except:
                print("Tidak ada feedback")
            print(f"||{'No':^6} {'Nilai':^12} {'Komentar':^25}".ljust(78)+"||")
            print("="*80)
            index = 1
            for t in tampung_feedback:
                print(f"||{index:^6}{t['Nilai']:<21} {t['Komentar']:<25}".ljust(78)+"||")
                index += 1
            print("="*80)
    else:
        print("Hanya admin yang bisa mengakses menu ini\n")
    input("Enter untuk kembali")
    menu_awal()

def awal():
    os.system("cls")
    try:
        data_user.pop(0)
    except:
        pass
    print("="*100)
    print("||"+"Perpusku".center(96)+"||")
    print("="*100)
    print("||"+"Selamat datang di aplikasi perpusku!".center(96)+"||")
    print("||"+"Silahkan login jika anda telah memiliki akun".center(96)+"||")
    print("||"+"Dan silahkan mendaftar terlebih dahulu jika anda tida mempunyai akun.".center(96)+"||")
    print("="*100)
    print("|| "+"[1] Masuk".ljust(95)+"||")
    print("|| "+"[2] Daftar".ljust(95)+"||")    
    print("|| "+"[3] Keluar".ljust(95)+"||")    
    print("="*100)
    print("||"+"By  : @Ardin & @Yugo".center(96)+"||")
    print("="*100)
    tanya = input("=> Masukkan pilihan anda = ")
    if tanya == "1":
        login_user()
    elif tanya == "2":
        register_user()
    elif tanya == "3":
        exit()
        
def login_user():
    os.system("cls")
    print("="*100)
    print("||"+"Perpusku".center(96)+"||")
    print("="*100)
    global tampung_username
    global tampung_password
    global blok
    nama = []
    sandi = []
    with open("database.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        try:
            for row in csv_reader:
                nama.append(row[0])
                sandi.append(row[1])
        except:
            pass
    username = input("Username      : ")
    password = input("Password      : ")
    if username in nama:
        index = nama.index(username)
        if password == sandi[index]:
            if username == "admin123":
                tampung_username.append(uname)
            if password == "admin123":
                tampung_password.append(pword)
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
    else:
        print("Username tidak ditemukan")
    input("Enter untuk kembali")
    awal()
    
def register_user():   
    os.system("cls")
    valid = 0
    print("="*100)
    print("||"+"Perpusku".center(96)+"||")
    print("="*100)
    username = input("Username      : ")
    password = input("Password      : ")
    if username.isalnum() == False or password.isalnum() == False:
        valid += 1
        print("Username atau Password hanya berupa huruf dan angka")
    if len(username) < 6 or len(password) < 6:
        valid += 1
        print("Username atau password minimal harus terdiri dari 6 karakter")
    if username == password:
        valid += 1
        print("Username dan password tidak boleh sama")
    if valid == 0:
        data_user.append([username, password])
        with open("database.csv", "a", newline="") as css:
            tulis = csv.writer(css, delimiter=",")
            for t in data_user:
                tulis.writerow(t)
        print("Akun berhasil dibuat")
    else:
        pass
    input("Enter untuk kembali")
    awal()
    
while True:
    awal()
