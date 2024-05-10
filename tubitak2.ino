int led2=2;
int led3=3;
int led5=4;
int led7=5;
int led11=6;
int led13=7;
int led17=8;
int led19=9;
int led23=10;
int led29=11;
int led31=12;
int led37=13;
char gelenVeri;

void setup() {
Serial.begin(9600);
pinMode(led2 , OUTPUT);
pinMode(led3 , OUTPUT);
pinMode(led5 , OUTPUT);
pinMode(led7 , OUTPUT);
pinMode(led11 , OUTPUT);
pinMode(led13 , OUTPUT);
pinMode(led17 , OUTPUT);
pinMode(led19 , OUTPUT);
pinMode(led23 , OUTPUT);
pinMode(led29 , OUTPUT);
pinMode(led31 , OUTPUT);
pinMode(led37 , OUTPUT);
}

void loop() {
if (Serial.available()>0){
  gelenVeri=Serial.read();
  if(gelenVeri=='a') digitalWrite(led2 , HIGH)
  else if(gelenVeri=='b') digitalWrite(led3 , HIGH);
  else if(gelenVeri=='c') digitalWrite(led5 , HIGH);
  else if(gelenVeri=='d') digitalWrite(led7 , HIGH);
  else if(gelenVeri=='e') digitalWrite(led11 , HIGH);
  else if(gelenVeri=='f') digitalWrite(led13 , HIGH);
  else if(gelenVeri=='g') digitalWrite(led17 , HIGH);
  else if(gelenVeri=='h') digitalWrite(led19 , HIGH);
  else if(gelenVeri=='i') digitalWrite(led23 , HIGH);
  else if(gelenVeri=='j') digitalWrite(led29 , HIGH);
  else if(gelenVeri=='k') digitalWrite(led31 , HIGH);
  else if(gelenVeri=='l') digitalWrite(led37 , HIGH);
  else if(gelenVeri=='m'){
    digitalWrite(led2 , LOW);
    digitalWrite(led3 , LOW);
    digitalWrite(led5 , LOW);
    digitalWrite(led7 , LOW);
    digitalWrite(led11 , LOW);
    digitalWrite(led13 , LOW);
    digitalWrite(led17 , LOW);
    digitalWrite(led19 , LOW);
    digitalWrite(led23 , LOW);
    digitalWrite(led29 , LOW);
    digitalWrite(led31 , LOW);
    digitalWrite(led37 , LOW);
  }
}
}
