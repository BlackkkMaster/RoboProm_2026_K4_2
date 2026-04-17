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

    def toPoint(self, x, y, z, a, g=0):
        self.UDPClientSocket.sendto(str.encode("r#"), self.serverAddressPort)
        if self.type == "g":
            self.UDPClientSocket.sendto(
                str.encode(f"{self.type}:{x}:{y}:{a}:{z}:{g}#"), self.serverAddressPort
            )
        if self.type == "p":
            self.UDPClientSocket.sendto(
                str.encode(f"{self.type}:{x}:{y}:{z}:{g}#"), self.serverAddressPort
            )
        time.sleep(2)

    def home(self):
        self.toPoint(200, 0, 200, -90, 0)

    def test(self):
        self.home()
        time.sleep(2)
        self.toPoint(100, 0, 200, 0, 0)
        time.sleep(2)
        self.home()
        time.sleep(2)

    def to_box(self):
        self.home()
        self.toPoint(250, 210, 98, -90, 1)
        self.toPoint(200, 100, 200, -90, 1)
        self.toPoint(10, 260, 25, -90, 1)
        self.toPoint(10, 260, 25, -90, 0)
        self.toPoint(200, 0, 200, -90)

    def from_box(self):
        self.home()
        self.toPoint(0, -280, 100, -90, 0)
        self.toPoint(0, -280, -10, -90, 1)
        self.toPoint(0, -280, 150, -90, 1)
        self.toPoint(250, -210, 100, -90, 0)

    def move_box_right(self):
        self.home()
        self.toPoint(0, 230, 200, -180)
        self.toPoint(0, 230, 25, -180)
        self.toPoint(0, 195, 25, -90)
        self.toPoint(0, 195, 200, -90)

        self.toPoint(200, 0, 200, -180)
        self.toPoint(200, 0, -100, -180)
        self.toPoint(200, 0, 200, -180)

        self.toPoint(0, -300, 200, -260)
        self.toPoint(0, -300, 25, -260)
        self.toPoint(0, -185, 20, -260)
        self.toPoint(0, -230, 20, -260)
        self.toPoint(0, -280, 20, -100)

        self.toPoint(200, 0, 200, -90)

    def move_box_left(self):
        self.home()

        self.toPoint(0, -230, 200, -180)
        self.toPoint(0, -230, 25, -180)

        self.toPoint(0, -195, 25, -270)
        self.toPoint(0, -195, 200, -270)

        self.toPoint(200, 0, 200, -180)
        self.toPoint(200, 0, 200, -180)

        self.toPoint(0, 300, 200, -100)
        self.toPoint(0, 300, 25, -100)
        self.toPoint(0, 185, 20, -100)
        self.toPoint(0, 230, 20, -100)

        self.toPoint(0, 280, 20, -260)

        self.home()


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
        time.sleep(2)

    def disable(self):
        self.UDPClientSocket.sendto(str.encode("k:0"), self.serverAddressPort)
        time.sleep(2)

    def step(self):
        self.enable()
        time.sleep(3)
        self.disable()
        time.sleep(3)

    def test(self):
        self.enable()
        time.sleep(2)
        self.disable()
        time.sleep(2)
