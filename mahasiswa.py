
class Mahasiswa:
    def __init__(self, nama, npm, jurusan, no_telepon):
        self.__nama = nama
        self.__npm = npm
        self.__jurusan = jurusan
        self.__no_telepon = no_telepon

    def set_nama(self, nama):
        self.__nama = nama

    def set_npm(self, npm):
        self.__npm = npm

    def set_jurusan(self, jurusan):
        self.__jurusan = jurusan

    def set_no_telepon(self, no_telepon):
        self.__no_telepon = no_telepon

    def get_nama(self):
        return self.__nama

    def get_npm(self):
        return self.__npm

    def get_jurusan(self):
        return self.__jurusan

    def get_no_telepon(self):
        return self.__no_telepon




