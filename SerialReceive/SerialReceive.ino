#include <SoftwareSerial.h>

SoftwareSerial radio(5, 4);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  radio.begin(9600);
  pinMode(3, OUTPUT);
  pinMode(3, LOW);

}

int i = 0;
  
void loop() {
  while (radio.available()) {
    Serial.write(radio.read()); 
  }
}
