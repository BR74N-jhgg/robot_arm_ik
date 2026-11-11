#include "StepperController.h"

// Note the pin order: IN1, IN3, IN2, IN4 - this is required for 28BYJ-48/ULN2003
StepperController::StepperController() : 
    baseStepper(AccelStepper::HALF4WIRE, 13, 27, 14, 26),
    shoulderStepper(AccelStepper::HALF4WIRE, 25, 32, 33, 15),
    elbowStepper(AccelStepper::HALF4WIRE, 2, 16, 4, 17) {}

void StepperController::setup() {
    // 28BYJ-48 absolute max reliable speed is ~500-1000
    baseStepper.setMaxSpeed(600);
    shoulderStepper.setMaxSpeed(600);
    elbowStepper.setMaxSpeed(600);

    // MultiStepper calculates speeds so all motors finish the move simultaneously
    coordinator.addStepper(baseStepper);
    coordinator.addStepper(shoulderStepper);
    coordinator.addStepper(elbowStepper);
}

void StepperController::setTargets(long base, long shoulder, long elbow) {
    targets[0] = base;
    targets[1] = shoulder;
    targets[2] = elbow;
    coordinator.moveTo(targets);
}

void StepperController::update() {
    coordinator.run();
}

bool StepperController::isMoving() {
    // run() returns true as long as any stepper is still moving to its target
    return coordinator.run();
}