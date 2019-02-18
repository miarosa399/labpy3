print ('=== LATIHAN1 ===')
print ('Tampilkan Bilangan Acak Lebih Kecil dari 0,5')

import random
jumlah = int(input('masukan jumlah n: '))
print()
for i in range (jumlah):
    i=random.uniform(0.0,0.5)
    print(i)
print()
