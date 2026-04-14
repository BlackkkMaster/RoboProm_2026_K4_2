import time
from tools import Manipulator, Conveer


def test_man():
    man.toPoint(200, 0, 200, 0, 0)
    time.sleep(2)
    man.toPoint(100, 0, 200, 0, 0)
    time.sleep(2)
    man.toPoint(200, 0, 200, 0, 0)
    time.sleep(2)


def test_con():
    con.enable()
    time.sleep(2)
    con.disable()
    time.sleep(2)
    con.enable()
    time.sleep(2)
    con.disable()
    time.sleep(2)


man = Manipulator("192.168.43.4", 8888, "g")
con = Conveer("192.168.43.13", 8888)

test_man()
test_con()
