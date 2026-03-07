# kullanilabilen log formati [tarih] - [ip] - [durum]
import os

def log_analiz_et(log_listesi, hedef_durum="failed"):
    eslesen_log_sayisi = 0
    hedef_ipler = set()
    for log in log_listesi:
        if log["durum"] == hedef_durum:
            eslesen_log_sayisi += 1
            hedef_ipler.add(log["ip"])

    return eslesen_log_sayisi, hedef_ipler

veritabani_loglari = []
with open("deneme_log.txt", "r") as log_dosyasi:
    for line in log_dosyasi:
        veri = line.split(" - ")
        log_verisi = {
            "ip": veri[1],
            "durum": veri[2].strip()
        }
        veritabani_loglari.append(log_verisi)

basarisiz_loglar, basarisiz_ipler = log_analiz_et(log_listesi=veritabani_loglari, hedef_durum="failed")
basarili_loglar, basarili_ipler = log_analiz_et(log_listesi=veritabani_loglari, hedef_durum="success")

while True:
    secim = input("Goruntulemek istediginiz verinin numarasini yaziniz (1)Basarili Loglar ve IP'ler, (2)Basarisiz Loglar ve IP'ler, (3)Tumu, (4)Raporu Kaydet, (q)Cikis: ")

    if secim == "1":
        print(f"Basarili Log Sayisi: {basarili_loglar}, Basarili IP'ler: {basarili_ipler}")
    elif secim == "2":
        print(f"Basarisiz Log Sayisi: {basarisiz_loglar}, Basarisiz IP'ler: {basarisiz_ipler}")
    elif secim == "3":
        print(f"Basirili Log Sayisi: {basarili_loglar} | Basarisiz Log Sayisi: {basarisiz_loglar} | Basarili IP'ler: {basarili_ipler} | Basarisiz IP'ler: {basarisiz_ipler} ")
    elif secim == "4":
        with open("rapor.txt", "w") as rapor_dosyasi:
            rapor_dosyasi.write(f"Basirili Log Sayisi: {basarili_loglar} | Basarisiz Log Sayisi: {basarisiz_loglar} | Basarili IP'ler: {basarili_ipler} | Basarisiz IP'ler: {basarisiz_ipler} ")
        rapor_yolu = os.path.abspath("rapor.txt")
        print(f"Dosya suraya kaydedildi: {rapor_yolu}")
    elif secim.lower() == "q":
        break
    else:
        print("Yanlis secim yaptiniz, tekrar deneyiniz")