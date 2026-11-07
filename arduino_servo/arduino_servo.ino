#include <ESP32Servo.h>
const int N = 3;
int pins[N] = {13, 14, 27};   // base, shoulder, elbow
Servo s[N];
void setup() {
  Serial.begin(115200);
  for (int i = 0; i < N; i++) {
    s[i].setPeriodHertz(50);
    s[i].attach(pins[i], 500, 2400);
    s[i].write(90);
  }
}
void loop() {
  if (Serial.available()) {
    for (int i = 0; i < N; i++) s[i].write(constrain(Serial.parseInt(), 0, 180));
    while (Serial.available() && Serial.read() != '\n') {}
  }
}