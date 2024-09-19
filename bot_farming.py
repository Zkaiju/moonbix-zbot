import time
import random

class MoonbixBot:
    def __init__(self, min_wait=5, max_wait=15):
        self.min_wait = min_wait
        self.max_wait = max_wait

    def start_farming(self):
        print("Bot mulai farming...")
        while True:
            self.perform_farming_action()
            wait_time = random.randint(self.min_wait, self.max_wait)
            print(f"Menunggu selama {wait_time} detik sebelum farming berikutnya...")
            time.sleep(wait_time)

    def perform_farming_action(self):
        # Simulasi aksi farming (misalnya request API)
        print("Melakukan aksi farming...")
        # Kode aksi farming bisa dimasukkan di sini, misalnya request ke API, scraping, dll.
        # Contoh sederhana:
        success = random.choice([True, False])
        if success:
            print("Aksi farming berhasil!")
        else:
            print("Aksi farming gagal!")

if __name__ == "__main__":
    bot = MoonbixBot(min_wait=5, max_wait=10)  # Sesuaikan waktu tunggu sesuai kebutuhan
    bot.start_farming()
