def sequential_search_sentinel(data, n, target):
    data.append(target)
    i = 0
    while data[i] != target:
        i += 1
    data.pop()
    if i < n:
        return True, i
    else:
        return False, -1

def main():
    data = [140, 33, 28, 95, 86, 72, 15, 60, 120, 45]
    n = len(data)
    print(f'Daftar nomor di perumahan: {data}')
    while True:
        try:
            target = int(input("Masukkan nomor rumah yang ingin dicari: "))
            break
        except ValueError:
            print('Nomor rumah harus berupa angka')
    found, pos = sequential_search_sentinel(data, n, target)
    if found:
        blok = ''
        if pos <= 4:
            blok = 'A'
        elif pos <= 7:
            blok = 'B'
        else:
            blok = 'C'
        print(f'Rumah dengan nomor {target} ditemukan pada blok {blok} urutan ke-{pos+1}')
    else:
        print('Nomor rumah tidak dapat ditemukan')

if __name__ == "__main__":
    main()
