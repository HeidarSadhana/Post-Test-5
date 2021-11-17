from itertools import islice
import os
import random

weekdays = ['senin','selasa','rabu','kamis','jumat']
weekend = ['sabtu','minggu']
week = [weekdays]+[weekend]
jenis_hari = random.choice(week)
hari = random.choice(jenis_hari)

keranjang_minuman = []
keranjang_makanan = []
listmenu = {
    'ListMinum' : {
        'AQIA':8000,
        'Le Mine':6000,
        'Soda Bahagia':12000,
        'Ponari Sweet':10000,
        'Es Teh Panas':10000,}
    ,'ListMakan' : {
        'Indomay Sedap Ayam Geprek':10000,
        'Roti Rebus Asam Manis':13000,
        'Nasi Kuning Binjai':14000,
        'Kentang Bakar Lima Jari':8000,
        'Krebi Peti Saos Tiram ':17000,}
    }  

CaraBayar = ['Tunai','E-Money'] 
tambah = lambda a, b, c: {key: value for key, value in (list(a.items())[:c] + list(b.items()) + list(a.items())[c:])}

class menu:
    def utama():
        os.system('cls')
        print('                  CAFE CERIA                  ')
        print('==============================================')
        print('1. Lihat Minuman')
        print('2. Lihat Makanan')
        print('3. Lihat Keranjang')
        print('4. Lihat Aturan Diskon')
        print('5. Edit Menu')
        print('0. Keluar')
        print('==============================================')
        print('hari:',hari)
        keranjang = len(keranjang_makanan)+len(keranjang_minuman)
        print('keranjang:', keranjang)

    def diskon():
        os.system('cls')
        print('LIST DISKON')
        print('==============================================')
        print('a. Setiap Pembelian Lebih dari 3 Minuman (10%)')
        print('b. Setiap Pembelian Lebih dari 2 Makanan (5%)')
        print('c. Setiap Pembelian di hari Senin-Jum\'at (10%)')
        print('d. Setiap Pembelian di hari Sabtu-Minggu (5%)')
        print('e. Setiap Pembayaran menggunakan E-money (5%)')
        print('==============================================')
        print('0. Kembali')

    def minuman():
        os.system('cls')
        no = 1
        print('            MINUMAN            ')
        print('===============================')
        for nama,harga in listmenu['ListMinum'].items():
            print("{}. {} \n= Rp.{}".format(no,nama,harga))
            no+=1
        print('===============================')
        
    def makanan():
        os.system('cls')
        no=1
        print('            MAKANAN           ')
        print('==============================')
        menu_makan = listmenu['ListMakan']
        for makan in menu_makan:
            print("{}. {} \n= Rp.{}".format(no,makan,menu_makan[makan]))
            no+=1         
        print('==============================')
        
    def keranjang():
        os.system('cls')
        global jumlah_makanan
        jumlah_makanan={} 
        for makanan in keranjang_makanan:
            jumlah_makanan[makanan]=keranjang_makanan.count(makanan)
        harga.makanan()
        global jumlah_minuman
        jumlah_minuman={} 
        for minuman in keranjang_minuman:
            jumlah_minuman[minuman]=keranjang_minuman.count(minuman)
        harga.minuman()
        if keranjang_minuman==[] and keranjang_makanan==[]:
            print('Belum Ada Pesanan')
        print('==============================')
        print('1. Bayar Tunai')
        print('2. Bayar E-money')
        print('3. Reset Keranjang')
        print('0. Kembali')
        print('==============================')

    def edit():
        print('Edit Menu')
        print('==============================')
        print('1. Edit Minuman')
        print('2. Edit Makanan')
        print('0. Kembali')
        print('==============================')

    def keluar():
        os.system('cls')
        print('Keluar...')
        SystemExit
    
class harga:
    def minuman():
        global harga_minum
        harga_minum = []
        for minum in listmenu['ListMinum']:
            if minum in jumlah_minuman:
                print('{} ({})'.format(minum,jumlah_minuman[minum]))
                harga = listmenu['ListMinum'][minum]*int(jumlah_minuman[minum])
                harga_minum.append(harga)

    def makanan():
        global harga_makan
        harga_makan = []
        for makan in listmenu['ListMakan']:
            if makan in jumlah_makanan:
                print('{} ({})'.format(makan,jumlah_makanan[makan]))
                harga = listmenu['ListMakan'][makan]*int(jumlah_makanan[makan])
                harga_makan.append(harga)
            
class interaksi:
    def utama():
        menu.utama()    
        pilih_menu = input("> ")
        if pilih_menu == "1":
            interaksi.minuman()
        elif pilih_menu == "2":
            interaksi.makanan()
        elif pilih_menu == "3":
            interaksi.keranjang()
        elif pilih_menu == "4":
            interaksi.diskon()
        elif pilih_menu == "5":
            interaksi.edit()
        elif pilih_menu == "0":
            menu.keluar()
        else:
            interaksi.utama()
    
    def minuman():
        menu.minuman()
        print('0. Kembali')
        pilih_minum = input("> ")
        for minum in listmenu['ListMinum']:
            minuman = list(listmenu['ListMinum'].keys()).index(minum)+1
            if pilih_minum == str(minuman):
                beli = ''
                while beli not in ['y','n']:
                    os.system('cls')
                    beli = input('Beli {}? y/n \n'.format(minum))
                    if beli == "y":
                        print('------------------------------')
                        jumlah = int(input("Jumlah: "))
                        for i in range(jumlah):
                            keranjang_minuman.append(minum)
                            i+=1
                        input("Kembali...")
                        break
                    else:
                        break
        if pilih_minum == "0":
            interaksi.utama()
        else:
            interaksi.minuman()

    def makanan():
        menu.makanan()
        print('0. Kembali')
        pilih_makan = input ("> ")
        for makan in listmenu['ListMakan']:
            makanan = list(listmenu['ListMakan'].keys()).index(makan)+1
            if pilih_makan == str(makanan):
                beli = ''
                while beli not in ['y','n']:
                    os.system('cls')
                    beli = input('Beli {}? y/n \n'.format(makan))
                    if beli == "y":
                        print('------------------------------')
                        jumlah = int(input("Jumlah: "))
                        for i in range(jumlah):
                            keranjang_makanan.append(makan)
                            i+=1
                        input("Kembali...")
                        break
                    else:
                        break
        if pilih_makan == '0':
            interaksi.utama()          
        else:
            interaksi.makanan()
    
    def diskon():
        menu.diskon()
        pilih = input("> ")
        if pilih == "0":
            interaksi.utama()
        else:
            interaksi.diskon()

    def keranjang():
        menu.keranjang()
        pilih = input("> ")
        global cara_bayar
        if pilih == "1":
            cara_bayar = CaraBayar.index('Tunai')
            membayar()
            interaksi.bayar()
        elif pilih == "2":
            cara_bayar = CaraBayar.index('E-Money')
            membayar()
            interaksi.bayar()
        elif pilih == "3":
            keranjang_makanan.clear()
            keranjang_minuman.clear()
            interaksi.keranjang()
        elif pilih == "0":
            interaksi.utama()
        else:
            interaksi.keranjang()

    def bayar():
        pilih = input("> ")
        if pilih == "1":
            if keranjang_makanan==[] and keranjang_minuman==[]:
                os.system('cls')
                print("Anda Belum Memesan Apapun")
                input("\nKembali Ke Menu Utama")
                interaksi.utama()
            else:
                os.system('cls')
                keranjang_makanan.clear()
                keranjang_minuman.clear()
                print("Terima Kasih Sudah Membeli")
                input("\nKembali Ke Menu Utama")
                interaksi.utama()
        elif pilih == "0":
            interaksi.keranjang()
        else:
            interaksi.bayar()
    
    def edit():
        os.system('cls')
        menu.edit()
        pilih = input('> ')
        if pilih == '1':
            interaksi.edit_minum()
        elif pilih == '2':
            interaksi.edit_makan()
        elif pilih == "0":
            interaksi.utama()
        else:
            interaksi.edit()

    def edit_minum():
        os.system('cls')
        print('Edit Menu (Minuman)')
        print('==============================')
        print('1. Tambah Minuman')
        print('2. Ubah Minuman')
        print('3. Hapus Minuman')
        print('0. Kembali')
        print('==============================')
        pilih_edit = input("> ")

        if pilih_edit == '1':
            os.system('cls')
            urutan = int(input('Tambah Minuman Di Urutan Ke - '))
            if urutan > len(listmenu['ListMinum'])+1:
                print('Urutannya Kejauhan Bro')
                input('Kembali...')
                interaksi.edit()
            elif urutan == len(listmenu['ListMinum'])+1:
                nama = input('Nama: ')                
                if nama in listmenu['ListMinum']:
                    print('Minuman Sudah Ada')
                    input('Kembali...')
                    interaksi.edit()
                else:
                    harga = int(input('Harga: '))
                    listmenu['ListMinum'][nama]=harga
                    input('Kembali...')
                    interaksi.edit()
            else:
                nama = input('Nama: ')                
                if nama in listmenu['ListMinum']:
                    print('Minuman Sudah Ada')
                    input('Kembali...')
                    interaksi.edit()
                else:
                    harga = int(input('Harga: '))
                    listmenu["ListMinum"] = tambah(listmenu["ListMakan"],{nama:harga},urutan-1)
                    input('Kembali...')
                    interaksi.edit()

        elif pilih_edit == '2':
            keranjang_minuman.clear()
            menu.minuman()
            print('0. Kembali')
            pilih_minum = input('No. Minuman Yang Ingin Diubah : ')
            while pilih_minum.isdigit():
                for minum in listmenu['ListMinum']:
                    x = list(listmenu['ListMinum'].keys()).index(minum)
                    if int(pilih_minum) == x+1:
                        os.system('cls')
                        nama_baru = input('Nama Baru: ')
                        harga_baru = int(input('Harga : '))
                        del listmenu['ListMinum'][next(islice(listmenu["ListMinum"],x,None))]
                        listmenu["ListMinum"] = tambah(listmenu["ListMinum"],{nama_baru:harga_baru},x)
                        break
                    if pilih_minum == '0':
                        break
                break
            else:
                interaksi.edit_minum()

        elif pilih_edit == '3':
            keranjang_minuman.clear()
            menu.minuman()
            print('0. Kembali')
            pilih_minum = input('No. Minuman Yang Ingin Dihapus : ')
            if pilih_minum.isdigit():
                for minum in listmenu['ListMinum']:
                    x = list(listmenu['ListMinum'].keys())
                    if int(pilih_minum) == x.index(minum)+1:
                        os.system('cls')
                        print('Yakin Ingin Menghapus {}? y/n'.format(minum))
                        keyakinan = ''
                        while keyakinan not in ['y','n']:
                            keyakinan = input('> ')
                            if keyakinan == 'y':
                                harga = listmenu['ListMinum'].pop(minum)
                                input('Mantap! {} dengan harga {} Sudah Dihapus'.format(minum,harga))
                                break
                            else:
                                break
                        break
                    elif pilih_minum == '0':
                        break
            else:
                interaksi.edit_minum()  
        elif pilih_edit == '0':
            interaksi.edit() 
        else:
            interaksi.edit_minum()

    def edit_makan():
        os.system('cls')
        print('Edit Menu (Makanan)')
        print('==============================')
        print('1. Tambah Makanan')
        print('2. Ubah Makanan')
        print('3. Hapus Makanan')
        print('0. Kembali')
        print('==============================')
        pilih_edit = input("> ")
        if pilih_edit == '1':
            os.system('cls')
            urutan = int(input('Tambah Makanan Di Urutan Ke - '))
            if urutan > len(listmenu['ListMakan'])+1:
                print('Urutannya Kejauhan Bro')
                input('Kembali...')
                interaksi.edit()
            elif urutan == len(listmenu['ListMakan'])+1:
                nama = input('Nama: ')                
                if nama in listmenu['ListMakan']:
                    print('Makanan Sudah Ada')
                    input('Kembali...')
                    interaksi.edit()
                else:
                    harga = int(input('Harga: '))
                    listmenu['ListMakan'][nama]=harga
                    input('Kembali...')
                    interaksi.edit()
            else:
                nama = input('Nama: ')                
                if nama in listmenu['ListMakan']:
                    print('Makanan Sudah Ada')
                    input('Kembali...')
                    interaksi.edit()
                else:
                    harga = int(input('Harga: '))
                    listmenu["ListMakan"] = tambah(listmenu["ListMakan"],{nama:harga},urutan-1)
                    input('Kembali...')
                    interaksi.edit()

        elif pilih_edit == '2':
            keranjang_makanan.clear()
            menu.makanan()
            print('0. Kembali')
            pilih_makan = input('No. Makanan Yang Ingin Diubah : ')
            while pilih_makan.isdigit():
                for makan in listmenu['ListMakan']:
                    x = list(listmenu['ListMakan'].keys()).index(makan)
                    if int(pilih_makan) == x+1:
                        os.system('cls')
                        nama_baru = input('Nama Baru: ')
                        harga_baru = int(input('Harga : '))
                        del listmenu['ListMakan'][next(islice(listmenu["ListMakan"],x,None))]
                        listmenu["ListMakan"] = tambah(listmenu["ListMakan"],{nama_baru:harga_baru},x)
                        break
                    if pilih_makan == '0':
                        break
                break
            interaksi.edit_makan()

        elif pilih_edit == '3':
            keranjang_makanan.clear()
            menu.makanan()
            print('0. Kembali')
            pilih_makan = input('No. Makanan Yang Ingin Dihapus : ')
            if pilih_makan.isdigit():
                for makan in listmenu['ListMakan']:
                    x = list(listmenu['ListMakan'].keys())
                    if int(pilih_makan) == x.index(makan)+1:
                        os.system('cls')
                        print('Yakin Ingin Menghapus {}? y/n'.format(makan))
                        keyakinan = ''
                        while keyakinan not in ['y','n']:
                            keyakinan = input('> ')
                            if keyakinan == 'y':
                                harga = listmenu['ListMakan'].pop(makan)
                                input('Mantap! {} dengan harga {} Sudah Dihapus'.format(makan,harga))
                                break
                            else:
                                break
                        break
                    elif pilih_makan == '0':
                        break
                    else:
                        break
            else:
                interaksi.edit_makan()
        elif pilih_edit == '0':
            interaksi.edit()
        else:
            interaksi.edit_makan()

def membayar():
    os.system('cls')
    print('HARGA')
    print('-----------------------')
    total_harga=0
    for i in harga_minum:
        total_harga+=i
        print('Rp.',i)
    for i in harga_makan:
        total_harga+=i
        print('Rp.',i)     
    print('----------------------- (+)')
    print('Total Harga: Rp.',total_harga)
    print('-----------------------')
    print('DISKON')
    print('-----------------------')
    hitung_diskon()
    mengdiskon = total_harga * diskon/100
    harga_akhir = total_harga - mengdiskon
    print(f'Harga Akhir: Rp.', round(harga_akhir))
    print('-----------------------')
    print('1. Bayar')
    print('0. Kembali')

def hitung_diskon():
    global diskon
    diskon = 0
    if cara_bayar == 1:
        diskon+=5
        print('+ Diskon E-Money (5%)')
    if len(keranjang_minuman)>=3:
        print('+ Diskon 3 Minuman (10%)')
        diskon+=10
    if len(keranjang_makanan)>=2:
        print('+ Diskon 2 Makanan (5%)')
        diskon+=5
    if hari in weekdays:
        print('+ Diskon Weekdays (10%)')
        diskon+=10
    if hari in weekend:
        print('+ Diskon Weekend (5%)')
        diskon+=5
    print('-----------------------')
    print('Total Diskon: '+str(diskon)+'%')
    print('-----------------------')

interaksi.utama()