"""Solve IK for one target and show the arm in 3D.  Usage: python demo.py 0.131 0.076 0.131"""
import sys, matplotlib.pyplot as plt
from ikpy.utils import plot as P
from arm import ARM, solve
t = [float(v) for v in sys.argv[1:4]] if len(sys.argv) == 4 else [0.131, 0.076, 0.131]
deg, err, full = solve(t)
print("Target (m):", t)
print("Joint angles (deg):", [round(float(d), 1) for d in deg])
print(f"Position error: {err:.2f} mm", "(OK)" if err < 5 else "(target may be out of reach)")
fig, ax = P.init_3d_figure(); ARM.plot(full, ax, target=t)
plt.savefig("arm_plot.png"); print("Saved arm_plot.png")
if "--noshow" not in sys.argv: plt.show()
