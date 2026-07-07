from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription, ExecuteProcess, RegisterEventHandler
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.event_handlers import OnProcessStart
from launch.substitutions import LaunchConfiguration, Command
from launch.conditions import IfCondition
import os
import launch

def generate_launch_description():
    get_nav2_pkg = get_package_share_directory("go2_navigation2")
    get_bringup_pkg = get_package_share_directory("nav2_bringup")

    use_sim_time = launch.substitutions.LaunchConfiguration('use_sim_time', default='false')
    # map_yaml_path = launch.substitutions.LaunchConfiguration(
    #     'map', default=os.path.join(get_nav2_pkg, 'maps', '01map.yaml'))
    map_yaml_path = launch.substitutions.LaunchConfiguration('map', default=os.path.join('4floor_first_map.yaml'))
    nav2_param_path = launch.substitutions.LaunchConfiguration('params_file', default=os.path.join(get_nav2_pkg, 'config', 'nav2_params.yaml'))

    # 包含nav2的launch文件
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_bringup_pkg, "launch", "navigation_launch.py")),
        launch_arguments=[("params_file", nav2_param_path), ("use_sim_time", use_sim_time), ("map", map_yaml_path)]
    )

    return LaunchDescription([
        nav2_launch
    ])