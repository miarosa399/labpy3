print ("=== LATIHAN2 ===")
print ('Menampilkan Bilangan Terbesar dan Berhenti Ketika Input Angka 0')

a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
g = 1
while g != 0:
        a = int(input("Masukan Angka: "))
        b = int(input("Masukan Angka: "))
        c = int(input("Masukan Angka: "))
        d = int(input("Masukan Angka: "))
        e = int(input("Masukan Angka: "))
        f = int(input("Masukan Angka: "))
        g = int(input("Masukan Angka: "))

        if a>b and a>c and a>d and a>e and a>f and a>g:
            print("Bilangan terbesar adalah: ",a)
        elif b>a and b>c and b>d and b>e and b>f and b>g:
            print("Bilangan terbesar adalah: ",b)
        elif c>b and c>a and c>d and c>e and c>f and c>g:
            print("Bilangan terbesar adalah: ",c)
        elif d>b and d>c and d>a and d>e and d>f and d>g:
            print("Bilangan terbesar adalah: ",d)
        elif e>b and e>c and e>d and e>a and e>f and e>g:
            print("Bilangan terbesar adalah: ",e)
        elif f>b and f>c and f>d and f>e and f>a and f>g:
            print("Bilangan terbesar adalah: ",f)
        else:
            print("Bilangan terbesar adalah: ",g)
