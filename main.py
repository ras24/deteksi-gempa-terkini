"""
Aplikasi deteksi gampa terkini
Modularisasi dengan function
"""


def ekstraksi_data():
    """
    Tanggal: 26 April 2022
    Waktu: 00:01:06 WIB
    Magnitudo: 4.8
    Kedalaman: 25 km
    Lokasi: LS=7.48 BT=106.68
    Pusat Gempa: Pusat gempa berada di laut 56 km tenggarakab. Sukabumi
    Dirasakan: Dirasakan (Skala MMI): II - III Sukabumi, II - III Cianjur selatan, II Garut, II Pangandaran
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '26 April 2022'
    hasil['waktu'] = '00:01:06 WIB'
    hasil['magnitudo'] = 4.8
    hasil['kedalaman'] = '25 km'
    hasil['lokasi'] = {'ls': 7.48, 'bt': 106.68}
    hasil['pusat'] = 'Pusat gempa berada di laut 56 km tenggarakab. Sukabumi'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II - III Sukabumi, II - III Cianjur selatan, II Garut, II Pangandaran'
    
    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
