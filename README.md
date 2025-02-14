# CRYPTOLOGY NOTES

# 🔐 Advanced Encryption Standard (AES)

AES (Advanced Encryption Standard) is the first publicly available encryption algorithm approved by the NSA for encrypting **Top Secret** documents.  
The encryption process is based on the **Substitution-Permutation** principle and involves multiple iterative rounds to enhance security.

## 🛠 AES Rounds Structure

The number of **rounds (iterations)** in AES depends on the **key length** used:

- **128-bit key → 10 rounds**
- **192-bit key → 12 rounds**
- **256-bit key → 14 rounds**

More rounds increase security but also require more processing power and memory.

---

## 🔄 AES Encryption Steps

### 🟢 Initial Round (Start)
1. **AddRoundKey**  
   - In the first encryption round, the key is directly XORed with the plaintext.

### 🔵 Main Rounds (Repeated Steps)
Each round consists of four operations:

2. **SubBytes**  
   - Each byte is replaced using an **S-Box (Substitution Box)** transformation.

3. **ShiftRows**  
   - Rows in the encryption matrix are shifted according to a predefined pattern.

4. **MixColumns**  
   - Columns are mixed using a specific mathematical transformation.

5. **AddRoundKey**  
   - A new key is generated and XORed with the current data.

### 🔴 Final Round
In the last round, the **MixColumns** step is omitted. The final round consists of:

6. **SubBytes**  
7. **ShiftRows**  
8. **AddRoundKey**  

After these operations, the **ciphertext (encrypted data)** is obtained.

---

AES is a highly optimized symmetric encryption algorithm in terms of both **speed and security**.  
It is widely used in various security protocols such as **SSL/TLS, VPN, and Wi-Fi WPA2**.


# KRİPTOLOJİ NOTLARI

## 🔐 Advanced Encryption Standard (AES)

AES (Advanced Encryption Standard), NSA tarafından **çok gizli** seviyesindeki belgelerin şifrelenmesi için onaylanmış, kamuya açık ilk şifreleme algoritmasıdır.  
Şifreleme süreci, **Değiştirme-Karıştırma (Substitution-Permutation)** prensibine dayanır ve güvenliği artırmak için birden fazla döngüsel işlem içerir.

## 🛠 AES Döngü Yapısı

AES algoritmasında, kullanılan **anahtar uzunluğuna** bağlı olarak **döngü (round) sayısı** belirlenir:

- **128-bit anahtar → 10 döngü**
- **192-bit anahtar → 12 döngü**
- **256-bit anahtar → 14 döngü**

Daha fazla döngü, daha güçlü bir güvenlik sağlarken, işlem süresi ve bellek kullanımı da buna paralel olarak artar.

---

## 🔄 AES Şifreleme Adımları

### 🟢 İlk Döngü (Başlangıç)
1. **Tur Anahtar Ekleme (AddRoundKey)**  
   İlk şifreleme turunda, anahtar doğrudan açık metin ile XOR işlemine tabi tutulur.

### 🔵 Ara Döngüler (Tekrarlayan İşlemler)
Her döngü aşağıdaki dört alt işlemden oluşur:

2. **Bayt Değiştirme (SubBytes)**  
   - Her bayt, bir **S-Box (Substitution Box)** kullanılarak farklı bir bayta dönüştürülür.

3. **Satır Kaydırma (ShiftRows)**  
   - Şifreleme matrisinin satırları belirli bir düzene göre kaydırılır.

4. **Sütun Karıştırma (MixColumns)**  
   - Matrisin sütunları özel bir matematiksel dönüşüm ile karıştırılır.

5. **Tur Anahtar Ekleme (AddRoundKey)**  
   - Her döngüde, yeni bir anahtar üretilerek mevcut veriyle XOR işlemi yapılır.

### 🔴 Son Döngü
Son turda **Sütun Karıştırma (MixColumns)** işlemi uygulanmaz. Döngü şu şekilde tamamlanır:

6. **Bayt Değiştirme (SubBytes)**  
7. **Satır Kaydırma (ShiftRows)**  
8. **Tur Anahtar Ekleme (AddRoundKey)**  

Bu işlemler tamamlandığında **şifrelenmiş veri (ciphertext)** elde edilir.

---

AES, hız ve güvenlik açısından modern sistemler için optimize edilmiş bir simetrik şifreleme algoritmasıdır.  
Günümüzde birçok güvenlik protokolünde (**SSL/TLS, VPN, Wi-Fi WPA2, vs.**) yaygın olarak kullanılmaktadır.
