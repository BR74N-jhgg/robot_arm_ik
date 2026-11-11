import ikpy.chain
import ikpy.link
import numpy as np

# 3-Axis Kinematic Chain based on updated joint and tool offsets
arm_chain = ikpy.chain.Chain(name='3_axis_arm', links=[
    # Base Link (Fixed to ground)
    ikpy.link.OriginLink(),

    # Joint 1: Base Pan
    ikpy.link.URDFLink(
        name="base_pan",
        origin_translation=[0.0, 0.0, 0.110], 
        origin_orientation=[0, 0, 0],
        rotation=[0, 0, 1],
        bounds=(-np.pi, np.pi) 
    ),

    # Joint 2: Shoulder Pitch
    ikpy.link.URDFLink(
        name="shoulder_pitch",
        origin_translation=[0.06211, 0.0, 0.0], 
        origin_orientation=[0, 0, 0],
        rotation=[0, 1, 0],
        bounds=(-np.pi, np.pi)
    ),

    # Joint 3: Elbow Pitch
    ikpy.link.URDFLink(
        name="elbow_pitch",
        origin_translation=[0.0, 0.059, 0.070], 
        origin_orientation=[0, 0, 0],
        rotation=[0, 1, 0],
        bounds=(-np.pi, np.pi)
    ),

    # Tip / End Effector
    ikpy.link.URDFLink(
        name="claw_tip",
        origin_translation=[0.099, 0.01233, -0.0034], 
        origin_orientation=[0, 0, 0],
        rotation=[0, 0, 0]
    )
])