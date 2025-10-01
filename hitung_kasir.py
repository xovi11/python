print("===================+++++==================")
print("                   KASIR                  ")
print("===================+++++==================")

total_blnj = 0
list_brg = {}


def tbh_barang():
    nama_brg = input("masukkan nama barang: ")
    hrg_brg = int(input("masukkan harga: "))
    jml_brg = int(input("masukkan jumlah: "))

    total_hrg  = hrg_brg * jml_brg
    list_brg[nama_brg] = {"hrg_brg": hrg_brg, "jml_brg": jml_brg, "total_brg": total_hrg}
    global total_blnj
    total_blnj += total_hrg

def tamp_list():
    print("list barang")
    for nama_brg , detail in list_brg.items():
        print(f"{nama_brg}: {detail['jml_brg']} x {detail['hrg_brg']} = {detail['total_brg']}")


def hitung_total_blnj():
    return total_blnj

def pembayaran():
    total_blnj = hitung_total_blnj()
    print(f"total belanja: {total_blnj}")
    bayar = int(input("masukkan jumlah pembayaran : "))
    kembali = bayar - total_blnj
    print(f"Kembalian : {kembali}")

def hapus_brg(nama_brg):
    if nama_brg in list_brg:
        del list_brg[nama_brg]
        print(f"barang {nama_brg} telah dihapus")
    else:
        print("barang tidak ditemukan!")
    
def update(nama_brg, jmlh_baru):
    if nama_brg in list_brg:
        harga = list_brg[nama_brg]["hrg_brg"]
        list_brg[nama_brg]["jml_brg"] = jmlh_baru
        list_brg[nama_brg]["total_brg"] = harga * jmlh_baru
        print(f"{nama_brg} telah diupdate jumlahnya menjadi {jmlh_baru}")
    else:
        print("barang tidak ditemukan")

def struk():
    print("===== STRUK BELANJA =====")
    tamp_list()
    print(f"Total Belanja: {hitung_total_blnj()}")
    print("=========================")

def diskon(total_blnj):
    if total_blnj > 50000:
        return total_blnj * 0.1
    if total_blnj > 10000:
        return total_blnj * 0.2
    if total_blnj > 20000:
        return total_blnj * 0.3
    return 0

def cari_brg(nama_brg):
    if nama_brg in list_brg:
        return list_brg[nama_brg]
    else:
        return None


while True:
    print("1. Tampilkan list barang")
    print("2. Tambah barang")
    print("3. Total Belanja")
    print("4. Pembayaran ")
    print("5. Update")
    print("6. hapus")
    print("7. cetak struk")
    print("8. Diskon")
    print("9. Cari barang")
    print("10. Keluar")
    pilihan = int(input("masukkan pilihan: "))
    if pilihan == 1:
        tamp_list()
    elif pilihan == 2:
        tbh_barang()
    elif pilihan == 3:
        hitung_total_blnj()
        print(f"total belanja {hitung_total_blnj()}")
    elif pilihan == 4:
        pembayaran()
    elif pilihan == 5:
        nama_brg = input("masukkan baranag yang ingin diupdate: ")
        jmlh_baru = int(input("masukkian jumlah barang: "))
        update(nama_brg, jmlh_baru)
    elif pilihan == 6:
        nama_brg = input("masukkan nama barang: ")
        hapus_brg(nama_brg)
    elif pilihan == 7:
        struk()
    elif pilihan == 8:
        diskon(total_blnj)
        print(f"diskon yang didapat: {diskon(total_blnj)}")
    elif pilihan == 9:
        nama_brg = input("masukkan nama barang: ")
        print(f"nama barang {cari_brg(nama_brg)}")
    elif pilihan == 10:
        break
    else:
        print("parameter tidak valid!")

    lanjut = input("apakah ingin lanjut: y/n: ")
    if lanjut != "y":
        print("terimakasih")
        break