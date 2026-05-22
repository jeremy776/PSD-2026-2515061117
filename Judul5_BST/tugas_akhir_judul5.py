class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTDasar:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def search_node(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)
    
    def inorder_students(self, node, students={}):
        if node is None:
            return
        self.inorder_students(node.left, students)
        print(f"{node.key} - {students.get(node.key, '')}")
        self.inorder_students(node.right, students)

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


def main():
    bst = BSTDasar()
    students = {}

    while True:
        print("\n=== Daftar Mahasiswa (Sederhana) ===")
        print("1. Tambah mahasiswa")
        print("2. Cari mahasiswa by NPM")
        print("3. Tampilkan semua mahasiswa (urut NPM)")
        print("4. Jumlah mahasiswa")
        print("0. Keluar")

        pilih = input("Pilihan: ")
        if pilih == "1":
            try:
                npm = int(input("NPM (angka): "))
            except ValueError:
                print("NPM harus berupa angka")
                continue
            if npm in students:
                print("NPM sudah terdaftar")
                continue
            nama = input("Nama mahasiswa: ")
            bst.insert(npm)
            students[npm] = nama
            print(f"Mahasiswa {nama} (NPM: {npm}) ditambahkan")
        elif pilih == "2":
            try:
                npm = int(input("NPM yang dicari: "))
            except ValueError:
                print("NPM harus berupa angka")
                continue
            if bst.search(npm):
                print(f"Ditemukan: {npm} - {students.get(npm, '(nama tidak tersedia)')}")
            else:
                print("Mahasiswa tidak ditemukan")
        elif pilih == "3":
            if bst.root is None:
                print("Daftar mahasiswa kosong.")
            else:
                bst.inorder_students(bst.root, students)
        elif pilih == "4":
            print(f"Jumlah mahasiswa: {bst.count_nodes(bst.root)}")
        elif pilih == "0":
            print("Selesai.")
            break
        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()
