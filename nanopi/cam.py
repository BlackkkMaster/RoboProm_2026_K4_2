import time
import socket

if __name__ == "__main__":
    ip = "192.168.43.111"
    server = "192.168.43.9"
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpPort = 8888
    udp.bind((ip, 8889))

    while True:
        try:
            udp.sendto(str.encode(f"c:2#"), (server, udpPort))
            time.sleep(2)
            data, addr = udp.recvfrom(1024)
            answer = str(data).split(":")
            print(answer)
            print(answer[11], answer[12])
        except KeyboardInterrupt as e:
            print("Interrupted")
            break
    exit()
