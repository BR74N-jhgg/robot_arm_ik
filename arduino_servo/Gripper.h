#pragma once
#include <ESP32Servo.h>

class Gripper {
public:
    void setup(int pin);
    void setAngle(int angle);

private:
    Servo servo;
};