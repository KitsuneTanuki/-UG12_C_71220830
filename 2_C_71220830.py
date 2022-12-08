raw = input("Masukkan angka : ")
count = input("Masukkan angka yg dihitung : ")

def penghitung(raw,count):
    hitungan = 0
    for i in raw:
        if (i == count):
            hitungan = hitungan + 1
    return hitungan

print('angka',count,'muncul sebanyak',penghitung(raw,count),'kali.')
