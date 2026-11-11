#include <Arduino.h>
#include "StepperController.h"
#include "Gripper.h"

StepperController arm;
Gripper claw;

String incomingData = "";

void setup() {
  Serial.begin(115200);
  
  arm.setup();
  claw.setup(5); // Assuming gripper is on GPIO 5
}

void loop() {
  while (Serial.available() > 0) {
    char c = Serial.read();
    
    if (c == '\n') {
      incomingData.trim();
      if (incomingData.length() > 0) {
        long val1, val2, val3;
        
        if (sscanf(incomingData.c_str(), "%ld,%ld,%ld", &val1, &val2, &val3) == 3) {
          arm.setTargets(val1, val2, val3);
          Serial.println("OK");
        } else {
          Serial.println("ERR: Invalid format");
        }
      }
      incomingData = "";
    } else {
      incomingData += c;
    }
  }

  arm.update();
}