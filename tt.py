#!/usr/bin/env python
import serial
import time

sp = serial.Serial(
    port="/dev/cu.usbmodemfd111",
    baudrate=115200,     # baudrate
    bytesize=8,             # number of databits
    parity=serial.PARITY_EVEN,
    stopbits=1,
    xonxoff=0,              # enable software flow control
    rtscts=0,               # disable RTS/CTS flow control
    timeout=0.5             # set a timeout value, None for waiting forever
)

cnt = 1
while 1:
    if cnt > 10:
        print "send 0x7F ..."
        sp.write("\x7F")
        cnt = 0
    cnt = cnt + 1
    ch = sp.read()
    if ch:
        if ord(ch) != 0x00:
            print(hex(ord(ch)))
    # time.sleep(1)
