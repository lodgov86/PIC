

def UART(self):
    # Enable pyserial extensions
    import pyftdi.serialext
    
    # Open a serial port on the second FTDI device interface (IF/2) @ 3Mbaud
    port = pyftdi.serialext.serial_for_url('ftdi:///1', baudrate=9600)
    
    # Send bytes
    #port.write(b'Hello World')
    
    # Receive bytes
    #data = port.read(1024)
    
    #print (data)
