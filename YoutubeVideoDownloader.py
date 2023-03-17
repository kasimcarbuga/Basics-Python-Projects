from pytube import Youtube

import os

link = Youtube (
    str(input("Link giriniz")))

video = link.streams.filter( 
    progressive = True,
    only_video = False,
    file_extension ='mp4').order_by('resolution').desc().first()

print("Kaydedilecek yolu girin")

print("(dosya içine kaydedilmesi için boş bırakın)")

yol = str(input("--")) or '.'

indirilmesigerekendosya = video.download(output_path=yol)

print (link.title + "İndirme Tamamlandı")
