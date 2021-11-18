import serial
import time

# Open and configure Serial connection
ser = serial.Serial()
ser.baudrate = 57600
ser.port = 'COM3'
ser.timeout = 1

ser.open()

answer = "Y"

if ~ser.is_open:
   while answer != "N" and ser.is_open == False:
      print ("Problem in serial connection, try again?")
      answer = input("(Y or N): ")
      if answer == "N":
         exit()
      else:
         if answer == "Y":
            ser.open()
         else:
            print("Only Y and N are valid answers.")

if ser.is_open:
   print ("Serial connection is open")

# Use those bytearrays to send commands to the fpga
request_data = bytearray()
reset_counter = bytearray()

# Must use do nothing after request_data or reset_counter
do_nothing = bytearray()

request_data.append(0x81)
do_nothing.append(0x80)
# If you want to change the RO, must be in reset mode
reset_counter.append(0x82)

# Use this bytearray to change your register
select_register1 = bytearray()
select_register2 = bytearray()

# [7:6] = select command. [5:0] instructions, on select register: {reg1[5:0],reg2[5:0]}

for z in range (1,11):

   select_register1.clear()
   select_register2.clear()
   
   select_register1.append(0x00)
   select_register2.append(0x40)

   f = open("Z_Resultados_" + str(z) + ".txt", "w")

   reg_counter = 0

   for x in range(1,65):
      for y in range(1,65):
         time.sleep(0.001)
         ser.write(reset_counter)
         time.sleep(0.001)
         ser.write(select_register1)
         time.sleep(0.001)
         ser.write(select_register2)
         time.sleep(0.001)
         ser.write(do_nothing)
         time.sleep(0.001)
         ser.write(request_data)
         time.sleep(0.001)
         f.write("\nContador " + str(reg_counter) + ": 0x" + str(ser.read().hex()) + str(ser.read().hex()))
         ser.write(do_nothing)
         select_register2[0] = select_register2[0] + 1
         reg_counter = reg_counter + 1
         
      select_register1[0] = select_register1[0] + 1
      select_register2.clear()
      select_register2.append(0x40)
      print(select_register1[0])

   ser.write(reset_counter)

   f.close()

ser.close()