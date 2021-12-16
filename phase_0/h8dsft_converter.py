#mengkonversi nilai suhu
def suhu_c(s):#fungsi untuk mengubah dari celcius ke kelvin
  c_to_k=s + 273.15
  print(c_to_k,"Kelvin")#cetak hasil konversi celcius ke kelvin
def suhu_k(s):#fungsi untuk mengubah dari kelvin ke celcius
  k_to_c = s-273.15
  print(k_to_c,"Celcius")#cetak hasil konversi dari kelvin ke celcius
def suhu_f(s):#fungsi untuk mengubah celcius ke farenheit
  c_to_f=(s*9/5)+32
  print(c_to_f,"Farenheit")#cetak hasil konversi dari celcius ke farenheit
def suhu_fk(s):#fungsi untuk mengubah dari kelvin ke farenheit
  k_to_f=(s-273.15)*9/5+32
  print(k_to_f,"Farenheit")#cetak hasil konversi dari kelvin ke farenheit
#proses input
celcius_kelvin=int(input("masukan angka dalam celcius: "))
suhu_c(celcius_kelvin)

kelvin_celcius=float(input("Masukan angka dalam Kelvin: "))
suhu_k(kelvin_celcius)

celcius_farenheit=float(input("Masukan angka dalam Celcius:"))
suhu_f(celcius_farenheit)

kelvin_farenheit=float(input("Masukan angka dalam Kelvin:"))
suhu_fk(kelvin_farenheit)