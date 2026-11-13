import ikpy.chain
import ikpy.link
import numpy as np

arm_chain = ikpy.chain.Chain(
    name='3_axis_arm',
    active_links_mask=[False, True, True, True, False],
    links=[
        # 0. Base Link (Fixed to ground)
        ikpy.link.OriginLink(),

        # 1. Joint 1: Base Pan
        ikpy.link.URDFLink(
            name="base_pan",
            origin_translation=[0.0, 0.0, 0.110],
            origin_orientation=[0, 0, 0],
            rotation=[0, 0, 1],
            bounds=(-np.pi, np.pi)
        ),

        # 2. Joint 2: Shoulder Pitch
        ikpy.link.URDFLink(
            name="shoulder_pitch",
            origin_translation=[0.06211, 0.0, 0.0],
            origin_orientation=[0, 0, 0],
            rotation=[0, 1, 0],
            bounds=(-np.pi, np.pi)
        ),

        # 3. Joint 3: Elbow Pitch (Pointing straight up at 0 rad)
        ikpy.link.URDFLink(
            name="elbow_pitch",
            origin_translation=[0.0, 0.059, 0.070],
            origin_orientation=[0, -np.pi/2, 0],
            rotation=[0, 1, 0],
            bounds=(-np.pi, np.pi)
        ),

        # 4. Tip / End Effector (Fixed structural offset)
        ikpy.link.URDFLink(
            name="claw_tip",
            origin_translation=[0.099, 0.01233, -0.0034],
            origin_orientation=[0, 0, 0],
            rotation=None,
            joint_type='fixed'
        )
    ]
)

assert len(arm_chain.links) == 5