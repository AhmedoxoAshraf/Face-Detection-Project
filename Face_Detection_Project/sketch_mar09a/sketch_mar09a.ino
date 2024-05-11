#include <cvzone.h> // include libirary

SerialData serialData(2, 1); // creat a serial of two classes
int valsRec[2]; // creat an array with two varaibles

void setup() {
 pinMode(4, OUTPUT); // output1
  pinMode(5, OUTPUT); // output 2
serialData.begin(); // start serial communication

}

void loop() {
  serialData.Get(valsRec); // get the serial data and put it in the array
  digitalWrite(4, valsRec[0]); // turn on output according to the serial data
  digitalWrite(5, valsRec[1]); // turn on output according to the serial data
  delay(10);

}
