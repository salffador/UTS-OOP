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
superadmin.report_issue(3, "Tidak bisa mengakses halaman profil.")
superadmin.resolve_issue()
superadmin.update_system_security()
