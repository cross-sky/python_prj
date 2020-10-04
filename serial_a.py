import serial
import threading, time
import string
import serial.tools.list_ports


class SerThread:
    def __init__(self, port='com3'):  # Serial
        self.my_serial = serial.Serial()
        self.my_serial.port = port
        self.my_serial.baudrate = 9600
        self.my_serial.timeout = 10
        self.alive = False
        self.waitEnd = None
        fname = time.strftime('%Y%m%d')
        self.rfname = 'r' + fname
        self.sfname = 'r' + fname
        self.thread_read = None
        self.thread_send = None
        self.sfile = open(self.sfname, 'w')
        self.rfile = open(self.rfname, 'w')

    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()

    def start(self):
        self.my_serial.open()
        print(self.my_serial.name)

        if self.my_serial.isOpen():
            self.waitEnd = threading.Event()
            self.alive = True
            self.thread_read = threading.Thread(target=self.reader)
            self.thread_read.setDaemon(True)

            self.thread_send = threading.Thread(target=self.sender)
            self.thread_send.setDaemon(True)

            self.thread_send.start()
            self.thread_read.start()
            return True
        else:
            return False

    def reader(self):
        while self.alive:
            try:
                data = self.my_serial.readline().decode('utf-8')
                print('recv: ' + time.strftime('%m%d/%H:%M:%S') + ", "+ data.strip())
                #print(time.strftime('%m%d/%H:%M:%S') + ',' + data.strip(), file=self.rfile)
            except Exception as ex:
                print(ex)

        self.waitEnd.set()
        self.alive = False

    def sender(self):
        while self.alive:
            try:
                send_data = input('input data:\n')
                if send_data == 'q':
                    break

                self.my_serial.write(send_data.encode('utf-8'))

            except Exception as ex:
                print(ex)

        self.waitEnd.set()
        self.alive = False

    def stop(self):
        self.alive = False
        if self.my_serial.isOpen():
            self.my_serial.close()
        self.rfile.close()
        self.sfile.close()


if __name__ == '__main__':
    list_port = list(serial.tools.list_ports.comports())
    i = 0
    if len(list_port):
        for l in list_port:
            print(str(i) + ': ' + str(l))
            i += 1
    port = input('please select a serial.\n')

    port_0 = list(list_port[int(port)])
    print(port_0)
    print(port_0[0])
    ser = SerThread(port_0[0])
    try:
        if ser.start():
            ser.waiting()
            ser.stop()
        else:
            pass
    except Exception as ex:
        print(ex)

    if ser.alive:
        ser.stop()
    print('End ok.')
    del ser
