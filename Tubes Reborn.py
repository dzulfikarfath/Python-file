from time import sleep
from rich.progress import track
from rich import print

def rdpu():
    while True:
        try:
            reksaa = int(input("Masukkan jangka waktu investasi Anda (bulan)\t:"))
            assert reksaa >= 1
            break
        except ValueError:
            print("[bold red]Mohon inputkan dalam bentuk angka")
        except AssertionError:
            print("[bold red]minimal selama 1 bulan")
    while True :
        try:
            jumlahrdpu = int(input("Berapa jumlah uang yang Anda ingin investasikan\t:"))
            assert jumlahrdpu >= 1
            break
        except ValueError:
            print("[bold red]Mohon inputkan dalam bentuk angka")
        except AssertionError:
            print("[bold red]Anda tidak bisa memasukkan 0")
    
    awalrdpu = 0
    while True :
        ulangrdpu =input("Apakah Anda ingin menambahkan uang lagi? [Y] / [N] :").capitalize()
        if ulangrdpu == 'Y':
            while True :
                try:
                    jumlahhrdpu = int(input("Berapa jumlah uang yang Anda ingin tambahkan untuk investasi\t:"))
                    assert jumlahhrdpu >= 1
                    awalrdpu += jumlahhrdpu
                    break
                except ValueError:
                    print("[bold red]Mohon inputkan dalam bentuk angka")
                except AssertionError:
                    print("[bold red]Anda tidak bisa memasukkan 0")
        elif ulangrdpu == 'N':
            break

    for step in track(range(2)):
        sleep(1)
        step 

    totalrdpu = jumlahrdpu + awalrdpu
    hasilrdpu = totalrdpu+(reksaa*totalrdpu*.006)
    print("Return investasi Anda selama %i"%reksaa,"bulan adalah %f"%hasilrdpu)
    riwayat["Reksadana Pasar Uang"] = hasilrdpu

def saham():
    while True:
        try:
            sahamm = int(input("Masukkan jangka waktu investasi Anda (bulan)\t:"))
            assert sahamm >= 1
            break
        except ValueError:
            print("[bold red]Mohon inputkan dalam bentuk angka")
        except AssertionError:
            print("[bold red]minimal selama 1 bulan")
    while True :
        try:
            jumlahsaham = int(input("Berapa jumlah uang yang Anda ingin investasikan\t:"))
            assert jumlahsaham >= 1
            break
        except ValueError:
            print("[bold red]Mohon inputkan dalam bentuk angka")
        except AssertionError:
            print("[bold red]Anda tidak bisa memasukkan 0")

    awalsaham = 0
    while True :
        ulangsaham =input("Apakah Anda ingin menambahkan uang lagi? [Y] / [N] :").capitalize()
        if ulangsaham == 'Y':
            while True :
                try:
                    jumlahhsaham = int(input("Berapa jumlah uang yang Anda ingin tambahkan untuk investasi\t:"))
                    assert jumlahhsaham >= 1
                    awalsaham += jumlahhsaham
                    break
                except ValueError:
                    print("[bold red]Mohon inputkan dalam bentuk angka")
                except AssertionError:
                    print("[bold red]Anda tidak bisa memasukkan 0")
        elif ulangsaham == 'N':
            break

    for step in track(range(2)):
        sleep(1)
        step 

    totalsaham = jumlahsaham + awalsaham
    hasilsaham = totalsaham+(sahamm*totalsaham*.0125)
    print("Return investasi Anda selama %i"%sahamm,"bulan adalah %f"%hasilsaham)
    riwayat["Saham"] = hasilsaham

def btc():
    while True:
        try:
            bitc = int(input("Masukkan jangka waktu investasi Anda (bulan)\t:"))
            assert bitc >= 1
            break
        except ValueError:
            print("[bold red]Mohon inputkan dalam bentuk angka")
        except AssertionError:
            print("[bold red]minimal selama 1 bulan")
    while True :
        try:
            jumlahbtc = int(input("Berapa jumlah uang yang Anda ingin investasikan\t:"))
            assert jumlahbtc >= 1
            break
        except ValueError:
            print("[bold red]Mohon inputkan dalam bentuk angka")
        except AssertionError:
            print("[bold red]Anda tidak bisa memasukkan 0")

    awalbtc = 0
    while True :
        ulangbtc =input("Apakah Anda ingin menambahkan uang lagi? [Y] / [N] :").capitalize()
        if ulangbtc == 'Y':
            while True :
                try:
                    jumlahhbtc = int(input("Berapa jumlah uang yang Anda ingin tambahkan untuk investasi\t:"))
                    assert jumlahhbtc >= 1
                    awalbtc += jumlahhbtc
                    break
                except ValueError:
                    print("[bold red]Mohon inputkan dalam bentuk angka")
                except AssertionError:
                    print("[bold red]Anda tidak bisa memasukkan 0")
        elif ulangbtc == 'N':
            break
    
    for step in track(range(2)):
        sleep(1)
        step 

    totalbtc = jumlahbtc + awalbtc
    hasilbtc = totalbtc+(bitc*totalbtc*.0291)
    print("Return investasi Anda selama %i"%bitc,"bulan adalah %f"%hasilbtc)
    riwayat["Bitcoin"] = hasilbtc

def dpst():
    while True:
        try:
            dp = int(input("Masukkan jangka waktu investasi Anda (bulan)\t:"))
            assert dp >= 1
            break
        except ValueError:
            print("[bold red]Mohon inputkan dalam bentuk angka")
        except AssertionError:
            print("[bold red]minimal selama 1 bulan")
    while True :
        try:
            jumlahdpst = int(input("Berapa jumlah uang yang Anda ingin investasikan\t:"))
            assert jumlahdpst >= 1
            break
        except ValueError:
            print("[bold red]Mohon inputkan dalam bentuk angka")
        except AssertionError:
            print("[bold red]Anda tidak bisa memasukkan 0")

    awaldpst = 0
    while True :
        ulangdpst =input("Apakah Anda ingin menambahkan uang lagi? [Y] / [N] :").capitalize()
        if ulangdpst == 'Y':
            while True :
                try:
                    jumlahhdpst = int(input("Berapa jumlah uang yang Anda ingin tambahkan untuk investasi\t:"))
                    assert jumlahhdpst >= 1
                    awaldpst += jumlahhdpst
                    break
                except ValueError:
                    print("[bold red]Mohon inputkan dalam bentuk angka")
                except AssertionError:
                    print("[bold red]Anda tidak bisa memasukkan 0")
        elif ulangdpst == 'N':
            break
    
    for step in track(range(2)):
        sleep(1)
        step 

    totaldpst = jumlahdpst + awaldpst
    hasildpst = totaldpst+(dp*totaldpst*.0041)
    print("Return investasi Anda selama %i"%dp,"bulan adalah %f"%hasildpst)
    riwayat["Deposito"] = hasildpst

def oblgs():
    while True:
        try:
            ob = int(input("Masukkan jangka waktu investasi Anda (bulan)\t:"))
            assert ob>= 1
            break
        except ValueError:
            print("[bold red]Mohon inputkan dalam bentuk angka")
        except AssertionError:
            print("[bold red]minimal selama 1 bulan")
    while True :
        try:
            jumlahoblgs = int(input("Berapa jumlah uang yang Anda ingin investasikan\t:"))
            assert jumlahoblgs >= 1
            break
        except ValueError:
            print("[bold red]Mohon inputkan dalam bentuk angka")
        except AssertionError:
            print("[bold red]Anda tidak bisa memasukkan 0")

    awaloblgs = 0
    while True :
        ulangoblgs =input("Apakah Anda ingin menambahkan uang lagi? [Y] / [N] :").capitalize()
        if ulangoblgs == 'Y':
            while True :
                try:
                    jumlahhoblgs = int(input("Berapa jumlah uang yang Anda ingin tambahkan untuk investasi\t:"))
                    assert jumlahhoblgs >= 1
                    awaloblgs += jumlahhoblgs
                    break
                except ValueError:
                    print("[bold red]Mohon inputkan dalam bentuk angka")
                except AssertionError:
                    print("[bold red]Anda tidak bisa memasukkan 0")
        elif ulangoblgs == 'N':
            break
    
    for step in track(range(2)):
        sleep(1)
        step 

    totaloblgs = jumlahoblgs + awaloblgs
    hasiloblgs = totaloblgs+(ob*totaloblgs*.0116)
    print("Return investasi Anda selama %i"%ob,"bulan adalah %f"%hasiloblgs)
    riwayat["Obligasi"] = hasiloblgs

def history():
    if len(riwayat) == 0:
        print("[bold yellow]Anda belum melakukan kalkulasi investasi")
    else :
        for step in track(range(2)):
            sleep(1)
            step 
        print("Berikut adalah riwayat kalkulasi Anda")
        for key,value in riwayat.items():
            print(f"{key}\t:{value}")

def saran():
    if len(riwayat) == 0:
        print("[bold yellow]Maaf menu ini hanya dapat ditampilkan setelah Anda melakukan kalkulasi")
    elif len(riwayat) == 1:
        print("[bold yellow]Maaf kami belum bisa memberikan saran karena Anda baru melakukan kalkulasi 1x")
    else :
        print("""
            [1] direkomendasikan untuk investasi
            [2] tidak direkomendasikan untuk investasi  
            [0] back
            """)
        aa = int(input("Masukkan pilihan Anda :"))
        if aa == 1 :
            for step in track(range(2)):
                sleep(1)
                step 

            y = riwayat.values()
            tertinggi = max(y)
            xx = [(value, key) for key, value in riwayat.items()]
            b = max(xx)[1]
            print("[bold green]Kami merekomendasikan Anda untuk investasi di",b,"[bold green]karena mendapat return sebesar",tertinggi)
        elif aa == 2 :
            for step in track(range(2)):
                sleep(1)
                step 

            x = riwayat.values()
            terendah = min(x)
            xy = [(value, key) for key, value in riwayat.items()]
            c = min(xy)[1]
            print("[bold yellow]Kami tidak merekomendasikan Anda untuk investasi di",c,"[bold yellow]karena return yang Anda dapatkan hanya",terendah)
        elif aa == 3:
            showmenu()
        


def sektor ():
    print("\t\t[bold green]--- SEKTOR ---")
    print("""
        [1] Reksadana Pasar Uang
        [2] Saham
        [3] Bitcoin
        [4] Deposito
        [5] Obligasi
        [0] Back
        """)
    pilih = int(input("Masukkan di sektor mana Anda ingin investasi :"))
    if pilih == 1:
        rdpu()
    elif pilih == 2:
        saham()
    elif pilih == 3:
        btc()
    elif pilih == 4:
        dpst()
    elif pilih == 5:
        oblgs()
    elif pilih == 0:
        showmenu()



def showmenu():
    print("\t\t[bold green]--- MENU ---")
    print("""
    [1] Simulasi Investasi
    [2] Cek Riwayat Kalkulasi
    [3] Saran Investasi
    [0] [bold red]Exit
    """)
    while True :
        try:
            menu = int(input("Masukkan pilihan\t:"))
            break
        except ValueError :
            print("[bold red]Mohon inputkan dalam bentuk angka")
    if menu == 1:
        sektor()
    elif menu == 2:
        history()
    elif menu == 3:
        saran()
    elif menu == 0:
        if len(riwayat)>=1:
            print("[bold cyan]Terimakasih telah menggunakan simulasi hitung kami")
        exit()

riwayat = {}

while(True):
    showmenu()


    
