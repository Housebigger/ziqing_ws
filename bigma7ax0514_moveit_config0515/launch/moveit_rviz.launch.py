from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_moveit_rviz_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("bigma7ax0514", package_name="bigma7ax0514_moveit_config0515").to_moveit_configs()
    return generate_moveit_rviz_launch(moveit_config)
