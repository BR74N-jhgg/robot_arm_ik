#pragma once
#include <AccelStepper.h>
#include <MultiStepper.h>

class StepperController {
public:
    StepperController();
    void setup();
    void setTargets(long base, long shoulder, long elbow);
    void update();
    bool isMoving();

private:
    AccelStepper baseStepper;
    AccelStepper shoulderStepper;
    AccelStepper elbowStepper;
    MultiStepper coordinator;
    long targets[3];
};