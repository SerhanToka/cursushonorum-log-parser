guvenlik_loglari = [
    {"tarih": "10:00", "ip": "192.168.1.5", "kullanici": "admin", "durum": "success"},
    {"tarih": "10:05", "ip": "10.0.0.1", "kullanici": "root", "durum": "failed"},
    {"tarih": "10:06", "ip": "10.0.0.1", "kullanici": "admin", "durum": "failed"},
    {"tarih": "10:10", "ip": "172.16.0.2", "kullanici": "guest", "durum": "failed"},
    {"tarih": "10:15", "ip": "10.0.0.1", "kullanici": "administrator", "durum": "failed"},
    {"tarih": "10:20", "ip": "192.168.1.5", "kullanici": "admin", "durum": "success"}
]

basarisiz_denemeler = 0
supheli_ipler = set()

for log in guvenlik_loglari:
    if log["durum"] == "failed":
        basarisiz_denemeler += 1
        print(f"Supheli IP bulundu: {log['ip']}")
        print("~~~~~~~~~")
        supheli_ipler.add(log["ip"])

print(f"Toplam basarisiz giris denemesi: {basarisiz_denemeler}")
print("Tespit edilen supheli IP'ler: ")
for ip in supheli_ipler:
    print(f"- {ip}")