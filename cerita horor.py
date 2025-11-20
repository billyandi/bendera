# nested = bersarang
# di dalam if / elif / else ada conditional

# CERITA HORROR

# main4.py
# Demon Slayer Interactive Story - Giyu & Tanjiro vs Akaza
# Dengan Good Ending (Akaza kepenggal) & Bad Ending

print("MALAM YANG GELAP")
print("hutan yang begitu sepi")
print("ada sesuatu di hutan itu, tapi.... apa?")
print("seorang explorer berjalan jalan di hutan dan ia menemuka sesuatu")
print()
print("1. mencari tahu")
print("2. pergi menjauh")
choice = int(input("= "))

if choice == 1:
    print("saat mendekat ia melihat sebuah gambar aneh yang bersimbolkan bintang")
    print("tiba tiba suasana menjadi sangat hening")
    print("explorer tersebut penasran dengan batu tersebut dan memotretnya")
    print("tiba tiba sebuah suara muncul")

    print("muncul suara jejak kaki")
    print("bersembunyi atau kabur?")
    print("1. kabur")
    print("2. sembunyi")
    choice = int(input("= "))

    if choice == 1:
        print("explorer tersebut terus berlari hingga menemukan sebuah goa")
        print("ia masuk ke dalam goa tersebut dan merasakan hal aneh namun")
        print("ia tidak mengetahui hal tersebut dan akhirnya menunggu")
        print("besok harinya suasana sudah membaik")
        print("ia berlari keluar dari hutan")
        print("GOOD ENDING = ia selamat dari tangkapan mahkluk yang tidak di ketahui")
    else:
        print("ia bersembunyi di balik bebatuan")
        print("suara jejak kaki tersebut semakin mendekat")
        print("mulai terdengar suara aneh seperti tarikan nafas yang berat")
        print("tiba tiba suara jalan tersebut menjadi lari")
        print("BAD ENDING = sang explorer tertangkap dan langsung di makan hidup-hidup")
else:
    print("ia berjalan pergi menjauhi batu tersebut")
    print("namun suara jejak kaki itu terus terdengar bersamaan suara nafas")
    print("ia menengok kebelakang dan melihat seseorang dengan pakaian hitam, sambil membawa kapak")
    print("ia melihat sebuah batang kayu tebal")

    print("1. mengambil batang kayu terus kabur")
    print("2. mengambil lalu kabur")
    choice = int(input("= "))

    if choice == 1:
        print("ia berlari sambil membawa batang tersebut")
        print("namun kecepatan dari orang tersebut lebih cepat dari pada sang explorer")
        print("ia melihat sebuah pagar lalu melewati pagar tersebut")
        print("lalu menutup lubang pagar tersebut dengan batang kayu yang di bawa")
        print("GOOD ENDING = orang berbaju hitam hanya menatap dari balik pagar dan membiarkanmu pergi")
    else:
        print("orang tersebut semakin mendekat")
        print("explorer itu mengangkat kayu yang ia pegang")
        print("saat sudah dekat ia menghantamkan kayu tersebut ke arah orang tersebut")
        print("namun sayang orang tersebut berhasil menahan")
        print("BAD ENDING = explorer di banting ke tanah dan badan nya di cincang oleh orang tersebut")