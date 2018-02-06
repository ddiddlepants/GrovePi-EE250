
def Main():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 
    host = '127.0.0.1'
    port = 1023

    server_addr = '192.168.1.225'

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    s.bind((host,port))

    dst_port = input("destination port-> ")
    while True:
        #tuples are immutable so we need to overwrite the last tuple
        server = (server_addr, int(dst_port))

        try:
        # Read distance value from Ultrasonic
        print(grovepi.ultrasonicRead(ultrasonic_ranger))
        distance = grovepi.ultrasonicRead(ultrasonic_ranger)

    	except TypeError:
        	print ("Error")
    	except IOError:
        	print ("Error")

        # for UDP, sendto() and recvfrom() are used instead
        s.sendto(distance.encode('utf-8'), server) 
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server: " + data)
        dst_port = input("destination port-> ")
        message = input("message-> ")
    s.close()

if __name__ == '__main__':
    Main()