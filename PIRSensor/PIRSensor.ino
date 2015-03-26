int Sensval;

void setup()
{
  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(13, OUTPUT);
}

void loop()
{
  Sensval = digitalRead(2);
  if (Sensval)
    Serial.println(Sensval);
  delay(100);
}
