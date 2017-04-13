import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev


GPIO.setmode(GPIO.BCM)


pipes = [[0xE8 , 0xE8 , 0xF0 , 0xF0 , 0xE1] , [0xF0 ,0xF0, 0xF0, 0xF0, 0xE1]]

radio  = NRF24(GPIO,spidev.SpiDev())
radio.begin(0,17)
radio.setPayloadSize(32)
radio.setChannel(0x76)

radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

# radio.openWritingPipe(pipes[0])

radio.openReadingPipe(1,pipes[1])
radio.printDetails()
radio.startListening()



while True:
   
    
    while not radio.available(0):
        time.sleep(1/100)
        

    recievedMessage = []
    radio.read(recievedMessage, radio.getDynamicPayloadSize())
    print("Recieved : {}" .format(recievedMessage))

    print("Translating string")
    string = ""

    for n in recievedMessage:
        if (n>=32 and n<=126):
            string += chr(n)
    
    print("our recieved message to : {}".format(string))

   

    
    
