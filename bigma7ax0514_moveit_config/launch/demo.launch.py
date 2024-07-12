from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("bigma7ax0514", package_name="bigma7ax0514_moveit_config").to_moveit_configs()
    return generate_demo_launch(moveit_config)
