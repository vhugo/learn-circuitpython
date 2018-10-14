int ledPin = 13;

void setup() {
  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Wait to receive input
  while(Serial.available() == 0);

  // Read the input
  int val = Serial.read() - '0';

  if (val == 1) {
    Serial.println("Led is On");
    digitalWrite(ledPin, HIGH);
  }

  else if (val == 0){
    Serial.println("Led is Off");
    digitalWrite(ledPin, LOW);
  }

  else {
    Serial.println("Invalid!");
  }

  // Echo the input
  //  Serial.println(val);
}
