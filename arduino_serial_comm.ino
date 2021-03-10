#define led 7
int data;

void setup()
{
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  digitalWrite(led, LOW);
}

void loop()
{
  while( Serial.available()> 0)
  {
    data = Serial.read();

    if (data == '1')
    {
      digitalWrite(led, HIGH);
      
    }
    else if (data == '0')
    {
      digitalWrite(led, LOW);
      
    }
  }
}
