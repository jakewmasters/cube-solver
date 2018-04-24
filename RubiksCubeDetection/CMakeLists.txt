cmake_minimum_required(VERSION 2.8.4)
project(RubiksCubeDetection)
find_package( OpenCV REQUIRED )
include_directories(${OpenCV_INCLUDE_DIRS})
add_executable(RubiksCubeDetection main.cpp)
target_link_libraries( RubiksCubeDetection ${OpenCV_LIBS} )

