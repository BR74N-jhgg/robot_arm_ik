#include <Arduino.h>
#include <AccelStepper.h>

// Define Stepper Pins for 3x 28BYJ-48 via ULN2003 drivers
// Each motor requires 4 pins (12 pins total for 3 axes).
// Use safe ESP32 GPIO pins (avoiding strapping/input-only pins).

// Base Motor Pins
#define BASE_IN1 13
#define BASE_IN2 14
#define BASE_IN3 27
#define BASE_IN4 26

// Shoulder Motor Pins
#define SHOULDER_IN1 25
#define SHOULDER_IN2 33
#define SHOULDER_IN3 32
#define SHOULDER_IN4 15

// Elbow Motor Pins
#define ELBOW_IN1 2
#define ELBOW_IN2 4
#define ELBOW_IN3 16
#define ELBOW_IN4 17

// Initialize AccelStepper for 4-wire mode (HALF4WIRE recommended for 28BYJ-48 torque)
// CRITICAL: The AccelStepper library requires the pin sequence for the ULN2003 
// to be passed as IN1, IN3, IN2, IN4 to energize the coils in the correct order.
AccelStepper baseStepper(AccelStepper::HALF4WIRE, BASE_IN1, BASE_IN3, BASE_IN2, BASE_IN4);
AccelStepper shoulderStepper(AccelStepper::HALF4WIRE, SHOULDER_IN1, SHOULDER_IN3, SHOULDER_IN2, SHOULDER_IN4);
AccelStepper elbowStepper(AccelStepper::HALF4WIRE, ELBOW_IN1, ELBOW_IN3, ELBOW_IN2, ELBOW_IN4);

const int NUM_JOINTS = 3;
long targetSteps[NUM_JOINTS] = {0, 0, 0};

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);

  // 28BYJ-48 max speeds are much slower than NEMA 17. 
  // Max reliable speed is usually around 500-1000 steps per second before stalling.
  baseStepper.setMaxSpeed(500.0);
  baseStepper.setAcceleration(200.0);
  
  shoulderStepper.setMaxSpeed(500.0);
  shoulderStepper.setAcceleration(200.0);
  
  elbowStepper.setMaxSpeed(500.0);
  elbowStepper.setAcceleration(200.0);
}

void loop() {
  // 1. Check for incoming serial commands
  if (Serial.available() > 0) {
    String incomingData = Serial.readStringUntil('\n');
    incomingData.trim();
    
    if (incomingData.length() > 0) {
      long val1, val2, val3;
      
      // Parse the 3 values
      int parsedCount = sscanf(incomingData.c_str(), "%ld,%ld,%ld", &val1, &val2, &val3);
      
      // Only apply if the entire message is valid
      if (parsedCount == NUM_JOINTS) {
        targetSteps[0] = val1;
        targetSteps[1] = val2;
        targetSteps[2] = val3;
        
        baseStepper.moveTo(targetSteps[0]);
        shoulderStepper.moveTo(targetSteps[1]);
        elbowStepper.moveTo(targetSteps[2]);
        
        Serial.println("OK");
      } else {
        Serial.println("ERR: Invalid format");
        // Flush buffer to prevent cascading read errors
        while(Serial.available()) { Serial.read(); }
      }
    }
  }

  // 2. Execute stepper movements continuously
  baseStepper.run();
  shoulderStepper.run();
  elbowStepper.run();
}