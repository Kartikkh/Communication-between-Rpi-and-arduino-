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

radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1,pipes[1])
radio.printDetails()

message = "11"


while True:
    start = time.time();
    radio.write(message)
    print("Sent message: {}".format(message))
    radio.startListening()
    
    while not radio.available(0):
        time.sleep(1/100)
        if time.time() - start > 2:
            print("timeOut")
            break


    recievedMessage = []
    radio.read(recievedMessage, radio.getDynamicPayloadSize())
    print("Recieved : {}" .format(recievedMessage))

    print("Translating string")
    string = ''
    print("our recieved message: {} ".format(string))

    radio.stopListening()
    time.sleep(2)


    
    
