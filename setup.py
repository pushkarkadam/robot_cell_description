from setuptools import find_packages, setup
import os 
from glob import glob

package_name = 'robot_cell_description'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.stl')),
        (os.path.join('share', package_name, 'meshes', 'collision', '2f_85'), glob('meshes/collision/2f_85/*')),
        (os.path.join('share', package_name, 'meshes', 'visual', '2f_85'), glob('meshes/visual/2f_85/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Pushkar Kadam',
    maintainer_email='pushkarkadam17@outlook.com',
    description='UR robot cell description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
