def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


def main():
    try:
        jumlah_barang = int(input('Masukan jumlah barang yang mau dibeli: '))
    except ValueError:
        print('\n===== Jumlah yang diberikan harus berupa angka =====\n')
        return
    arr = []
    print('\n===== Masukan harga masing masing barang =====\n')
    for i in range(jumlah_barang):
        try:
            harga = int(input(f"Masukan harga barang ke {i+1}: "))
            arr.append(harga)
        except ValueError:
            print('\n===== Harga tidak valid, harus berupa angka =====\n')
    print(f'\nUrutan harga barang dari yang termurah:')
    insertion_sort(arr, jumlah_barang)
    for i in range(jumlah_barang):
        print(f'Rp. {arr[i]:,.0f}'.replace(",", "."))
    print()
    
if __name__ == "__main__":
    main()
