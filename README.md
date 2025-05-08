# bugilped
---

# 🕵️‍♂️ bugilped.py

**bugilped.py** adalah alat sederhana berbasis Python untuk memeriksa apakah suatu domain responsif terhadap endpoint `http://domain.com/cdn-cgi/trace`. Tool ini sangat berguna untuk mendeteksi situs yang menggunakan layanan Cloudflare.

---

## ✨ Fitur

* Mengecek banyak domain secara paralel untuk performa tinggi
* Menggunakan threading untuk efisiensi
* Menampilkan hasil domain yang merespons dengan status `200 OK`
* Opsi untuk menyimpan hasil ke file `.txt`
* Dukungan warna terminal dengan `colorama`

---

## 📦 Instalasi

1. **Clone repositori ini**:

   ```bash
   git clone https://github.com/username/bugilped.git
   cd bugilped
   ```

2. **Buat dan aktifkan virtual environment (opsional tapi disarankan)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   Jika belum ada file `requirements.txt`, kamu bisa langsung install manual:

   ```bash
   pip install requests colorama
   ```

---

## 🧪 Cara Menjalankan

1. **Buat file `.txt` berisi daftar domain**, satu domain per baris, misalnya `daftar.txt`:

   ```
   example.com
   google.com
   cloudflare.com
   ```

2. **Jalankan script**:

   ```bash
   python bugilped.py
   ```

3. **Masukkan nama file saat diminta**:

   ```
   Masukkan nama file txt yang berisi daftar domain: daftar.txt
   ```

4. Jika ada domain yang valid (merespons `http://domain.com/cdn-cgi/trace` dengan kode 200), hasil akan ditampilkan dengan warna hijau.

5. Di akhir eksekusi, kamu akan ditanya apakah ingin menyimpan hasil:

   ```
   Simpan hasil ke dalam file txt dengan nama? (Tekan Enter untuk tidak menyimpan): hasil_valid
   ```

   Maka hasil akan disimpan sebagai `hasil_valid.txt`.

---

## 📁 Contoh Output

```bash
Mengecek domain dari file: daftar.txt

200 google.com
200 cloudflare.com

Simpan hasil ke dalam file txt dengan nama? (Tekan Enter untuk tidak menyimpan): hasil
Hasil telah disimpan ke file: hasil.txt
```

---

## ❗ Catatan

* Tool ini hanya mendeteksi apakah domain merespons pada endpoint `cdn-cgi/trace`, bukan jaminan situs menggunakan Cloudflare.
* Pastikan file daftar domain valid dan bisa diakses dari jaringan Anda.
* Jalanakn di termux hp yang memiliki kuota ilped, jika di laptop jalankan dengan hotspot dari hp yang memiliki kuota ilped.

---

## 📄 Lisensi

Repositori ini berlisensi bebas digunakan untuk keperluan edukasi, riset, dan pentesting legal. Gunakan dengan tanggung jawab.

---

Kalau kamu mau, aku juga bisa buatkan `requirements.txt` dan bantu upload ke GitHub. Mau sekalian dibuatkan?

## ❗ Payload
GET /cdn-cgi/trace HTTP/1.1[crlf]Host: bakrie.ac.id[crlf]Connection: Keep-Alive[crlf][crlf]GET-RAY / HTTP/1.1[crlf]Host: [host][crlf]Upgrade: websocket 🔥 CREATE BY  : AFZAN 🔥[crlf][crlf
