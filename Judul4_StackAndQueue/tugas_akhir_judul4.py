class QueueArray:
    def __init__(self, max_size=10):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, x):
        if self.is_full():
            print("Antrian Rumah Sakit sudah penuh.")
            return
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.q[self.rear_idx] = x
        print(f"{x} Berhasil di masukkan ke antrian.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian masih kosong.")
            return
        print(f"Telah melayani {self.q[self.front_idx]}")
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Antrian masih kosong.")
            return
        print(f"Antrian sekarang: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("Antrian masih kosong.")
            return
        print("Isi antrian saat ini: ", end="")
        i = self.front_idx
        while True:
            print(self.q[i], end=" ")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
        print()

def main():
    queue = QueueArray()
    pilih = 0
    while pilih != 5:
        print("\n=== Sistem antrian Rumah Sakit ===")
        print("1. Tambah antrian")
        print("2. Layani antrian")
        print("3. Antrian paling depan")
        print("4. Tampilkan")
        print("5. Keluar Program")
        try:
            pilih = int(input("Pilih Menu: "))
        except ValueError:
            print("Pilih menu harus berupa angka!")
            continue
        if pilih == 1:
            try:
                val = str(input("Nama Pasien: "))
                queue.enqueue(val)
            except ValueError:
                print("Nama tidak sesuai dengan format!")
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            print("Program telah selesai.")
        else:
            print(f"Menu {pilih} tidak tersedia. Silakan pilih menu yang valid.")
            
if __name__ == "__main__":
    main()
