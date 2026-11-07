"""Type targets, arm moves. Usage: python run_robot.py   (add --sim to test without hardware)"""
import sys, time
from arm import solve, to_servo
import config as C
sim = "--sim" in sys.argv
if not sim:
    import serial; ser = serial.Serial(C.SERIAL_PORT, C.BAUD); time.sleep(2)
guess = None
while True:
    try:
        s = input("Target x y z in metres (or q): ").strip()
    except EOFError:
        print("\nNo more input; exiting.")
        break
    if s == "q": break
    try: t = [float(v) for v in s.split()]; assert len(t) == 3
    except Exception: print("Enter 3 numbers, e.g. 0.131 0.076 0.131"); continue
    deg, err, guess = solve(t, guess)
    if err > 5: print(f"Unreachable (error {err:.1f} mm) - not moving"); continue
    cmd = ",".join(map(str, to_servo(deg))) + "\n"
    print("Angles:", [round(float(d), 1) for d in deg], "-> servo cmd:", cmd.strip())
    if not sim: ser.write(cmd.encode())
