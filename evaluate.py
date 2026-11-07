"""Test 50 random targets -> accuracy/speed table for your report."""
import time, numpy as np
from arm import ARM, solve
rng = np.random.default_rng(0); errs, times = [], []
for _ in range(50):
    q = [0] + [rng.uniform(l.bounds[0], l.bounds[1]) for l in ARM.links[1:-1]] + [0]
    t = ARM.forward_kinematics(q)[:3, 3]           # guaranteed reachable
    s = time.perf_counter(); _, e, _ = solve(t); times.append((time.perf_counter() - s) * 1000); errs.append(e)
errs = np.array(errs)
print(f"Success (<5 mm): {(errs<5).mean()*100:.0f}%  Mean error: {errs.mean():.2f} mm  Mean time: {np.mean(times):.1f} ms")
