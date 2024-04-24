class User:
    def __init__(self, user_id, password):
        self._user_id = user_id
        self._password = password

    def login(self, user_id, password):
        if user_id == self._user_id and password == self._password:
            print(f"Welcome, User {self._user_id}!")
            return True
        else:
            print("Invalid user_id or password.")
            return False

    def get_user_id(self):
        return self._user_id


class Mahasiswa(User):
    def __init__(self, nim, nama, jurusan, user_id, password):
        super().__init__(user_id, password)
        self._nim = nim
        self._nama = nama
        self._jurusan = jurusan

    def get_nim(self):
        return self._nim

    def get_nama(self):
        return self._nama

    def get_jurusan(self):
        return self._jurusan


class Dosen(User):
    def __init__(self, nama, nip, user_id, password):
        super().__init__(user_id, password)
        self._nama = nama
        self._nip = nip

    def get_nama(self):
        return self._nama

    def get_nip(self):
        return self._nip


class UAA(User):
    def __init__(self, nama, user_id, password):
        super().__init__(user_id, password)
        self._nama = nama

    def get_nama(self):
        return self._nama


class SuperAdmin(User):
    def __init__(self, nama, user_id, password):
        super().__init__(user_id, password)
        self._nama = nama

    def get_nama(self):
        return self._nama


class Library(User):
    def __init__(self, nama, user_id, password):
        super().__init__(user_id, password)
        self._nama = nama

    def get_nama(self):
        return self._nama


# Contoh penggunaan:

# Mahasiswa
mahasiswa1 = Mahasiswa("422023029", "Salvador", "Sistem Informasi", 1, "password123")
mahasiswa1.login(1, "password123")  # Expected output: "Welcome, User 1!"
print(f"Mahasiswa NIM {mahasiswa1.get_nim()}, {mahasiswa1.get_nama()}, Jurusan {mahasiswa1.get_jurusan()}")

# Dosen
dosen1 = Dosen("Hendrik Tampubolon", "12345", 2, "password456")
dosen1.login(2, "password456")  # Expected output: "Welcome, User 2!"
print(f"Dosen {dosen1.get_nama()}, NIP {dosen1.get_nip()}")

# UAA
uaa1 = UAA("Dosenblablabla", 3, "password789")
uaa1.login(3, "password789")  # Expected output: "Welcome, User 3!"
print(f"UAA {uaa1.get_nama()}")

# SuperAdmin
superadmin1 = SuperAdmin("Tubagus", 4, "password1011")
superadmin1.login(4, "password1011")  # Expected output: "Welcome, User 4!"
print(f"SuperAdmin {superadmin1.get_nama()}")

# Library
library1 = Library("Perpustakaan UKRIDA", 5, "password1213")
library1.login(5, "password1213")  # Expected output: "Welcome, User 5!"
print(f"Library {library1.get_nama()}")

class User:
    def __init__(self, user_id, password):
        self._user_id = user_id
        self._password = password

    def login(self, user_id, password):
        if user_id == self._user_id and password == self._password:
            print(f"Welcome, User {self._user_id}!")
            return True
        else:
            print("Invalid user_id or password.")
            return False

    def get_user_id(self):
        return self._user_id


class Mahasiswa(User):
    def __init__(self, nim, nama, jurusan, user_id, password):
        super().__init__(user_id, password)
        self._nim = nim
        self._nama = nama
        self._jurusan = jurusan
        self._softskills_points = 0
        self._calendar = []

    def upload_sertifikat(self, nama_sertifikat):
        self._softskills_points += 1
        print(f"Sertifikat {nama_sertifikat} berhasil diupload.")

    def lihat_kalender(self):
        return self._calendar

    def tambah_event_kalender(self, event):
        self._calendar.append(event)

    def get_nim(self):
        return self._nim

    def get_nama(self):
        return self._nama

    def kirim_e_ticket(self, pesan):
        e_ticket = f"Mahasiswa {self._nama} ({self._nim}) melaporkan:{pesan}"
        return e_ticket


class Dosen(User):
    def __init__(self, nama, nip, user_id, password):
        super().__init__(user_id, password)
        self._nama = nama
        self._nip = nip

    def get_nama(self):
        return self._nama

    def get_nip(self):
        return self._nip


class UAA(User):
    def __init__(self, nama, user_id, password):
        super().__init__(user_id, password)
        self._nama = nama

    def get_nama(self):
        return self._nama


class SuperAdmin(User):
    def __init__(self, nama, user_id, password):
        super().__init__(user_id, password)
        self._nama = nama
        self._e_tickets = []

    def tanggapi_e_ticket(self, e_ticket):
        self._e_tickets.append(e_ticket)
        print(f"E-ticket dari {e_ticket.splitlines()[0]} telah diterima dan akan segera ditangani.")

    def get_nama(self):
        return self._nama


class Library(User):
    def __init__(self, nama, user_id, password):
        super().__init__(user_id, password)
        self._nama = nama
        self._books = {"Pemrograman Dasar": 5, "Basis Data": 3, "Kalkulus": 7}

    def pinjam_buku(self, judul):
        if judul in self._books and self._books[judul] > 0:
            self._books[judul] -= 1
            print(f"Anda berhasil meminjam buku {judul}.")
        else:
            print(f"Maaf, stok buku {judul} sedang habis.")

    def kembalikan_buku(self, judul):
        if judul in self._books:
            self._books[judul] += 1
            print(f"Anda telah mengembalikan buku {judul}.")
        else:
            print(f"Buku {judul} bukan milik perpustakaan ini.")

    def get_nama(self):
        return self._nama


# Contoh penggunaan:

# Mahasiswa
mahasiswa1 = Mahasiswa("422023029", "Salvador", "Sistem Informasi", 1, "password123")
pesan_e_ticket = "Saya menemukan bug pada fitur upload sertifikat."
e_ticket = mahasiswa1.kirim_e_ticket(pesan_e_ticket)
print("E-ticket yang dikirimkan:", e_ticket)

# SuperAdmin
superadmin1 = SuperAdmin("Admin", 10, "password_admin")
superadmin1.tanggapi_e_ticket(e_ticket)
print("E-tickets yang diterima:", superadmin1._e_tickets)

# Library
library1 = Library("Perpustakaan Universitas", 20, "password_library")
library1.pinjam_buku("Pemrograman Dasar")
library1.kembalikan_buku("Pemrograman Dasar")

class Mahasiswa(User):
    def __init__(self, nim, nama, jurusan, user_id, password):
        super().__init__(user_id, password)
        self._nim = nim
        self._nama = nama
        self._jurusan = jurusan
        self._softskills_points = 0
        self._calendar = []
        self._pa = None
        self._jumlah_bimbingan_pa = 0  # Jumlah bimbingan PA dalam semester ini

    def upload_sertifikat(self, nama_sertifikat):
        self._softskills_points += 1
        print(f"Sertifikat {nama_sertifikat} berhasil diupload.")

    def lihat_kalender(self):
        return self._calendar

    def tambah_event_kalender(self, event):
        self._calendar.append(event)

    def get_nim(self):
        return self._nim

    def get_nama(self):
        return self._nama

    def kirim_e_ticket(self, pesan):
        e_ticket = f"Mahasiswa {self._nama} ({self._nim}) melaporkan:\n{pesan}"
        return e_ticket

    def tambah_bimbingan_pa(self, pa_nama):
        self._pa = pa_nama
        self._jumlah_bimbingan_pa += 1  # Menambah jumlah bimbingan setiap kali metode dipanggil
        print(f"Bimbingan PA dengan {pa_nama} telah ditambahkan. Jumlah bimbingan PA sekarang adalah {self._jumlah_bimbingan_pa}.")

    def get_pa(self):
        return self._pa

    def get_jumlah_bimbingan_pa(self):
        return self._jumlah_bimbingan_pa

# Contoh penggunaan:

# Mahasiswa
mahasiswa1 = Mahasiswa("422023029", "Salvador", "Sistem Informasi", 1, "password123")
mahasiswa1.tambah_bimbingan_pa("Dosen Pembimbing")
mahasiswa1.tambah_bimbingan_pa("Dosen Pembimbing")
mahasiswa1.tambah_bimbingan_pa("Dosen Pembimbing")
print(f"Bimbingan PA telah dilakukan sebanyak {mahasiswa1.get_jumlah_bimbingan_pa()} kali dalam semester ini.")

class User:
    def __init__(self, user_id, password):
        self._user_id = user_id
        self._password = password

    def login(self, user_id, password):
        if user_id == self._user_id and password == self._password:
            print(f"Welcome, User {self._user_id}!")
            return True
        else:
            print("Invalid user_id or password.")
            return False

    def get_user_id(self):
        return self._user_id

class Dosen(User):
    def __init__(self, nip, nama, departemen, user_id, password):
        super().__init__(user_id, password)
        self._nip = nip
        self._nama = nama
        self._departemen = departemen
        self._jadwal = []
        self._nilai = {}
        self._absensi = {}

    def upload_jadwal(self, mata_kuliah, waktu):
        self._jadwal.append((mata_kuliah, waktu))
        print(f"Jadwal {mata_kuliah} pada {waktu} berhasil diupload.")

    def upload_nilai(self, nim, mata_kuliah, nilai):
        if nim not in self._nilai:
            self._nilai[nim] = {}
        self._nilai[nim][mata_kuliah] = nilai
        print(f"Nilai {nilai} untuk mata kuliah {mata_kuliah} mahasiswa NIM {nim} berhasil diupload.")

    def upload_absensi(self, nim, mata_kuliah, tanggal, hadir=True):
        if nim not in self._absensi:
            self._absensi[nim] = {}
        if mata_kuliah not in self._absensi[nim]:
            self._absensi[nim][mata_kuliah] = []
        self._absensi[nim][mata_kuliah].append((tanggal, hadir))
        status = "hadir" if hadir else "tidak hadir"
        print(f"Absensi untuk {nim} pada mata kuliah {mata_kuliah} tanggal {tanggal} sebagai {status} berhasil diupload.")

# Example usage:
dosen1 = Dosen("D12345", "Dr. Ahmad", "Teknik Informatika", 2, "securePass123")
dosen1.login(2, "securePass123")  # User login
dosen1.upload_jadwal("Algoritma", "Senin, 08:00-10:00")
dosen1.upload_nilai("422023029", "Algoritma", 94)
dosen1.upload_absensi("422023029", "Algoritma", "2024-04-22")

class User:
    def __init__(self, user_id, password):
        self._user_id = user_id
        self._password = password

    def login(self, user_id, password):
        if user_id == self._user_id and password == self._password:
            print(f"Welcome, User {self._user_id}!")
            return True
        else:
            print("Invalid user_id or password.")
            return False

    def get_user_id(self):
        return self._user_id

class UAA(User):
    def __init__(self, user_id, password, nama):
        super().__init__(user_id, password)
        self._nama = nama
        self._tagihan = {}
        self._kalender_pendidikan = []

    def input_tagihan(self, nim, jumlah, deskripsi):
        if nim not in self._tagihan:
            self._tagihan[nim] = []
        self._tagihan[nim].append({"jumlah": jumlah, "deskripsi": deskripsi})
        print(f"Tagihan {jumlah} untuk NIM {nim} dengan deskripsi '{deskripsi}' berhasil ditambahkan.")

    def input_event_kalender(self, tanggal, event):
        self._kalender_pendidikan.append({"tanggal": tanggal, "event": event})
        print(f"Event '{event}' pada tanggal {tanggal} berhasil ditambahkan ke kalender pendidikan.")

# Example usage:
uaa = UAA(3, "uaaPass123", "Pak Budi")
uaa.login(3, "uaaPass123")
uaa.input_tagihan("422023029", 0, "SPP Semester Ganjil 2023/2024")
uaa.input_event_kalender("2023-09-01", "Awal Semester Ganjil")

class User:
    def __init__(self, user_id, password):
        self._user_id = user_id
        self._password = password

    def login(self, user_id, password):
        if user_id == self._user_id and password == self._password:
            print(f"Welcome, User {self._user_id}!")
            return True
        else:
            print("Invalid user_id or password.")
            return False

    def get_user_id(self):
        return self._user_id

class Library(User):
    def __init__(self, user_id, password, library_name):
        super().__init__(user_id, password)
        self.library_name = library_name
        self.books = {}  # Dictionary to store book title and quantities
        self.loan_requests = []  # List to store loan requests

    def add_book(self, title, quantity):
        if title in self.books:
            self.books[title] += quantity
        else:
            self.books[title] = quantity
        print(f"{quantity} copies of '{title}' added to the library.")

    def request_book_loan(self, student_id, book_title):
        if book_title in self.books and self.books[book_title] > 0:
            self.loan_requests.append((student_id, book_title))
            print(f"Loan request for '{book_title}' by student {student_id} accepted.")
        else:
            print(f"Book '{book_title}' is not available for loan.")

    def approve_loan(self):
        if not self.loan_requests:
            print("No pending loan requests.")
            return
        student_id, book_title = self.loan_requests.pop(0)
        self.books[book_title] -= 1
        print(f"Loan approved for student {student_id} for the book '{book_title}'.")

    def check_book_availability(self, title):
        if title in self.books and self.books[title] > 0:
            print(f"'{title}' is available with {self.books[title]} copies remaining.")
        else:
            print(f"'{title}' is not available.")

# Example usage:
library = Library(5, "lib123", "Main Campus Library")
library.login(5, "lib123")
library.add_book("Python Programming", 3)
library.request_book_loan("422023029", "Python Programming")
library.approve_loan()
library.check_book_availability("Python Programming")

class User:
    def __init__(self, user_id, password):
        self._user_id = user_id
        self._password = password

    def login(self, user_id, password):
        if user_id == self._user_id and password == self._password:
            print(f"Selamat datang, Pengguna {self._user_id}!")
            return True
        else:
            print("ID pengguna atau kata sandi salah.")
            return False

    def get_user_id(self):
        return self._user_id

class SuperAdmin(User):
    def __init__(self, user_id, password):
        super().__init__(user_id, password)
        self.e_tickets = []  # Menyimpan masukan/laporan bug

    def report_issue(self, user_id, issue):
        self.e_tickets.append((user_id, issue))
        print(f"Laporan masalah diterima dari pengguna {user_id}: {issue}")

    def resolve_issue(self):
        if not self.e_tickets:
            print("Tidak ada masalah yang perlu diatasi saat ini.")
            return
        user_id, issue = self.e_tickets.pop(0)
        print(f"Masalah dari pengguna {user_id} telah diatasi: {issue}")

    def update_system_security(self):
        print("Keamanan sistem diperbarui untuk melindungi data pengguna.")

# Contoh penggunaan:
superadmin = SuperAdmin(999, "adminSecure")
superadmin.login(999, "adminSecure")
superadmin.report_issue(1, "Bug pada u!pload sertifikat.")
superadmin.resolve_issue()
superadmin.update_system_security()
