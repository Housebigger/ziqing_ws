from setuptools import setup
from glob import glob 
import os 

package_name = 'bigmama0306_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/**')), 
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*.STL'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hyh',
    maintainer_email='hyh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

