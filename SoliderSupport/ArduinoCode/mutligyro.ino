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

double x, y, z;
int xAng, yAng, zAng;

void setup(){
  Serial.begin(9600);
}

void loop(){

  Serial.println("Gyro 1");
  Wire.begin(gyro1_sda, gyro1_scl); 
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);

  //Reading Accelometer Values
  AcX=Wire.read()<<8|Wire.read();
  AcY=Wire.read()<<8|Wire.read();
  AcZ=Wire.read()<<8|Wire.read();

  Wire.end();

  // Calaculating Angle in Radians
  xAng = map(AcX,minVal,maxVal,-90,90);
  yAng = map(AcY,minVal,maxVal,-90,90);
  zAng = map(AcZ,minVal,maxVal,-90,90);

  x= RAD_TO_DEG * (atan2(-yAng, -zAng)+PI);
  y= RAD_TO_DEG * (atan2(-xAng, -zAng)+PI);
  z= RAD_TO_DEG * (atan2(-yAng, -xAng)+PI);

  Serial.print("AngleX= ");
  Serial.println(x);

  Serial.print("AngleY= ");
  Serial.println(y);

  Serial.print("AngleZ= ");
  Serial.println(z);
  Serial.println("-----------------------------------------");

  Serial.println("Gyro 2");
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

  Serial.print("AngleX= ");
  Serial.println(x);

  Serial.print("AngleY= ");
  Serial.println(y);

  Serial.print("AngleZ= ");
  Serial.println(z);
  Serial.println("-----------------------------------------");
  
  delay(1000);
}
