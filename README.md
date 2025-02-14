# cryptology-notes

AES
AES, NSA tarafından çok gizli belgelerin şifrelenmesinde kullanımı onaylanmış kamuya açık ilk şifreleme uygulamasıdır.
Temelinde Değiştirme-Karıştırma(Substution-Permutation) işlemlerine dayanır.
kullanılan anahtar uzunluğuna göre döngü sayısı belirlenir.döngü sayısı artıkça daha güvenilir bir hal alırken döngüsel işlemlerin artması performansın daha yavaş olmasına ,yapılacak işlem ve kullanılan bellek alanının artmasına yol açar.
İlk döngüde gerçekleşen alt işlem;
 Tur Anahtar Ekleme(AddRoundKey)
Ara döngülerde gerçekleşen alt işlemler;
 Bayt değiştirme (SubBytes)
 Satır Kaydırma(ShiftRows)
 Sütun Karıştırma (MixColumn)
 Tur Anahtar Ekleme(AddRoundKey)
Son döngüde gerçekleşen alt işlemler;
 Bayt değiştirme (SubBytes)
 Satır Kaydırma(ShiftRows)
 Tur Anahtar Ekleme(AddRoundKey)
