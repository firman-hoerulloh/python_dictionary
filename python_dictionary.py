# deklarasi fungsi
def baca_data(filename):
    #fungsi digunakan untuk membaca file teks &
    # diubah ke tipe data terstruktur
    file = open("mobil.txt", "r") 
                                  

    data_mobil = {}   #key = jenis mobil, value = list(warna,bbm,Stok)

    teks = file.readline().replace("\n","")
    
    while teks != "" :  #teks bukan EOF
        list_kata = teks.split("#")  #indeks 0=jenis mobil, 1=warna, 2=bahan bakar, 3=stok
        
        if list_kata[0] in data_mobil:
            data_mobil[list_kata[0]].append(list_kata[1], list_kata[2], int(list_kata[3]))
        else :
            data_mobil[list_kata[0]] = [ list_kata[1],list_kata[2], int(list_kata[3])]

        teks = file.readline().replace("\n","")

    file.close()
    return data_mobil



def report(mobil):
    # fungsi untuk mencari stok tersedikit & terbanyak
    stocks = []
    
    for data in mobil.values() :
        stocks.append(data[2])    #indeks values 0=warna, 1=bahan bakar, 2=stok
        

    val_min, idx_min = min((val_min, idx_min) for (idx_min, val_min) in enumerate(stocks))
    
    val_max, idx_max = max((val_max, idx_max) for (idx_max, val_max) in enumerate(stocks))
    
    keys_list = list(mobil)
    
    print("Stok tersedikit: \n", keys_list[idx_min],"=",val_min,"stok")
    print("Stok terbanyak: \n", keys_list[idx_max],"=",val_max,"stok")
    

def bahan_bakar(mobil, model):
    #fungsi untuk mencari bahan bakar jenis mobil tertentu
    bbm = ""
    
    for key,value in mobil.items() :
        if(key == model):
            bbm = value
        
    
    if bbm == "" :
        return "Maaf jenis mobil tidak terdaftar"
    else :
        return bbm[1]  #indeks values 0=warna, 1=bahan bakar, 2=stok


#main program
file = "mobil.txt"
mobil = open(file, 'r')
print(mobil.read())
print("")
data_mobil = baca_data(file)
print(data_mobil)
print("")
report(data_mobil)
print("")
jenis_mobil = input("Masukkan jenis mobil:\n")
print("Bahan bakar:\n", bahan_bakar(data_mobil, jenis_mobil))

