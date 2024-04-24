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
