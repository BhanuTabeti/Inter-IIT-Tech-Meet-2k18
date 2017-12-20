//Written by Bhanu Prakash Goud Tabeti

#include<Wire.h>

const int MPU_addr=0x68;
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;

int minVal=265;
int maxVal=402;

int gyro1_sda = 22;
int gyro1_scl = 23;

int gyro2_sda = 16;
int gyro2_scl = 17;

int Thumb_pin = 25;
int Index_pin = 33;
int Middle_pin = 32;
int Ring_pin = 35;
int Little_pin = 34;

int Thumb, Index, Middle, Ring, Little;
double x, y, z;
int xAng, yAng, zAng;

unsigned long MyMap(unsigned long x, unsigned long in_min, unsigned long in_max, unsigned long out_min, unsigned long out_max) {

     return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

//long map(long x, long in_min, long in_max, long out_min, long out_max)
//{
//  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
//}
void setup(){
    Serial.println("hi");
  Serial.begin(9600);
  Wire.begin(22, 23); 
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
//  Serial.println("hi");
  Wire.end();
  Wire.begin(16, 17);
//    Serial.println("hi"); 
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
  Wire.end();
}
int i = 0;
void loop(){
  // Flex
  while(Serial.available()){
    Serial.read();
    i++;
  }
  if (i%2 == 0){
  
  Serial.print("[");
//  Serial.println(analogRead(Thumb_pin));
  if(analogRead(Thumb_pin) < 600){
  
    Thumb = 1;
  }
  else{
    Thumb = 0;
  }
// Serial.println(analogRead(Index_pin));
  if(analogRead(Index_pin) < 1100){
    Index = 1;
  }
  else{
    Index = 0;
  }

  if(analogRead(Middle_pin) < 1100){
    Middle = 1;
  }
  else{
    Middle = 0;
  }

  if(analogRead(Ring_pin) < 1100){
    Ring = 1;
  }
  else
  {
    Ring = 0;
  }

  if(analogRead(Little_pin) < 1100){
    Little = 1;
  }
  else{
    Little = 0;
  }

  Serial.print(Thumb);
  Serial.print(",");
  Serial.print(Index);
  Serial.print(",");
  Serial.print(Middle);
  Serial.print(",");
  Serial.print(Ring);
  Serial.print(",");
  Serial.print(Little);
  Serial.print(",");
  // GyroScope 1
  Wire.begin(gyro1_sda, gyro1_scl); 
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);

  //Reading Accelometer Values
  AcX=Wire.read()<<8|Wire.read();
  AcY=Wire.read()<<8|Wire.read();
  AcZ=Wire.read()<<8|Wire.read();

//  Wire.end();
//
  // Calaculating Angle in Radians
  xAng = map(AcX,minVal,maxVal,-90,90);
  yAng = map(AcY,minVal,maxVal,-90,90);
  zAng = map(AcZ,minVal,maxVal,-90,90);

  x= RAD_TO_DEG * (atan2(-yAng, -zAng)+PI);
  y= RAD_TO_DEG * (atan2(-xAng, -zAng)+PI);
  z= RAD_TO_DEG * (atan2(-yAng, -xAng)+PI);

  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.print(z);
  Serial.println(",");


  Wire.begin(gyro2_sda, gyro2_scl); 
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);

  AcX=Wire.read()<<8|Wire.read();
  AcY=Wire.read()<<8|Wire.read();
  AcZ=Wire.read()<<8|Wire.read();

  Wire.end();

  xAng = map(AcX,minVal,maxVal,-90,90);
  yAng = map(AcY,minVal,maxVal,-90,90);
  zAng = map(AcZ,minVal,maxVal,-90,90);

  x= RAD_TO_DEG * (atan2(-yAng, -zAng)+PI);
  y= RAD_TO_DEG * (atan2(-xAng, -zAng)+PI);
  z= RAD_TO_DEG * (atan2(-yAng, -xAng)+PI);

  Serial.print(x);
  Serial.print(",");
  Serial.print(y);
  Serial.print(",");
  Serial.print(z);
  Serial.println("],");
  }
  delay(100);
}
