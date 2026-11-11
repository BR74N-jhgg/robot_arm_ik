#include "Gripper.h"

void Gripper::setup(int pin) {
    // SG90 micro servos need specific min/max pulse widths
    servo.attach(pin, 500, 2400); 
}

void Gripper::setAngle(int angle) {
    servo.write(angle);
}