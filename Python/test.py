import uart

#The following serial device is specific to the system
#In Windows systems they tend to be a COM?? device
#In Linux they are typically under /dev/ttyUSB??? 
ser = open_serial('COM5') #Create the serial object

##################################
### TEST 1 - Send 3 pieces of data
##################################

# In the FPGA Architecture, for each received byte, one is sent
uart.send_byte(0x01,ser)
uart.send_byte(0x02,ser)
uart.send_byte(0x03,ser)

#Clean the serial buffer -- Garbage from the Shift Register
ser.flushOutput()

#Expected to read the sentbytes: 0x01 0x02 0x03
ser.read(3)


#######################################################
### Test 2 - Send integers from 0 - 255 from a for loop
#######################################################
for x in range(0,255):
    uart.send_byte(x,ser)

ser.read(253)
