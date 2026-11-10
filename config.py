import ikpy.chain
import ikpy.link
import numpy as np

arm_chain = ikpy.chain.Chain(name='3_axis_arm', links=[
    # Base Link (Fixed to ground)
    ikpy.link.OriginLink(),

    # Joint 1: Base Pan
    ikpy.link.URDFLink(
        name="base_pan",
        # 110mm height from base bottom to shoulder pivot center
        origin_translation=[0.0, 0.0, 0.6211], 
        origin_orientation=[0, 0, 0],
        rotation=[0, 0, 1], # Rotates around Z
        bounds=(-np.pi, np.pi) 
    ),

    # Joint 2: Shoulder Pitch
    ikpy.link.URDFLink(
        name="shoulder_pitch",
        # 62.11mm horizontal offset from base center to shoulder pivot
        origin_translation=[0.0, 0.0, 0.06211], 
        origin_orientation=[0, 0, 0],
        rotation=[0, 1, 0], # Rotates around Y
        bounds=(-np.pi, np.pi)
    ),

    # Joint 3: Elbow Pitch
    ikpy.link.URDFLink(
        name="elbow_pitch",
        # 70.00mm length from shoulder pivot to elbow pivot
        origin_translation=[0.0, 0.059, 0.070], 
        origin_orientation=[0, 0, 0],
        rotation=[0, 1, 0], # Rotates around Y
        bounds=(-np.pi, np.pi)
    ),

    # Tip / End Effector
    ikpy.link.URDFLink(
        name="claw_tip",
        # 99.00mm length from elbow pivot to claw tip
        origin_translation=[0.099, 0.01233, -0.0034], 
        origin_orientation=[0, 0, 0],
        rotation=[0, 0, 0] # Structural link only
    )
    
])
 