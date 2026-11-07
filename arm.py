import numpy as np
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
import config as C

def build_arm():
    links = [OriginLink()]
    for name, off, axis, (lo, hi) in C.JOINTS:
        links.append(URDFLink(name=name, origin_translation=off, origin_orientation=[0, 0, 0],
                              rotation=axis, bounds=(np.radians(lo), np.radians(hi))))
    links.append(URDFLink(name="tip", origin_translation=C.TOOL_OFFSET,
                          origin_orientation=[0, 0, 0], joint_type="fixed"))
    mask = [False] + [True] * len(C.JOINTS) + [False]
    return Chain(name="arm", links=links, active_links_mask=mask)

ARM = build_arm()
N = len(C.JOINTS)

def solve(target, guess=None):
    """Return (joint angles in degrees, error in mm)."""
    full = ARM.inverse_kinematics(target, initial_position=guess)
    reached = ARM.forward_kinematics(full)[:3, 3]
    err = np.linalg.norm(reached - np.array(target)) * 1000
    return np.degrees(full[1:1 + N]), err, full

def to_servo(deg):
    return [int(np.clip(C.SERVO_OFFSET[i] + C.SERVO_DIR[i] * d, 0, 180)) for i, d in enumerate(deg)]
