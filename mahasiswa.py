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

