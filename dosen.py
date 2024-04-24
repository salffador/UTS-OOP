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
