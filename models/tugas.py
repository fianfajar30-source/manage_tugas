from abc import ABC, abstractmethod


class Tugas(ABC):
    """Class induk (abstract) untuk semua jenis tugas.

    Rumus prioritas berbeda tiap jenis, jadi hitung_prioritas()
    wajib ditulis oleh class anak.
    """

    def __init__(self, kode, judul, deadline, estimasi_jam):
        self.kode = kode
        self.judul = judul
        self.deadline = deadline         
        self.estimasi_jam = estimasi_jam  
        self.selesai = False

    @abstractmethod
    def hitung_prioritas(self, hari_ini):
        pass

    def sisa_hari(self, hari_ini):
        """Selisih hari menuju deadline (negatif jika sudah lewat)."""
        return (self.deadline - hari_ini).days

    def skor_urgensi(self, hari_ini):
        """Skor dasar dari sisa hari, dipakai oleh semua class anak."""
        sisa = self.sisa_hari(hari_ini)
        if sisa < 0:
            return 100
        if sisa <= 1:
            return 80
        if sisa <= 3:
            return 60
        if sisa <= 7:
            return 40
        return 20

    def tandai_selesai(self):
        if self.selesai:
            raise ValueError("Tugas sudah ditandai selesai.")
        self.selesai = True

    def __str__(self):
        status = "selesai" if self.selesai else "belum selesai"
        tanggal = self.deadline.strftime("%d-%m-%Y")
        return (f"[{self.kode}] {self.judul} | deadline {tanggal} "
                f"| {self.estimasi_jam} jam | {status}")
