Robot Cell Description
======================

This project assembles UR10e robot with Robotiq gripper and a pointer tool.

Get started
-----------

.. code-block:: bash

    # Change to the workspace directory
    cd ~/ros2_ws
    source install/setup.bash
    
    # build repository
    colcon build --packages-select robot_cell_description

To launch joint states and rviz execute the following:

.. code-block:: bash

    ros2 launch robot_cell_description view_robot.launch.py