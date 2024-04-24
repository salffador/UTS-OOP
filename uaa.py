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
