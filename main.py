"""
Aplikasi deteksi gampa terkini
Modularisasi dengan function
"""
import gempa_terkini


if __name__ == '__main__':
    print('Aplikasi utama')
    result = gempa_terkini.ekstraksi_data()
    gempa_terkini.tampilkan_data(result)
