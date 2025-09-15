print("=======Tebak angka========")
import random
def tebak_angka():
    tebak_angka = random.randint(1, 10)
    kesempatan = 3

    print("saya telah memilih angka antara 1-10")
    print ("coba tebak angka tersebut, kamu mempunyai 3 kesempatan")

    while kesempatan > 0:
            tebak = int(input("masukkan angka: "))
            if tebak == tebak_angka:
                    print("Tebakan benar")
                    break
            elif tebak < tebak_angka:
                    kesempatan -= 1
                    print(f"angka terlalu kecil, kesempatan tinggal {kesempatan}")
            else:
                kesempatan -= 1
                print(f"angka terlalu besar, kesempatan tinggal {kesempatan}")
            if kesempatan  == 0:
                print(f"kesempatan habis")
tebak_angka()