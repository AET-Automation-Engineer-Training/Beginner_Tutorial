cmake_minimum_required(VERSION 3.0.2)
project(vocie_demo)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES camera
#  CATKIN_DEPENDS roscpp rospy std_msg
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


#############
## Install ##
#############

 catkin_install_python(PROGRAMS
   scripts/*.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )

#############
## Testing ##
#############

