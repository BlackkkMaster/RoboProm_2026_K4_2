from tools import Manipulator, Conveer
import socket
import time

COUNT_DETAILS = 3
CAMERA_SERVER_IP = "192.168.43.9"
CAMERA_SERVER_PORT = 8888
LOCAL_CAMERA_IP = "192.168.43.111"
LOCAL_CAMERA_PORT = 8889

man = Manipulator("192.168.43.4", 8888, "g")
con = Conveer("192.168.43.13", 8888)

# man.test()
# con.test()

# while True:
#     x, y, z, g = 0, -300, 200, 0
#     x = int(input("x: "))
#     y = int(input("y: "))
#     z = int(input("z: "))
#     #a = int(input("a: "))
#     a = -90
#     g = int(input("g: "))
#     man.toPoint(x, y, z, a, g)

# con.test()


def get_part_info(timeout: float = 2.0):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((LOCAL_CAMERA_IP, LOCAL_CAMERA_PORT))
    sock.settimeout(timeout)
    try:
        sock.sendto(b"c:2#", (CAMERA_SERVER_IP, CAMERA_SERVER_PORT))
        data, _ = sock.recvfrom(1024)
        answer = data.decode().split(":")
        # Ожидаемый формат ответа: ...:тип_детали:...:координата_X:координата_Y
        part_type = answer[3]
        x = float(answer[11])
        y = float(answer[12])
        return [part_type, x, y]
    except (socket.timeout, IndexError, ValueError) as e:
        print(f"Ошибка получения данных с камеры: {e}")
        return None
    finally:
        sock.close()


pred = get_part_info()[2]
c = 0

man.home()

while True:
    try:
        obj = get_part_info()
        if obj[2] == pred or obj[1] < 450:
            continue
        print("detal detected", obj)
        pred = get_part_info()[2]
        man.to_box()
        pred = get_part_info()[2]
        c += 1
        if c == COUNT_DETAILS:
            c = 0
            man.move_box_right()
            while c != COUNT_DETAILS:
                c += 1
                man.from_box()
                con.step()
            man.move_box_left()
            c = 0
    except Exception:
        pass


