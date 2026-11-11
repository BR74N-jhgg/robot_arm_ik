import serial
import time
import numpy as np
from config import arm_chain

# Hardware Constants for 28BYJ-48 (Half-step mode)
TOTAL_STEPS_PER_REV = 4096.0

esp32 = serial.Serial('/dev/cu.usbserial-10', 115200, timeout=1)
time.sleep(2) # Wait for ESP32 to reboot

def rad_to_steps(radians):
    """Converts IK radians to absolute stepper motor steps."""
    revolutions = radians / (2 * np.pi)
    return int(revolutions * TOTAL_STEPS_PER_REV)

def move_to_target(x, y, z):
    target_position = [x, y, z]
    
    # 1. Calculate Inverse Kinematics
    ik_angles = arm_chain.inverse_kinematics(target_position)
    
    # 2. Check if the target is actually reachable (Fix 3)
    predicted_position = arm_chain.forward_kinematics(ik_angles)[:3, 3]
    error = np.linalg.norm(predicted_position - target_position)
    if error > 0.005:  # 5 mm tolerance
        print(f"ERR: Target {target_position} unreachable. Error: {error:.4f}m")
        return
    
    # 3. Convert to Motor Steps
    base_steps = rad_to_steps(ik_angles[1])
    shoulder_steps = rad_to_steps(ik_angles[2])
    elbow_steps = rad_to_steps(ik_angles[3])
    
    # 4. Format and Send the Serial Command
    command = f"{base_steps},{shoulder_steps},{elbow_steps}\n"
    esp32.write(command.encode('utf-8'))
    
    response = esp32.readline().decode('utf-8').strip()
    print(f"Sent: {command.strip()} | ESP32 Reply: {response}")

if __name__ == "__main__":
    print("Moving to position 1...")
    move_to_target(0.131, 0.076, 0.131)
    time.sleep(3)
    
    print("Moving to position 2...")
    move_to_target(0.10, 0.10, 0.10)