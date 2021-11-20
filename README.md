# DE1-SOC UART Project

This project is an attempt to build an interface to send data from a PC to an FPGA via a UART interface.

The first set of tools used are an Altera Development Board DE1-SoC and a python script making use of the PySerial API.

The architectures of the digital system in the FPGA are prone to changes over time given the amount of tests to by performed on the software side of it. 

In the **root** folder there are a number of Verilog and SystemVerilog files that can be reused in any other FPGA project, the rest of it are QuartusII-specific files for the model I have available. The names are self-explanatory, however here is a list of the files used in the current stage of the project:

- DE1\_SOC.v : Top-module and wrapper
- BSR.sv: Byte shift register
- uart.v: A simple UART module, non configurable, that operates with baudrate 57600, 8-bit, no-parity-check, no flowcontrol, 1-bit start/stop bits
- hex\_decoder: A module that converts a 4-bit binary number to a 7-bit binary number complient with a 7-segment led display
- byte\_reg.v: (not in use) 4-bit counter

In the **Python** folder there are two files `uart.py` and `test.py`. The first one is a custom library that implements two functions `open_serial()` and `send_byte()`. They make use of methods from the PySerial API, user must install the packge first.
