#python 3.7.3

print ( "## ## ### ## ## ## ## ## ## ### ######## ####### ######## ## >
print ( "## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## #>
print ( "## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ####>
print ( "##### ## ## ## ##### ## ## ## ## ## ## ## ## ####### ########>
print ( "## ## ######## ## ## ## ## ## ## ######### ## ## ## ## ## ## >
print ( "## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##" )  >
print ( "## ## ## ## ######## ## ## ####### ######## ## ##############>
print ( " \n \t \t \t DiCiptakan oleh : MR.CyberHack ./RelGans (github.>

print ( " \033 [93m \t \t \t Tim : IndonesiaCyberXploid (github.>
    waktu . tidur ( 2 )
def  Tambah ( Dzarel , Aya ):
        kembali  Dzarel  +  Aya
def  kurang ( Dzarel , Aya ) :
        kembali  Dzarel  -   Aya
def  kali ( Dzarel , Aya ):
        kembali  Dzarel  *  Aya
def  hasil_bagi ( Dzarel , Aya ):
        kembalikan  Dzarel  %  Aya
def  pangkat ( Dzarel , Aya ):
        kembali  Dzarel  **  Aya
def  bulat ( Dzarel , Aya ):
        kembali  Dzarel  //  Aya

print ( " \n Pilih ? \n " )
    print ( "1.Pertambahan" )
    print ( "2. Pengurangan" )
    print ( "3. Perkalian" )
    print ( "4.bagi" )
    print ( "5. Sisa dari Pembagian" )
    print ( "6. Pangkat" )
    print ( "7.Pembagian Bulat" )
    print ( "8. Keluar" )


xyz  =  raw_input ( " \n Masukkan pilihan (Angka) : " )
jika  xyz  ==  '1' :
        faz  =  int ( input ( " \n masukkan angka pertama : " ))
        rya  =  int ( input ( "Masukkan angka kedua : " ))
        print ( " \n " , faz , "+" , rya , "=" , tambah ( faz , rya ))
        waktu . tidur ( 3 )
        cetak ( " \n "  *  100 )
        fazga ()
elif  xyz  ==  '2' :
        faz  =  int ( input ( " \n masukkan angka pertama : " ))
        rya  =  int ( input ( "Masukkan angka kedua : " ))
        print ( " \n " , faz , "-" , rya , "=" , kurang ( faz , rya ))
        waktu . tidur ( 3 )
  cetak ( " \n "  *  100 )
        fazga ()

       elif  xyz  ==  '3' :
        faz  =  int ( input ( " \n masukkan angka pertama : " ))
        rya  =  int ( input ( "Masukkan angka kedua : " ))
        print ( " \n " , faz , "*" , rya , "=" , kali ( faz , rya ))
        waktu . tidur ( 3 )
        cetak ( " \n "  *  100 )
        fazga ()
        
        elif  xyz  ==  '4' :
        faz  =  int ( input ( " \n masukkan angka pertama : " ))
        rya  =  int ( input ( "Masukkan angka kedua : " ))
        print ( " \n " , faz , "/" , rya , "=" , bagi ( faz , rya ))
        waktu . tidur ( 3 )
        cetak ( " \n "  *  100 )
        fazga ()

elif  xyz  ==  '5' :
        faz  =  int ( input ( " \n masukkan angka pertama : " ))
        rya  =  int ( input ( "Masukkan angka kedua : " ))
        print ( " \n " , faz , "%" , rya , "=" , hasil_bagi ( faz , ry>
        waktu . tidur ( 3 )
        cetak ( " \n "  *  100 )
        fazga ()

elif  xyz  ==  '6' :
        faz  =  int ( input ( " \n masukkan angka pertama : " ))
        rya  =  int ( input ( "Masukkan angka kedua : " ))
        print ( " \n " , faz , "**" , rya , "=" , pangkat ( faz , rya >
        waktu . tidur ( 3 )
        cetak ( " \n "  *  100 )
        fazga ()

elif  xyz  ==  '7' :
        faz  =  int ( input ( " \n masukkan angka pertama : " ))
        rya  =  int ( input ( "Masukkan angka kedua : " ))
        print ( " \n " , faz , "//" , rya , "=" , bulat ( faz , rya ))
        waktu . tidur ( 3 )
        cetak ( " \n "  *  100 )
        fazga ()
elif  xyz  ==  '8' :
        print ( " \033 [92m \n sampai jumpa !" )
        waktu . tidur ( 2 )
        cetak ( " \n "  *  100 )
        keluar

lain :
        print ( " \033 [91m \n Salah Pilihan !" )
        waktu . tidur ( 2 )
        cetak ( " \n "  *  100 )
        fazga ()

fazga ()