# ===== EDIT THESE TO MATCH YOUR ARM =====
import numpy as np
# Each joint: name, offset from previous joint [x,y,z] in metres, rotation axis, limits (deg)
JOINTS = [
    ("base",     [0, 0, 0.00], [0, 0, 1], (-180, 180)),
    ("shoulder", [0, 0.070, 0.0], [0, 1, 0], (-60, 60)),
    #("elbow",    [0, 0, 0.0115], [0, 1, 0], (-90, 90)),
]
TOOL_OFFSET = [0, 0.080, 0]      # last joint -> gripper tip (metres)
SERIAL_PORT = "COM4"            # Mac: "/dev/tty.usbmodemXXXX"
BAUD = 115200
SERVO_OFFSET = [90, 90, 90]     # servo degrees when joint angle = 0
SERVO_DIR = [1, 1, 1]           # set -1 if a servo turns the wrong way
