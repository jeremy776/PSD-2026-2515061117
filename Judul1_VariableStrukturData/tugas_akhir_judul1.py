def menu_utama():
    print('')
    print('       Selamat Datang di Gudang Minimarket       ')
    print('')
    print('Menu Tersedia                      ')
    print('1. Tambah Produk Toko              ')
    print('2. Daftar Produk Toko              ')
    print('3. Hapus Produk Toko               ')
    print('4. Keluar                          ')
    print('')


def main():
    daftar_barang = []
    daftar_harga = []
    running = True
    while running:
        menu_utama()
        try:
            pilih_menu = int(input('Masukkan nomor menu: '))
            
            if pilih_menu == 1:
                print(' ')
                print('            Penambahan Prdouk            ')
                print(' ')
                running_add_product = 'y'
                while running_add_product.lower() == 'y':
                    try:
                        barang_baru = input('Masukan produk baru (ketik exit untuk keluar): ')
                        if barang_baru == 'exit':
                            running_add_product = 'n'
                            continue
                        harga_barang = int(input('Masukan harga produk: '))
                        daftar_barang += [barang_baru.lower()]
                        daftar_harga += [harga_barang]
                        print('')
                        print(f'Poduk baru telah di tambahkan:\n {barang_baru.capitalize()} - Rp. {harga_barang}')
                        print('')
                        running_add_product = input('Mau tambah produk lagi? (y/n): ')
                        print('')
                    except ValueError:
                        print('Input yang diberikan tidak valid.')
                        print('')
                        continue
            elif pilih_menu == 2:
                print(' ')
                print('            Daftar Produk            ')
                print(' ')
                if len(daftar_barang) <= 0:
                    print('Belum ada Produk di Gudang')
                else:
                    for i in range(len(daftar_barang)):
                        print(f'{daftar_barang[i].capitalize()} - Rp. {daftar_harga[i]}')
            elif pilih_menu == 3:
                print(' ')
                print('            Hapus Produk            ')
                print(' ')
                try:
                    running_delete_product = 'y'
                    while running_delete_product.lower() == 'y':
                        if len(daftar_barang) <= 0:
                            print('Belum ada Produk di Gudang')
                            running_delete_product = 'n'
                            continue
                        else:
                            for i in range(len(daftar_barang)):
                                print(f'{i+1}.  {daftar_barang[i].capitalize()} - Rp. {daftar_harga[i]}')
                            print('')
                        hapus_ke = int(input('Masukan nomor barang yang ingin dihapus (ketik exit untuk keluar): '))
                        if hapus_ke > len(daftar_barang):
                            print('Barang tidak dapat ditemukan.')
                            print('')
                            continue
                        
                        print(f'Berhasil menghapus {daftar_barang[hapus_ke-1].capitalize()}')
                        del daftar_barang[hapus_ke-1]
                        del daftar_harga[hapus_ke-1]
                        print('')
                        running_delete_product = input('Mau menghapus produk lagi? (y/n): ')
                except ValueError:
                    print('Input yang diberikan tidak valid.')
                    print('')
                    continue
            elif pilih_menu == 4:
                print('Terima kasih telah menggunakan program ini.')
                running = False
            else:
                print('')
                print('Menu tidak tersedia didalam program ini.')
        except ValueError:
            print('Input kamu tidak valid, masukan angka yang sesuai.')
            

if __name__ == "__main__":
    main()