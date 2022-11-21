listPasien = [
    {
        'nama': 'Firza',
        'alamat': 'Surabaya',
        'tanggalLahir': '20 09 1995',
        'jenisKelamin' : 'L',
        'KTP' : '9500950095009500',
        'keluhan' : 'Flu'

    },
    {
         'nama': 'Ahmad',
        'alamat': 'Semarang',
        'tanggalLahir': '30 01 1997',
        'jenisKelamin' : 'L',
        'KTP' : '1200120012001200',
        'keluhan' : 'Demam'
    },
    {
         'nama': 'Linda',
        'alamat': 'Jakarta',
        'tanggalLahir': '13 12 1994',
        'jenisKelamin' : 'P',
        'KTP' : '7890789078907890',
        'keluhan' : 'Pusing'
    }
]


def menampilkanDaftarPasien() :
  if (len(listPasien)>0) :
    print('''
Data Seluruh Pasien\n
---------------------
    ''')
    print('Index\t|Nama\t|alamat\t\t|tanggal lahir\t|jns kel\t|KTP atau ID\t\t|keluhan' )
    for i in range(len(listPasien)) :
        print('{}\t| {}\t|{}\t|{}\t|{}\t\t|{}\t|{}'.format(i,listPasien[i]['nama'],listPasien[i]['alamat'],listPasien[i]['tanggalLahir'],listPasien[i]['jenisKelamin'],listPasien[i]['KTP'],listPasien[i]['keluhan']))
      
  elif (len(listPasien)==0):
    print("ALERT! data masih kosong")

  questionKeMenu()
  

def mencariDataPasien():
  
    pilihanField = input('''
        
Cari berdasarkan field apa?
Menu :
1. Nama
2. Alamat
3. Tanggal Lahir
4. Jenis Kelamin
5. KTP
6. Keluhan
Pilih menu yang ingin dijalankan (1/2/3/4/5/6):

''')
    if (pilihanField == '1'):
            pilihanField = 'nama'
    elif (pilihanField == '2'):
            pilihanField = 'alamat'
    elif (pilihanField == '3'):
            pilihanField = 'tanggalLahir'
    elif (pilihanField == '4'):
            pilihanField = 'jenisKelamin'
    elif (pilihanField == '5'):
            pilihanField = 'KTP'
    elif (pilihanField == '6'):
            pilihanField = 'keluhan'
    else:
      print("ALERT! input tidak benar")
      mengubahDataPasien()

    masukanUser = input("Masukan kata kunci pencarian :")

    for i in range (len(listPasien)):
      if masukanUser == listPasien[i][pilihanField]:
            print ("")
            print ("Data yang ingin anda cari adalah sebagai berikut:")
            print('{}\t| {}\t|{}\t|{}\t|{}\t\t|{}\t|{}'.format(i,listPasien[i]['nama'],listPasien[i]['alamat'],listPasien[i]['tanggalLahir'],listPasien[i]['jenisKelamin'],listPasien[i]['KTP'],listPasien[i]['keluhan']))
            questionKeMenu()
      
    else:
        print("ALERT! tidak ada data dengan kata kunci tersebut")
        mencariDataPasien()


def menambahDataPasien() :
    namaPasien = input('Masukkan Nama pasien : ')
    alamatPasien = input('Masukan alamat pasien : ')
    tanggalLahir = input('Masukan tanggal lahir pasien (DDMMYYYY) : ')
    jenisKelamin = input('Masukan jenis kelamin pasien (L/P) : ')
    KTP = input('masukan ID KTP pasien : ')
    keluhan = input('masukan keluhan pasien  :')
    questionSimpan = input ("Anda yakin menyimpan data ini? (Y/N): ")
    if(questionSimpan == 'Y' or questionSimpan == 'y') :
        for i in range (len(listPasien)):
            if KTP == listPasien[i]['KTP']:
                print("ALERT! data KTP sudah ada, ulangi proses!")
                menambahDataPasien()
                break

        else:
          listPasien.append({
              'nama': namaPasien,
              'alamat': alamatPasien,
              'tanggalLahir': tanggalLahir,
              'jenisKelamin' : jenisKelamin,
              'KTP': KTP,
              'keluhan': keluhan,
                })
          print("ALERT! Data tersimpan")
          questionLihatData()
              
              
        
    elif(questionSimpan == 'N' or questionSimpan == 'n') :
        print("ALERT! Data tidak tersimpan")
        menambahDataPasien()    


def menghapusDataPasien() :
    deletion = []
    inputKTP = input('masukan ID/KTP pasien yang akan dihapus: ')
    questionHapus = input ("Anda yakin menghapus data ini? (Y / N): ")
    if(questionHapus == 'Y' or questionHapus == 'y') :
      for i in range (len(listPasien)):
        if inputKTP == listPasien[i]['KTP']:       
            deletion.append(i)    
      for key in deletion:
        del listPasien[key]      
        print("ALERT! data berhasil terhapus")
        questionLihatData()
      else:
            print("ALERT! data yang anda maksud tidak ada")
            questionKeMenu()    
        
    elif(questionHapus == 'N' or questionHapus == 'n') :
            print("ALERT! data tidak terhapus")
            menghapusDataPasien()

def mengubahDataPasien() :
    inputKTP = input('masukan ID/KTP pasien yang akan diubah: ')
    change = []
    for i in range (len(listPasien)):
        if inputKTP == listPasien[i]['KTP']:
            change.append(i)
            print ("")
            print ("Data yang ingin anda ubah adalah sebagai berikut:")
            print('Index\t|Nama\t|alamat\|tgl lhr\t|jns kel\t|KTP\t|keluhan' )
            print('{}\t| {}\t|{}\t|{}\t|{}\t\t|{}\t|{}'.format(i,listPasien[i]['nama'],listPasien[i]['alamat'],listPasien[i]['tanggalLahir'],listPasien[i]['jenisKelamin'],listPasien[i]['KTP'],listPasien[i]['keluhan']))

            pilihanField = input('''
        
Ubah berdasarkan field apa?
Menu :
1. Nama
2. Alamat
3. Tanggal Lahir
4. Jenis Kelamin
5. KTP
6. Keluhan
Pilih menu yang ingin dijalankan (1/2/3/4/5/6):''')
            if (pilihanField == '1'):
                pilihanField = 'nama'
            elif (pilihanField == '2'):
                pilihanField = 'alamat'
            elif (pilihanField == '3'):
                pilihanField = 'tanggalLahir'
            elif (pilihanField == '4'):
                pilihanField = 'jenisKelamin'
            elif (pilihanField == '5'):
                pilihanField = 'KTP'
            elif (pilihanField == '6'):
                pilihanField = 'keluhan'
            else:
                print("ALERT! Input salah")   
            inputUbahField = input("Input data yang baru: ")
    for key in change:
            questionUbah = input("Anda yakin mengubah data ini? (Y/N) ")
            if(questionUbah == 'Y' or questionUbah == 'y') :    
                listPasien[key][pilihanField] = inputUbahField
                print ("ALERT! Data berhasil diubah")
                questionLihatData()
                break
            elif(questionUbah == 'N' or questionUbah == 'n') :
                print('''ALERT! Data belum diubah
            ''')
                mengubahDataPasien()
                break
                
            
    else:
        print("ALERT! data yang anda maksud tidak ada")
        mengubahDataPasien()




def menampilkanMenu() :
    pilihanMenu = input('''
____________________________________________
Menu Aplikasi RS. Bunda Ceria
____________________________________________

Menu :
1. Tampilkan / Cari Data Pasien
2. Tambah Data Pasien
3. Ubah Data Pasien
4. Hapus Data Pasien
5. Keluar

Pilih menu yang ingin dijalankan (1/2/3/4/5) :
_____________________________________________
        
''')

    if(pilihanMenu == '1') :
        print('1. Sub Menu 1 Tampilkan Semua Data')
        print('2. Sub Menu 2 Cari Data')
        print('3. Kembali ke Menu')
        subMenu1= input("pilih sub menu:  ")
        if (subMenu1 == '1'):
            menampilkanDaftarPasien()
        elif (subMenu1 == '2'):
            mencariDataPasien()
        elif (subMenu1 == '3'):
            menampilkanMenu()       
    elif(pilihanMenu == '2') :
        print('1. Lanjutkan> Tambahkan Data Pasien')
        print('2. Kembali ke Menu')
        subMenu1= input("pilih sub menu (1/2):  ")
        if (subMenu1 == '1'):
            menambahDataPasien()
        elif (subMenu1 == '2'):
            menampilkanMenu()
    elif(pilihanMenu == '3') :
        print('1. Lanjutkan> Ubah Data Pasien')
        print('2. Kembali ke Menu')
        subMenu1= input("pilih sub menu (1/2):  ")
        if (subMenu1 == '1'):
            mengubahDataPasien()
        elif (subMenu1 == '2'):
            menampilkanMenu()
        
    elif(pilihanMenu == '4') :
        print('1. Lanjutkan> Hapus Data Pasien')
        print('2. Kembali ke Menu')
        subMenu1= input("pilih sub menu (1/2):  ")
        if (subMenu1 == '1'):
            menghapusDataPasien()
        elif (subMenu1 == '2'):
            menampilkanMenu()
        
    elif(pilihanMenu == '5') :
        exit("aplikasi tertutup")
    else:
        print("ALERT! input yang anda masukan salah, masukan 1/2/3/4/5!")

def questionKeMenu() :
  question = input('''
Kembali ke menu? (Y/N)
''')
  if(question == 'Y' or question == 'y') :
        menampilkanMenu()
  elif(question == 'N' or question == 'n') :
        exit('aplikasi ditutup')

def questionLihatData() :
  questionLihatData = input('''
Lihat hasil? (Y/N)
''')
  if(questionLihatData == 'Y' or questionLihatData == 'y') :
        menampilkanDaftarPasien()
  elif(questionLihatData == 'N' or questionLihatData == 'n') :
        menampilkanMenu()
        

while True :
  menampilkanMenu()
