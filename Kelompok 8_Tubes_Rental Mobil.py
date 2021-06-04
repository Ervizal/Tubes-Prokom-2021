import os
import datetime
import time
import pandas as pd
from validate_email import validate_email
import threading
import sys
import itertools


def judul():
    os.system("cls")
    print("[======================================]")
    print("[=== PT NGABERS BRAKTAKTAK AND FREND ===]")
    print("[======================================]\n")


def menu_utama():
    print("====================")
    print("==== Menu Utama ====")
    print("====================")
    jam = datetime.datetime.now()
    print(jam.strftime("%A") + ",", jam.strftime("%d"), jam.strftime("%B"), jam.strftime("%Y"),
          jam.strftime("%H") + ":" + jam.strftime("%M") + ":" + jam.strftime("%S"))
    print("1. Login customer")
    print("2. Login admin")
    print("3. Exit program")
    while True:
        try:
            ut = int(input("Masukkan menu yang anda pilih (1/2/3) : "))
        except:
            print("Mohon masukkan angka 1/2/3")
        else:
            if ut in [1, 2, 3]:
                break
            else:
                print("Mohon masukkan angka 1/2/3")
                pass
    return ut


def login_cust():
    os.system("cls")
    print("========================")
    print("==== Login customer ====")
    print("========================")
    stat_akun = 0
    while True:
        if stat_akun == "Y" or stat_akun == "T":
            break
        else:
            stat_akun = input("Apakah anda sudah memiliki akun (Y/T) : ")
            stat_akun = stat_akun.upper()
    return stat_akun


def custY():
    os.system("cls")
    print("========================")
    print("==== Login customer ====")
    print("========================")
    pd.options.mode.chained_assignment = None  # default='warn', supaya tdk ada warning saat mengganti value

    # nama file
    file = "data_pelanggan.xlsx"

    # import dari xlsx yang sudah ada
    data_pelanggan = pd.read_excel(file, index_col="No").loc[:, "Nama":]
    df = pd.DataFrame(data_pelanggan)

    # mengecek data
    lgn = True
    while True:
        try:
            username = str(input("Username : "))
            password = str(input("Password: "))
        except:
            loading()
            print("\n==== Maaf Username atau Password Anda Salah! ====\n")
        else:
            aa, n_m = cek_login(username, password, df)
            if(aa == True):
                lgn = True
                break
            else:
                loading()
                print("\n==== Maaf Username atau Password Anda Salah! ====\n")
                lgn = False
                pass
    loading()
    return lgn, True, n_m


def cek_login(p, q, r):
    un = p
    pa = q
    df = r
    for i in range (1, len(df["Username"])+1):
        if((un == df["Username"][i]) and (pa == df["Password"][i])):
            nm = df["Nama"][i]
            aa = True
            break
        else:
            nm = "Not Found!"
            aa = False
    return aa, nm


def custT():
    os.system("cls")
    val = True
    print("========================")
    print("==== Pembuatan akun ====")
    print("========================")
    file = "data_pelanggan.xlsx"
    data_pelanggan = pd.read_excel(file)
    df = pd.DataFrame(data_pelanggan)

    while True:
        user = input("username : ")
        if user in list(df["Username"].values):
            print("username sudah ada")
        else:
            break
    password = input("password : ")
    nama = input("nama lengkap : ")
    alamat = input("alamat : ")
    jenis_kelamin = input("jenis kelamin : ")
    identitas = input("pilih kartu identitas (SIM/KTP/PASPOR) : ")
    no_id = input("no identitas %s : " % identitas)
    email = input("email : ")
    while validate_email(email) == False:
        email = str(input("masukkan email yang tepat : "))

    df.loc[len(df.index)] = [len(df) + 1, nama, identitas, no_id, user, password, email, alamat, jenis_kelamin]
    export = pd.ExcelWriter(file)
    df.to_excel(export, index=False)
    export.save()


    # append data ke csv atau excel


def login_berhasil():
    os.system("cls")
    print("==== Login Berhasil! ====\n")
    time.sleep(1)


def login_gagal():
    os.system("cls")
    print("==== Login Gagal! ====\n")
    time.sleep(1)


def menu_cust():
    os.system("cls")
    print("============================")
    print("==== Selamat Datang %s! ====" % username)
    print("============================")
    print("1. Penyewaan mobil")
    print("2. Pengembalian mobil")


def menu_sewa():
    os.system("cls")
    print("========================")
    print("==== Menu Persewaan ====")
    print("========================")
    # tampilkan kendaraan yang tersedia dan harga sewa nya


def menu_pengembalian():
    os.system("cls")
    print("===========================")
    print("==== Menu Pengembalian ====")
    print("===========================")


# mencari data mobil yang disewa dengan plat nomor, lalu statusnya diubah menjadi "Tersedia", dan nama penyewa diganti "-"

def login_admin():
    os.system("cls")
    pw1 = "Admin123"
    pw2 = "Admin123"
    log = True
    print("=====================")
    print("==== Login Admin ====")
    print("=====================")
    while True:
        try:
            user = str(input("Username : "))
            password = str(input("Password : "))
        except:
            loading()
            print("\n==== Maaf Username atau Password Anda Salah! ====")
        else:
            if ((user == pw1) and (password == pw2)):
                log = True
                break
            else:
                loading()
                print("\n==== Maaf Username atau Password Anda Salah! ====")
                log = False
                pass
    loading()
    return log, True


def data_kendaraan():
    os.system("cls")
    kendaraan = pd.read_excel("data_kendaraan.xlsx", sheetname="Sheet1")
    for jumlah in kendaraan:
        print("jumlah")
    # menyimpan data kendaraan di excel atau csv (sebisa mungkin excel shg menggunakan pandas sambil mempelajari pandas


def pemesanan(akun, nama):
    print("========================")
    print("==== Menu Pemesanan ====")
    print("========================")
    data_mobil = pd.read_excel("data_kendaraan.xlsx")
    df = pd.DataFrame(data_mobil)
    kolom = df.columns.tolist()
    kolom.remove("Penyewa")
    print(df.to_string(index=False, columns=kolom))
    while True:
        try:
            no_mobil = int(input("Masukkan nomor mobil yang anda pilih: "))
        except:
            print("Mohon masukkan angka")
        else:
            if no_mobil in range(1, len(df)+1):
                break
            else:
                print("Mohon masukkan angka sesuai tabel")
                pass
    index_mobil = no_mobil - 1
    sel = df["Penyewa"][index_mobil]
    sel = sel.replace("\'", "\"")
    sel_dict = json.loads(sel)
    tgl_awal = datetime.datetime.now()
    while True:
        tgl = int(input("Masukkan tanggal pengembalian(1-31): "))
        bln = int(input("Masukkan bulan pengembalian(1-12): "))
        thn = int(input("Masukkan tahun pengembalian(YYYY): "))
        if tgl in range(1, 32) and bln in range(1, 13) and thn in range(2021, 2025):
            break
        else:
            print("Mohon masukkan tanggal, bulan, dan tahun dengan benar!")
            pass

    tgl_akhir = f"{str(tgl).zfill(2)}/{str(bln).zfill(2)}/{thn}"
    sel_dict.update({akun: [tgl_awal.strftime("%d/%m/%Y"), tgl_akhir]})
    df["Penyewa"][index_mobil] = sel_dict
    print(df.to_string(index=False))
    d1, d2 = df["Penyewa"][index_mobil][akun]
    tgl1, bln1, thn1 = d1.split("/")
    d1 = date(int(thn1), int(bln1), int(tgl1))
    tgl2, bln2, thn2 = d2.split("/")
    d2 = date(int(thn2), int(bln2), int(tgl2))
    d3 = d2 - d1
    lama_hari = d3.days
    print(f"Anda akan menyewa {df['Jenis'][index_mobil]} selama {lama_hari} hari")
    while True:
        lanjut = input("Apakah anda melanjutkan ke tahap pembayaran?(Y/T): ")
        if lanjut.upper() == "T":
            del df["Penyewa"][index_mobil][akun]
            print("Silahkan melakukan input ulang")
            pemesanan(akun, nama)
        elif lanjut.upper() == "Y":
            df["Status"][index_mobil] = f"Disewakan kepada {nama}"
            export = pd.ExcelWriter("data_kendaraan.xlsx")
            df.to_excel(export, index=False)
            export.save()
            break
        else:
            print("Mohon masukkan (Y/T)")
    return True

def booking():
    os.system("cls")
    print("======================")
    print("==== Menu Booking ====")
    print("======================")
    # mencari mobil berdasarkan plat nomor, lalu status diubah menjadi disewakan pada .... hingga ....

def menu_admin():
    print("====================")
    print("==== Menu Admin ====")
    print("====================")
    print("1. Menambah armada")
    print("2. Mengurangi armada")
    print("3. Update harga sewa")
    ma = int(input("Masukkan menu yang anda pilih : "))
    return ma


def T_armada():
    print("========================")
    print("==== Tambah Armada ====")
    print("========================")
    #data_kendaraan()
    pd.options.mode.chained_assignment = None
    data = pd.read_excel("data_kendaraan.xlsx", header=0, )
    df = pd.DataFrame(data)
    print(df)

    # tambah mobil
    print("=====Masukkan data mobil baru=====")
    mob = str(input("Masukkan jenis mobil: "))
    hrg = str(input("Masukkan harga sewa mobil: "))
    thn = str(input("Masukkan tahun mobil: "))
    kap = str(input("Masukkan kapasitas penumpang mobil: "))
    no_pol= str(input("Masukkan nomor polisi mobil: "))
    stat = "Tersedia"
    mobil_baru = [mob, hrg,thn,kap,no_pol,stat]
    jlh_mbl = len(df["Harga"])
    print("Jumlah mobil saat ini", jlh_mbl)
    df.loc[jlh_mbl + 1] = mobil_baru
    print(df)
    export3 = pd.ExcelWriter("data_kendaraan.xlsx")
    df.to_excel(export3)
    export3.save()
    print(df)
    # menambahkan data mobil ke database csv


def K_armada():
    print("=======================")
    print("==== Kurangi Armada ====")
    print("=======================")
    #data_kendaraan()
    pd.options.mode.chained_assignment = None
    data = pd.read_excel("data_kendaraan.xlsx", header=0)
    df = pd.DataFrame(data)
    print(df.to_string(index=False))
    while True:
        try:
            jml = int(input("Pilih nomor kendaraan yang akan dikurangi: "))
        except:
            print("Mohon masukkan angka saja")
        else:
            break
    pd.options.mode.chained_assignment = None

    df = df.drop(jml - 1)
    df["No"] = [x for x in range(1, len(df) + 1)]
    print(df.to_string(index=False))

    hps = int(input("Masukkan nomor mobil yang akan dihapus:"))
    #df.drop([hps], axis=0, inplace=True)

    df=df.reset_index(drop=True)
    print("Data mobil terbaru:", df.to_string(index=False))
    export4 = pd.ExcelWriter("data_kendaraan.xlsx")
    df.to_excel(export4)
    export4.save()
    print(df)


def U_harga():
    print("======================")
    print("==== Update Harga ====")
    print("======================")
    pd.options.mode.chained_assignment = None
    data = pd.read_excel("data_kendaraan.xlsx", index_col="No", sheet_name="Sheet1", header=0, )
    df = pd.DataFrame(data)
    print(df)

    up = int(input("Mobil yang akan di update harga[ex:1]:"))
    # print("Berikut data mobil yang Anda sewa:")
    print(df.iloc[up - 1])
    harga_baru = str(input("Masukkan harga mobil terbaru:"))
    # ubah harga mobil
    df["Harga"][up] = harga_baru
    export5=pd.ExcelWriter("data_kendaraan.xlsx")
    df.to_excel(export5)
    export5.save()
    print(df)

def C_typo():
    print("======================")
    print("==== Correcting Typo ====")
    print("======================")
    pd.options.mode.chained_assignment = None
    data = pd.read_excel("data_kendaraan.xlsx", index_col="No", sheet_name="Sheet1", header=0, )
    df = pd.DataFrame(data)
    print(df)

    update = int(input("Mobil yang akan diubah datanya[ex:1]:"))
    print("Berikut data mobil yang ingin Anda ubah:")
    print(df.iloc[update - 1])
    jns_baru = str(input("Masukkan jenis mobil terbaru:"))
    hra_baru = str(input("Masukkan harga mobil terbaru:"))
    thn_baru = str(input("Masukkan tahun mobil terbaru:"))
    kap_baru = str(input("Masukkan kapasitas mobil terbaru:"))
    nopol_baru = str(input("Masukkan no polisi mobil terbaru:"))
    stat_baru = str(input("Masukkan status mobil terbaru:"))

    # ubah data mobil
    df["Jenis"][update] = jns_baru
    df["Harga"][update] = hra_baru
    df["Tahun"][update] = thn_baru
    df["Kapasitas"][update] =kap_baru
    df["No Polisi"][update] =nopol_baru
    df["Status"][update] =stat_baru
    export6=pd.ExcelWriter("data_kendaraan.xlsx")
    df.to_excel(export6)
    export6.save()
    print(df.to_string(index=False))



# T_armada()
# K_armada()
# U_harga()
# C_typo()

def pengembalian(akun,nama):
    print("=========================")
    print("=== Menu Pengembalian ===")
    print("=========================")
    data_mobil = pd.read_excel("data_kendaraan.xlsx")
    df = pd.DataFrame(data_mobil)
    kolom = df.columns.tolist()
    kolom.remove("Penyewa")
    print(df.to_string(index=False, columns=kolom))
    while True:
        while True:
            try:
                no_mobil = int(input("Masukkan nomor mobil yang akan anda kembalikan: "))
            except:
                print("Mohon masukkan angka")
            else:
                if no_mobil in range(1, len(df) + 1):
                    break
                else:
                    print("Mohon masukkan angka sesuai tabel")
                    pass
        index_mobil = no_mobil - 1
        if df["Status"][index_mobil] == f"Disewakan kepada {nama}":
            print("betul")
            df["Status"][index_mobil] = "Tersedia"
            sel = df["Penyewa"][index_mobil]
            sel = sel.replace("\'", "\"")
            sel_dict = json.loads(sel)
            df["Penyewa"][index_mobil] = sel_dict
            del df["Penyewa"][index_mobil][akun]
            print(df.to_string(index=False))
            export = pd.ExcelWriter("data_kendaraan.xlsx")
            df.to_excel(export, index=False)
            export.save()
            break
        else:
            print("Mohon masukkan nomor mobil yang tepat")

def lupa_pw():
    print("============================")
    print("==== Menu Lupa Password ====")
    print("============================")
    uname = str(input("Masukkan username anda : "))
    id = str(input("Masukkan no. id anda (KTP/SIM) : "))
    # cari unamenya, if id == no_id then fix pilih data dan ganti


def succ_pw():
    print("====================================")
    print("==== Password berhasil diganti! ====")
    print("====================================")
    print("\n\nTekan Enter!")


def fail_pw():
    print("===================================")
    print("==== Gagal mengganti password! ====")
    print("===================================")
    print("\n\nTekan Enter!")

def tunai():
    print()
    bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
    bayar = int(input("Masukkan jumlah uang yang dibayarkan : "))
    change = bayar - bill
    print("Anda berhasil membayar tagihan sebesar Rp %d" % bill)
    if(change == 0):
        print("terima kasih telah membayar dengan uang pas!")
    elif(change > 0):
        print("Jangan lupa ambil kembalian anda sebesar Rp %d, terima kasih!" % change)
    else:
        print("Bayar dengan jumlah uang yang sesuai!")
        pembayaran()

def nontunai():
    print("\n=== Metode bayar non tunai ===")
    print("1. Kartu Kredit")
    print("2. Kartu Debit")
    print("3. Gopay")
    print("4. OVO")
    print("5. Shopee Pay")
    print("6. Dana")
    met = int(input("Pilih nomor metode bayar yang diinginkan [1/2/3/4/5/6] : "))
    if(met == 1):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        rek = str(input("Masukkan nomor rekening anda : "))
        idkartu = str(input("Masukkan nama pemilik kartu rekening : "))
        bank = str(input("Masukkan nama bank : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui kartu kredit bank %s nomor rekening %s atas nama %s sebesar Rp %d berhasil dibayarkan!" % (bank, rek, idkartu, bill))
    elif(met == 2):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        rek = str(input("Masukkan nomor rekening anda : "))
        idkartu = str(input("Masukkan nama pemilik kartu rekening : "))
        bank = str(input("Masukkan nama bank : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui kartu debit bank %s nomor rekening %s atas nama %s sebesar Rp %d berhasil dibayarkan!" % (bank, rek, idkartu, bill))
    elif(met == 3):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        no = str(input("Masukkan nomor Gopay anda : "))
        id = str(input("Masukkan nama pemilik akun Gopay : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui Gopay %d atas nama %s sebesar Rp %d berhasil dibayarkan!" % (no, id, bill))
    elif(met == 4):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        no = str(input("Masukkan nomor OVO anda : "))
        id = str(input("Masukkan nama pemilik akun OVO : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui OVO %d atas nama %s sebesar Rp %d berhasil dibayarkan!" % (no, id, bill))
    elif(met == 5):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        no = str(input("Masukkan nomor Shopee Pay anda : "))
        id = str(input("Masukkan nama pemilik akun Shopee Pay : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui Shopee Pay %d atas nama %s sebesar Rp %d berhasil dibayarkan!" % (no, id, bill))
    elif(met == 6):
        bill = int(input("Masukkan jumlah tagihan [ex:100000] : "))
        no = str(input("Masukkan nomor Dana anda : "))
        id = str(input("Masukkan nama pemilik akun Dana : "))
        print("Tunggu sebentar pembayaran sedang diproses...")
        time.sleep(5)
        print("Pembayaran melalui Dana %d atas nama %s sebesar Rp %d berhasil dibayarkan!" % (no, id, bill))
    else:
        print("Input salah!")
        pembayaran()
        
def pembayaran():
    print("=== Pembayaran ===")
    print("1. Tunai")
    print("2. Non tunai")
    byr = int(input("Pilih metode pembayaran [1/2] : "))
    if(byr == 1):
        tunai()
    elif(byr == 2):
        nontunai()
    else:
        print("Masukkan input yang valid!")

def loading():    
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
    t = threading.Thread(target=animate)
    t.start()
    time.sleep(5)
    done = True  
   
   
def struk(a, b, c, d, e, f, g, h, i, j, k):
    nama = a
    nik = b
    kendaraan = c
    plat = d
    tanggal_pinjam = e
    tanggal_kembali = f
    jenis_pembayaran = g #DP awal / pelunasan
    metode = h #tunai/non tunai
    via = i #ovo gopay dll
    no = j #no akun
    nominal = k
    print("\tPT NGABERS BRAKTAKTAK AND FRENDS")
    print("Sewa Mobil")
    print("===========================================")
    print("%s\t\t%s" % (nama, nik))
    print("===========================================")
    print("Kendaraan\t:\t%s" % kendaraan)
    print("No Polisi\t:\t%s" % plat)
    print("Tanggal Pinjam\t:\t", tanggal_pinjam)
    print("Tanggal Kembali\t:\t", tanggal_kembali)
    print("===========================================")
    print("=============== %s ===============" % jenis_pembayaran)
    print("Dibayar dengan\t:\t%s" % metode)
    if(metode == "Non Tunai"):
        print("Via\t:\t%s" % via)
        print("Nomor akun\t:\t%s" % no)
    print("Nominal dibayarkan\t:\t%s" % nominal)


def cust_byr(i, j, k, l, m, n):
    jns, lama, hrg, denda, tsewa, tbalik = i, j, k, l, m, n
    asuransi = 0.1*hrg
    total = 0
    if(jns == "DP Awal"):
        total = (asuransi + (0.5*hrg))
    elif(jns == "Pelunasan"):
        total = (0.5*hrg) + denda
    return total, jns, tsewa, tbalik
    

#Bagian Program Utama   
lagi = "Y"  
while (lagi == "Y"): 
    os.system("cls")
    judul()
    ut = 0
    ut = menu_utama()
    if(ut == 1):
        stat_akun = login_cust()
        if(stat_akun.upper() == "Y"):
            akunY, tr, user = custY()
            if(akunY == True):
                login_berhasil()
                chs = menu_cust(user)
                if(chs == 1):
                    menu_sewa()
                elif(chs == 2):
                    menu_pengembalian()
                else:
                    print("Input anda salah!")                  
        elif(stat_akun.upper() == "T"):
            custT()
        else:
            print("Input anda salah!")
    elif(ut == 2):
        log, st = login_admin()
        if(log == True):
            login_berhasil()
            ma = menu_admin()
            if(ma == 1):
                T_armada() 
            elif(ma == 2):
                K_armada()
            elif(ma == 3):
                U_harga()
            else:
                print("Input anda salah!")
                menu_admin()
        else:
            raise Exception("==== Maaf Username atau Password Anda Salah! ====")
    elif(ut == 3):
        print("Terima kasih telah menggunakan program kami, sampai jumpa kembali!")
        print("Program ditutup...")
        sys.exit()
    else:
        print("Input anda salah!")
    print("\n[  Sampai jumpa kembali!  ]\n")
