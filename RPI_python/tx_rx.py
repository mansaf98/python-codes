import serial
from sys import exit
from datetime import datetime

message = "start:"
with open("threshold.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    #print(stripped_line)
    message=message + stripped_line + ":"
message = message[:-1] + '\n'
#print(message)
a_file.close()
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    i = 0
    while True:
        output = open("output.txt", 'w')
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        output.write("this is the greenhouse enviornment as of "+ dt_string)
        output.write("\n")
        ser.write(message.encode())
        if ser.in_waiting > 0:
            try:
                rx = ser.readline().decode('utf-8').rstrip()
                print(rx)
                if rx.startswith('gas levels:'):
                    for i in range(8):
                        print(rx)
                        output.write(rx + "\n")
                        output.flush()
                        rx = ser.readline().decode('utf-8').rstrip()
                    output.close()
                    exit() 
            except UnicodeDecodeError:
                print("cont")
             