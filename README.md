# Robot Arm IK (IKPy)
1. Install Python 3.8+, then in this folder:  `pip install -r requirements.txt`
2. Edit `config.py` with your arm's measurements. Calibrate `SERVO_OFFSET` and
   `SERVO_DIR` for your installed servos before using servo output.
3. `python demo.py 0.005 0.170 0.115`  -> joint angles + 3D plot
4. `python evaluate.py`             -> accuracy/speed results for your report
5. `python run_robot.py --sim`      -> interactive test without hardware
6. Upload `arduino_servo/arduino_servo.ino` (servos on pins 9,10,11), set SERIAL_PORT in config.py, run `python run_robot.py`
Safety: test small moves first; use an external 5-6V supply for servos, not the Arduino 5V pin.
