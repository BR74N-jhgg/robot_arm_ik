# Each joint: name, offset from previous joint [x, y, z] in metres,
# rotation axis, and angle limits in degrees.
JOINTS = [
    ("base_pan", [0.0, 0.0, 0.110], [0, 0, 1], (-180, 180)),
    ("shoulder_pitch", [0.06211, 0.0, 0.0], [0, 1, 0], (-180, 180)),
    ("elbow_pitch", [0.0, 0.059, 0.070], [0, 1, 0], (-180, 180)),
]
TOOL_OFFSET = [0.099, 0.01233, -0.0034]

SERIAL_PORT = "/dev/cu.usbserial-10"  # Set this to the port used by your controller.
BAUD = 115200
SERVO_OFFSET = [90, 90, 90]
SERVO_DIR = [1, 1, 1]
