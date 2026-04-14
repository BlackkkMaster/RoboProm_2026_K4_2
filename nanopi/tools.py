import socket
import time


class Manipulator:
    def __init__(self, ip: str, port: int, type: str) -> None:
        self.ip = ip
        self.port = port
        self.UDPClientSocket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM
        )
        self.type = type
        self.serverAddressPort = (ip, port)

    def toPoint(self, x, y, z, a=0, g=0):
        self.UDPClientSocket.sendto(str.encode("r#"), self.serverAddressPort)
        if self.type == "g":
            self.UDPClientSocket.sendto(
                str.encode(f"{self.type}:{x}:{y}:{a}:{z}:{g}#"), self.serverAddressPort
            )
        if self.type == "p":
            self.UDPClientSocket.sendto(
                str.encode(f"{self.type}:{x}:{y}:{z}:{g}#"), self.serverAddressPort
            )


class Camera:
    def __init__(self, ip: str, port: int) -> None:
        self.ip = ip
        self.port = port
        self.UDPClientSocket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM
        )
        self.serverAddressPort = (ip, port)

    def send_test_message(self):
        self.UDPClientSocket.sendto(str.encode("cam:test"), self.serverAddressPort)


class Conveer:
    def __init__(self, ip: str, port: int) -> None:
        self.ip = ip
        self.port = port
        self.UDPClientSocket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM
        )
        self.serverAddressPort = (ip, port)

    def enable(self):
        self.UDPClientSocket.sendto(str.encode("k:1"), self.serverAddressPort)

    def disable(self):
        self.UDPClientSocket.sendto(str.encode("k:0"), self.serverAddressPort)
