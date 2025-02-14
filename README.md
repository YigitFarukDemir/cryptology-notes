🔐 Advanced Encryption Standard (AES)
AES (Advanced Encryption Standard), NSA tarafından "çok gizli" seviyesindeki belgelerin şifrelenmesi için onaylanmış, kamuya açık ilk şifreleme algoritmasıdır. Şifreleme süreci, Değiştirme-Karıştırma (Substitution-Permutation) prensibine dayanır ve güvenliği artırmak için birden fazla döngüsel işlem içerir.

🛠 AES Döngü Yapısı
AES algoritmasında, kullanılan anahtar uzunluğuna bağlı olarak döngü (round) sayısı belirlenir:

128-bit anahtar → 10 döngü
192-bit anahtar → 12 döngü
256-bit anahtar → 14 döngü
Daha fazla döngü, daha güçlü bir güvenlik sağlarken, işlem süresi ve bellek kullanımı da buna paralel olarak artar.

🔄 AES Şifreleme Adımları
🟢 İlk Döngü (Başlangıç)
1️⃣ Tur Anahtar Ekleme (AddRoundKey)

İlk şifreleme turunda, anahtar doğrudan açık metin ile XOR işlemine tabi tutulur.
🔵 Ara Döngüler (Tekrarlayan İşlemler)
Her döngü aşağıdaki dört alt işlemden oluşur:

2️⃣ Bayt Değiştirme (SubBytes)

Her bayt, bir S-Box (Substitution Box) kullanılarak farklı bir bayta dönüştürülür.
3️⃣ Satır Kaydırma (ShiftRows)

Şifreleme matrisinin satırları belirli bir düzene göre kaydırılır.
4️⃣ Sütun Karıştırma (MixColumns)

Matrisin sütunları özel bir matematiksel dönüşüm ile karıştırılır.
5️⃣ Tur Anahtar Ekleme (AddRoundKey)

Her döngüde, yeni bir anahtar üretilerek mevcut veriyle XOR işlemi yapılır.
🔴 Son Döngü
Son turda Sütun Karıştırma (MixColumns) işlemi uygulanmaz. Döngü şu şekilde tamamlanır:

6️⃣ Bayt Değiştirme (SubBytes)
7️⃣ Satır Kaydırma (ShiftRows)
8️⃣ Tur Anahtar Ekleme (AddRoundKey)

Bu işlemler tamamlandığında şifrelenmiş veri (ciphertext) elde edilir.

AES, hız ve güvenlik açısından modern sistemler için optimize edilmiş bir simetrik şifreleme algoritmasıdır ve günümüzde birçok güvenlik protokolünde (SSL/TLS, VPN, Wi-Fi WPA2, vs.) yaygın olarak kullanılmaktadır.
