guvenlik_loglari = [
    {"tarih": "10:00", "ip": "192.168.1.5", "kullanici": "admin", "durum": "success"},
    {"tarih": "10:05", "ip": "10.0.0.1", "kullanici": "root", "durum": "failed"},
    {"tarih": "10:06", "ip": "10.0.0.1", "kullanici": "admin", "durum": "failed"},
    {"tarih": "10:10", "ip": "172.16.0.2", "kullanici": "guest", "durum": "failed"},
    {"tarih": "10:15", "ip": "10.0.0.1", "kullanici": "administrator", "durum": "failed"},
    {"tarih": "10:20", "ip": "192.168.1.5", "kullanici": "admin", "durum": "success"}
]

def log_analiz_et(log_listesi):
    basarisiz_denemeler = 0
    supheli_ipler = set()

    for log in log_listesi:
        if log["durum"] == "failed":
            basarisiz_denemeler += 1
            print(f"Supheli IP bulundu {log['ip']}")
            print("~~~~~~~~~")
            supheli_ipler.add(log["ip"])

    basarisiz_veri = f"Basarisiz deneme sayisi: {basarisiz_denemeler}"
    supheli_veri = f"Tespit edilen supheli IP'ler: {supheli_ipler}"

    return basarisiz_veri, supheli_veri

guvenlik_basarisiz_veri, guvenlik_supheli_veri = log_analiz_et(guvenlik_loglari)

# print(guvenlik_basarisiz_veri)
# print(guvenlik_supheli_veri)