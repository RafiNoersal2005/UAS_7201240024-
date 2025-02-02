reservations = []  # List untuk menyimpan data reservasi
stack = []        # Stack untuk implementasi LIFO
queue = []        # Queue untuk implementasi FIFO

# Fungsi Menambahkan Reservasi
def add_reservation():
    reservation_id = input("Masukkan ID Reservasi: ")
    guest_name = input("Masukkan Nama Tamu: ")
    room_type = input("Masukkan Tipe Kamar (Single/Double/Suite): ")
    check_in = input("Masukkan Tanggal Check-In (YYYY-MM-DD): ")
    check_out = input("Masukkan Tanggal Check-Out (YYYY-MM-DD): ")
    reservation = {
        "ID": reservation_id,
        "Guest": guest_name,
        "RoomType": room_type,
        "CheckIn": check_in,
        "CheckOut": check_out
    }
    reservations.append(reservation)
    stack.append(reservation)
    queue.append(reservation)
    print("Reservasi berhasil ditambahkan.\n")

# Fungsi Menampilkan Semua Reservasi
def display_reservations():
    if not reservations:
        print("Tidak ada reservasi dalam daftar.\n")
        return
    print("\nDaftar Reservasi:")
    print(f"{'ID':<10} {'Nama Tamu':<20} {'Tipe Kamar':<15} {'Check-In':<12} {'Check-Out':<12}")
    print("-" * 70)
    for res in reservations:
        print(f"{res['ID']:<10} {res['Guest']:<20} {res['RoomType']:<15} {res['CheckIn']:<12} {res['CheckOut']:<12}")
    print()

# Fungsi Menghapus Reservasi
def delete_reservation():
    reservation_id = input("Masukkan ID Reservasi yang ingin dihapus: ")
    global reservations
    for res in reservations:
        if res['ID'] == reservation_id:
            reservations.remove(res)
            if res in stack:
                stack.remove(res)
            if res in queue:
                queue.remove(res)
            print("Reservasi berhasil dihapus.\n")
            return
    print("Reservasi tidak ditemukan.\n")

# Fungsi Mengupdate Reservasi
def update_reservation():
    reservation_id = input("Masukkan ID Reservasi yang ingin diupdate: ")
    for res in reservations:
        if res['ID'] == reservation_id:
            new_guest = input("Masukkan Nama Tamu Baru: ")
            new_room = input("Masukkan Tipe Kamar Baru: ")
            new_check_in = input("Masukkan Tanggal Check-In Baru: ")
            new_check_out = input("Masukkan Tanggal Check-Out Baru: ")
            res['Guest'] = new_guest
            res['RoomType'] = new_room
            res['CheckIn'] = new_check_in
            res['CheckOut'] = new_check_out
            print("Reservasi berhasil diupdate.\n")
            return
    print("Reservasi tidak ditemukan.\n")

# Fungsi Mengurutkan Reservasi Berdasarkan Tanggal Check-In
def sort_reservations_by_check_in():
    global reservations
    reservations = sorted(reservations, key=lambda x: x['CheckIn'])
    print("Reservasi telah diurutkan berdasarkan tanggal check-in.\n")

# Fungsi Pencarian Berdasarkan Nama Tamu
def search_reservation():
    target_name = input("Masukkan Nama Tamu yang ingin dicari: ").lower()
    results = [res for res in reservations if target_name in res['Guest'].lower()]
    if results:
        print("\nReservasi Ditemukan:")
        for res in results:
            print(res)
    else:
        print("Reservasi tidak ditemukan.\n")

# Fungsi Menampilkan Reservasi di Stack (LIFO)
def display_stack():
    if not stack:
        print("Stack kosong.\n")
        return
    print("\nReservasi dalam Stack (LIFO):")
    for res in reversed(stack):
        print(f"{res['ID']} - {res['Guest']} ({res['CheckIn']} - {res['CheckOut']})")
    print()

# Fungsi Menampilkan Reservasi di Queue (FIFO)
def display_queue():
    if not queue:
        print("Queue kosong.\n")
        return
    print("\nReservasi dalam Queue (FIFO):")
    for res in queue:
        print(f"{res['ID']} - {res['Guest']} ({res['CheckIn']} - {res['CheckOut']})")
    print()

# Menu Utama
def main_menu():
    while True:
        print("=== Sistem Manajemen Reservasi Hotel ===")
        print("1. Tambah Reservasi")
        print("2. Tampilkan Semua Reservasi")
        print("3. Update Reservasi")
        print("4. Hapus Reservasi")
        print("5. Urutkan Reservasi Berdasarkan Check-In")
        print("6. Cari Reservasi Berdasarkan Nama Tamu")
        print("7. Tampilkan Reservasi di Stack (LIFO)")
        print("8. Tampilkan Reservasi di Queue (FIFO)")
        print("9. Keluar")
        choice = input("Pilih menu (1-9): ")
        print()
        if choice == "1":
            add_reservation()
        elif choice == "2":
            display_reservations()
        elif choice == "3":
            update_reservation()
        elif choice == "4":
            delete_reservation()
        elif choice == "5":
            sort_reservations_by_check_in()
        elif choice == "6":
            search_reservation()
        elif choice == "7":
            display_stack()
        elif choice == "8":
            display_queue()
        elif choice == "9":
            print("Terima kasih telah menggunakan Sistem Manajemen Reservasi Hotel!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Jalankan Program
if __name__ == "__main__":
    main_menu()
