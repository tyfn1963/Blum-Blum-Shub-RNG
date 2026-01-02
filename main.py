import time


# BBS Algoritması (Blum Blum Shub)
# Odev icin hazirlanmistir.

class RastgeleSayiUretec:
    def __init__(self, bit_sayisi):
        # Asal sayilar (p ve q).
        # Kural: ikisi de 4'e bolununce 3 kalmali.
        self.p = 30000000091
        self.q = 40000000003

        # M degeri (Blum tamsayisi)
        self.M = self.p * self.q

        # Seed (tohum) degeri. Zaman damgasini kullaniyoruz ki her seferinde farkli olsun.
        # Seed'in 0 veya 1 olmamasi lazim, M ile aralarinda asal olmali.
        zaman_damgasi = int(time.time() * 10000)
        self.state = zaman_damgasi % self.M
        self.uzunluk = bit_sayisi

        # print(f"Baslangic degeri (Seed): {self.state}") # Kontrol icin acilabilir

    def bit_uret(self):
        # Formül: x_yeni = (x_eski^2) mod M
        self.state = (self.state ** 2) % self.M

        # En sondaki biti aliyoruz (tek mi cift mi)
        return self.state % 2

    def calistir(self):
        sonuc_dizisi = []
        for i in range(self.uzunluk):
            bit = self.bit_uret()
            sonuc_dizisi.append(bit)

        return sonuc_dizisi


def istatistik_kontrol(dizi):
    toplam = len(dizi)
    sifirlar = dizi.count(0)
    birler = dizi.count(1)

    print("\n--- Sonuclar ---")
    print(f"Toplam Uretilen: {toplam} bit")
    print(f"0 Sayisi: {sifirlar}")
    print(f"1 Sayisi: {birler}")

    # Oranlari yazdir
    oran_0 = (sifirlar / toplam) * 100
    oran_1 = (birler / toplam) * 100
    print(f"Oranlar -> 0: %{oran_0:.2f} | 1: %{oran_1:.2f}")

    # Basit bir kalite kontrolu
    fark = abs(sifirlar - birler)
    if fark < (toplam * 0.05):  # %5 hata payi kabul edilebilir
        print("Sonuc: Denge saglandi. (Basarili)")
    else:
        print("Sonuc: Denge biraz bozuk, tekrar calistirilabilir.")


# Ana dongu
if __name__ == "__main__":
    print("Sayi ureteci baslatiliyor...")

    # 5000 bit uretsin simdilik
    app = RastgeleSayiUretec(5000)
    bitler = app.calistir()

    # Ornek gorunsun diye ilk 64 biti ekrana basiyoruz
    ekran_cikti = "".join(str(b) for b in bitler[:64])
    print(f"Ornek Cikti (Ilk 64 bit): {ekran_cikti}...")

    istatistik_kontrol(bitler)