#include <Servo.h>
#include <dht.h>

dht DHT;
int dht_apin = 2;
int smokeA0 = A5;
int servopin = 10;
int servopos = 180;
int servopin1 = 9;
int servopos1 = 0;
Servo myServo;
Servo myServo1;
int LDRPin = A1;
int LDRValue = 0;
int d2sensorThres;
int ldrsensorthres;
int tempsensorthres;
int humsensorthres;
bool windowstat;
bool lock;
void setup() {
  Serial.flush();
  delay(500);//Delay to let system boot
  pinMode(smokeA0, INPUT);
  pinMode(4, OUTPUT);
  myServo.attach(servopin);
  myServo1.attach(servopin1);
  myServo.write(servopos);
  myServo1.write(servopos1); 
  delay(1000);//Wait before accessing Sensor
  digitalWrite(4, HIGH);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
  String data = Serial.readStringUntil('\n');
  Serial.print("You sent me: ");
  Serial.println(data);
  delay(1000);
  String delimiter = ":";
  String key = data.substring(0, data.indexOf(delimiter));
  if (key.equals("start")){
  int f = data.indexOf(delimiter);
  data.remove(0, f+1);
  String token = data.substring(0, data.indexOf(delimiter));
  d2sensorThres = token.toInt(); //1
  Serial.print("recieved d2 sensor: ");
  Serial.println(d2sensorThres);
  delay(1000);
  f = data.indexOf(delimiter);
  data.remove(0, f+1);
  token = data.substring(0, data.indexOf(delimiter));
  ldrsensorthres = token.toInt(); //2
  Serial.print("recieved ldr sensor: ");
  Serial.println(ldrsensorthres);
  delay(1000);
  f = data.indexOf(delimiter);
  data.remove(0, f+1); 
  token = data.substring(0, data.indexOf(delimiter));
  tempsensorthres = token.toInt(); //3
  Serial.print("recieved tempreture sensor: ");
  Serial.println(tempsensorthres);
  delay(1000);
  f = data.indexOf(delimiter);
  data.remove(0, f+1);
  token = data.substring(0, data.indexOf(delimiter));
  humsensorthres = token.toInt(); //4
  Serial.print("recieved humidity sensor: ");
  Serial.println(humsensorthres);
  Serial.println("done");
  delay(1000);
  int rain = analogRead(A2);
  Serial.println(rain);
  int analogSensor = analogRead(smokeA0);
  Serial.print("gas levels: ");
  Serial.println(analogSensor);
  delay(1000);
  LDRValue = analogRead(LDRPin); // read the value from the sensor
  Serial.print("light intensity: ");
  Serial.println(LDRValue); //prints the values coming from the sensor on the screen
  if (LDRValue < ldrsensorthres) {
    digitalWrite(4, LOW);
    Serial.println("light intensity below threshold value, opening light system");
  }
  else {
    digitalWrite(4, HIGH);
    Serial.println("light intensity is ok, light system is off");
  }
  delay(1000);
  //start of dht 11 sensor
  DHT.read11(dht_apin);
  Serial.print("Current humidity = ");
  Serial.print(DHT.humidity);
  Serial.print("%  ");
  Serial.print("temperature = ");
  Serial.print(DHT.temperature);
  Serial.println("C  ");
  if (DHT.humidity > humsensorthres || DHT.temperature > tempsensorthres)
  {
    Serial.println("greenhouse humidity or tempreture is above threshold value");
    windowstat = true;
  }
  else
  {
    Serial.println("greenhouse humidity or tempreture is ok");
    windowstat = false;    
  }
  delay(1000);
  //start of rain module
  if(rain < 400)
  {
     lock = true;
    Serial.println("it appears to be raining, locking windows");
  }else
  {
    Serial.println("it doesnt appears to be raining");
    lock = false; 
  }
  delay(1000);
   if (analogSensor > d2sensorThres)
  {
    Serial.println("gas levels are above threshold");
  }
  else
  {
    Serial.println("gas levels are ok");
  }
  delay(1000);
  if ((DHT.humidity > humsensorthres) || (DHT.temperature > tempsensorthres) || (analogSensor > d2sensorThres) || (rain < 500) && (lock == false)){
  
    myServo.write(90);
    myServo1.write(90);
    Serial.println("windows are open");
    windowstat = true;
      
  }else
  {
    myServo.write(servopos);
    myServo1.write(servopos1);
    Serial.println("windows are closed");
    windowstat = false;    
  } 
  delay(1000);



  delay(1000);
  }
  }
}
