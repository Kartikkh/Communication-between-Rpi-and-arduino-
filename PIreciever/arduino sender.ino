#include <SPI.h>
#include "nRF24L01.h"
#include "RF24.h"

RF24 radio(9,10);


void setup(void){
 // while(!Serial);
  // Serial.begin(9600);

  radio.begin();

  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  radio.openWritingPipe(0xF0F0F0F0E1LL);
 
  radio.enableDynamicPayloads();
  radio.powerUp(); 
}

void loop(void){
     const char text[] = "1";  
       radio.write(&text , sizeof(text));
       delay(200);
    }
   
