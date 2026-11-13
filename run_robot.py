import serial
import time
import numpy as np
from config import arm_chain

# Hardware Constants for 28BYJ-48 (Half-step mode)
TOTAL_STEPS_PER_REV = 4096.0

# Adjust to match your Mac's exact serial port
esp32 = serial.Serial('/dev/cu.usbserial-10', 115200, timeout=1)
time.sleep(2) # Wait for ESP32 to reboot

# Track current angles starting at straight-up origin (Origin, Base, Shoulder, Elbow, Tip)
current_angles = [0.0] * len(arm_chain.links)

def rad_to_steps(radians, gear_ratio=1.0, direction=1):
    """Converts IK radians to absolute stepper motor steps with gear reduction."""
    revolutions = radians / (2 * np.pi)
    return int(revolutions * TOTAL_STEPS_PER_REV * gear_ratio * direction)

def move_to_target(x, y, z):
    global current_angles
    target_position = [x, y, z]
    
    # 1. Calculate Inverse Kinematics from last known position
    ik_angles = arm_chain.inverse_kinematics(target_position, initial_position=current_angles)
    
    # 2. Check if the target is actually reachable
    predicted_position = arm_chain.forward_kinematics(ik_angles)[:3, 3]
    error = np.linalg.norm(predicted_position - target_position)
    if error > 0.005:  # 5 mm tolerance
        print(f"ERR: Target {target_position} unreachable. Error: {error:.4f}m")
        return
        
    current_angles = ik_angles
    
    # 3. Convert to Motor Steps (Set gear_ratio=1.0, direction=1 for any un-geared joint)
    base_steps = rad_to_steps(ik_angles[1], gear_ratio=1.0, direction=1)
    shoulder_steps = rad_to_steps(ik_angles[2], gear_ratio=4.0, direction=-1)
    elbow_steps = rad_to_steps(ik_angles[3], gear_ratio=1.0, direction=1)
    
    # 4. Format and Send the Serial Command
    command = f"{base_steps},{shoulder_steps},{elbow_steps}\n"
    esp32.write(command.encode('utf-8'))
    
    response = esp32.readline().decode('utf-8').strip()
    print(f"Sent: {command.strip()} | ESP32 Reply: {response}")

if __name__ == "__main__":
    assert rad_to_steps(np.pi, gear_ratio=4.0, direction=-1) == -8192
    print("Robot Arm IK Controller Ready.")
    print("Enter coordinates in meters separated by spaces (e.g., 0.15 0.0 0.15)")
    print("Type 'q' to quit.")
    
    while True:
        user_input = input("\nEnter X Y Z: ").strip()
        
        if user_input.lower() in ['q', 'quit', 'exit']:
            print("Exiting...")
            break
            
        try:
            coords = list(map(float, user_input.split()))
            if len(coords) != 3:
                print("ERR: Please enter exactly three numbers.")
                continue
            move_to_target(coords[0], coords[1], coords[2])
        except ValueError:
            print("ERR: Invalid input. Please enter numbers like: 0.15 0 0.1")