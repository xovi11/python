print("======= Konversi Nilai======")

while True:
    x = int(input("masukkan nilai: "))

    if x >= 85:
        print("nilai A")
    elif x >= 70:
        print("nilai B")
    elif x >= 60:
        print("nilai C")
    else:
        print("nilai D") 

    lanjut = input("apakah anda ingin lanjut? y/n")
    if lanjut.lower() != "y":
        print("Terimakasih")
        break
        