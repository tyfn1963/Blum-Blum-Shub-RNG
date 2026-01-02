# 🔐 BBS-Secure-RNG (Blum Blum Shub Generator)

Bu proje, **Sayılar Teorisi** temelli ve kriptografik açıdan güvenli bir sözde rastgele sayı üreteci (CSPRNG) olan **Blum Blum Shub** algoritmasının implementasyonudur.

## 🎯 Proje Amacı
İki temel kuralı sağlayan bir algoritma geliştirmek:
1.  **Tahmin Edilemezlik:** Üretilen sayılarda herhangi bir desen (pattern) bulunmamalıdır.
2.  **İstatistiksel Kalite:** Üretilen bit dizisinde 0 ve 1'lerin dağılımı dengeli (Uniform Distribution) olmalıdır.

## 🧠 Algoritma Mantığı ve Teori

BBS algoritması şu formüle dayanır:

$$x_{n+1} = (x_n)^2 \mod M$$

Burada:
* **M (Blum Tamsayısı):** $p$ ve $q$ gibi iki çok büyük asal sayının çarpımıdır ($M = p \cdot q$).
* **Önemli Kural:** Seçilen $p$ ve $q$ asalları, 4'e bölündüğünde 3 kalanını vermelidir ($p \equiv 3 \mod 4$). Bu, algoritmanın kriptografik zorluğunu garanti eder.
* **Seed (Tohum):** $M$ ile aralarında asal olan rastgele bir başlangıç sayısıdır.

### 📝 Sözde Kod (Pseudo-Code)

```text
BAŞLA
  p, q ASAL sayılarını belirle (p % 4 == 3 VE q % 4 == 3 olmalı)
  M = p * q hesapla
  Seed (x) değerini belirle (M ile aralarında asal)
  
  DÖNGÜ (İstenen bit sayısı kadar):
      x = (x * x) MOD M
      Rastgele_Bit = x MOD 2  (x'in tek mi çift mi olduğuna bak)
      Bit'i listeye ekle
  DÖNGÜ BİTİR
  
  Listeyi analiz et (0 ve 1 sayımı)
BİTİR
