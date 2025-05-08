import requests
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor, as_completed

# Inisialisasi colorama untuk mendukung warna di terminal
init(autoreset=True)

def cek_domain(domain):
    """
    Fungsi untuk mengecek apakah domain dapat diakses dengan /cdn-cgi/trace.
    Mengembalikan domain jika status code 200, atau None jika gagal.
    """
    url = f"http://{domain}/cdn-cgi/trace"
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            return domain
    except requests.exceptions.RequestException:
        pass
    return None

def cek_domain_parallel(file_name):
    """
    Fungsi utama untuk membaca file domain, mengecek domain secara paralel,
    dan menampilkan hasil.
    """
    try:
        # Membaca file txt yang berisi daftar domain
        with open(file_name, 'r') as file:
            domains = [line.strip() for line in file if line.strip()]

        print(f"Mengecek domain dari file: {file_name}\n")

        # List untuk menyimpan domain yang berhasil diakses
        successful_domains = []

        # Menggunakan ThreadPoolExecutor untuk mengecek domain secara paralel
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(cek_domain, domain) for domain in domains]

            for future in as_completed(futures):
                result = future.result()
                if result:
                    successful_domains.append(result)
                    print(Fore.GREEN + f"200 {result}")

        # Menanyakan apakah pengguna ingin menyimpan hasil ke file
        save_option = input("\nSimpan hasil ke dalam file txt dengan nama? (Tekan Enter untuk tidak menyimpan): ").strip()
        if save_option:
            save_file_name = f"{save_option}.txt"
            with open(save_file_name, 'w') as save_file:
                for domain in successful_domains:
                    save_file.write(f"{domain}\n")
            print(Fore.CYAN + f"Hasil telah disimpan ke file: {save_file_name}")

    except FileNotFoundError:
        print(Fore.RED + f"File '{file_name}' tidak ditemukan.")
    except Exception as e:
        print(Fore.RED + f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    # Meminta input nama file dari pengguna
    file_name = input("Masukkan nama file txt yang berisi daftar domain: ").strip()
    cek_domain_parallel(file_name)
