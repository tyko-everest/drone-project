#include <SoftwareSerial.h>

SoftwareSerial radio(5, 4);

void setup() {
  Serial.begin(9600);
  radio.begin(9600);
  pinMode(3, OUTPUT);
  pinMode(3, LOW);

//  radio.write("AT+RESET");
//  delay(100);
//  while (radio.available()) {
//    Serial.write(radio.read()); 
//  }

}
  
void loop() {
  while (Serial.available()) {
    radio.write(Serial.read()); 
  }
}
