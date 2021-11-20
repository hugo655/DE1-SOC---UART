import serial

def open_serial(port_name):
    ser = serial.Serial(port=port_name, baudrate=57600, bytesize=8, parity='N', stopbits=1, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False)
    ser.close()
    ser.open()
    return ser

def send_byte(byte2send, seri):
    my_var = bytearray()
    my_var.append(byte2send)
    seri.write(my_var)
    my_var.clear()


