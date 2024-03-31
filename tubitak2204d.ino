#include <LiquidCrystal.h>

int veri;
int muslukMotor = 8;
int depoMotor = 9;
int toprakSensor = 6;
int bahceMotor = 7;
int potPin = A1;
int potDeger = 0;
float istSicaklik = 0;
int lm35Pin = A0;
int okunan_deger = 0;
float sicaklik_gerilim = 0;
float sicaklik = 0;

LiquidCrystal lcd_1(12, 11, 5, 4, 3, 2);

void setup() 
{
  pinMode(toprakSensor, INPUT);
  pinMode(bahceMotor, OUTPUT);
  Serial.begin(9600);
  lcd_1.begin(16, 2);
  lcd_1.print("SICAKLIK: ");
}
 
void loop()
{
  okunan_deger = analogRead(lm35Pin);
  sicaklik_gerilim = (okunan_deger / 1023.0)*5000;
  sicaklik = sicaklik_gerilim /10.0; 
  lcd_1.setCursor(10, 0);
  lcd_1.print(sicaklik);
  
  potDeger = analogRead(potPin);
  istSicaklik = (potDeger/1023.0)*70+20;
  lcd_1.setCursor(0, 1);
  lcd_1.print("HEDEF: ");
  lcd_1.setCursor(10, 1);
  lcd_1.print(istSicaklik);
  
  if(sicaklik < istSicaklik){
  	digitalWrite(depoMotor, HIGH);
    digitalWrite(muslukMotor, LOW);
  }
  else{
    digitalWrite(depoMotor, LOW);
    digitalWrite(muslukMotor, HIGH);
  }
  
  veri = digitalRead(toprakSensor);
  if(veri == true){
    digitalWrite(bahceMotor, HIGH);
  }
  else{
    digitalWrite(bahceMotor, LOW);
  }
}
