# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/clion-2017.2.3/bin/cmake/bin/cmake

# The command to remove a file.
RM = /opt/clion-2017.2.3/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/RubixCubeDetection.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/RubixCubeDetection.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/RubixCubeDetection.dir/flags.make

CMakeFiles/RubixCubeDetection.dir/main.cpp.o: CMakeFiles/RubixCubeDetection.dir/flags.make
CMakeFiles/RubixCubeDetection.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/RubixCubeDetection.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/RubixCubeDetection.dir/main.cpp.o -c /home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection/main.cpp

CMakeFiles/RubixCubeDetection.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/RubixCubeDetection.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection/main.cpp > CMakeFiles/RubixCubeDetection.dir/main.cpp.i

CMakeFiles/RubixCubeDetection.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/RubixCubeDetection.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection/main.cpp -o CMakeFiles/RubixCubeDetection.dir/main.cpp.s

CMakeFiles/RubixCubeDetection.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/RubixCubeDetection.dir/main.cpp.o.requires

CMakeFiles/RubixCubeDetection.dir/main.cpp.o.provides: CMakeFiles/RubixCubeDetection.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/RubixCubeDetection.dir/build.make CMakeFiles/RubixCubeDetection.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/RubixCubeDetection.dir/main.cpp.o.provides

CMakeFiles/RubixCubeDetection.dir/main.cpp.o.provides.build: CMakeFiles/RubixCubeDetection.dir/main.cpp.o


# Object files for target RubixCubeDetection
RubixCubeDetection_OBJECTS = \
"CMakeFiles/RubixCubeDetection.dir/main.cpp.o"

# External object files for target RubixCubeDetection
RubixCubeDetection_EXTERNAL_OBJECTS =

RubixCubeDetection: CMakeFiles/RubixCubeDetection.dir/main.cpp.o
RubixCubeDetection: CMakeFiles/RubixCubeDetection.dir/build.make
RubixCubeDetection: /usr/local/lib/libopencv_stitching.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_superres.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_videostab.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_aruco.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_bgsegm.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_bioinspired.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_ccalib.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_cvv.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_dpm.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_face.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_freetype.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_fuzzy.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_hdf.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_img_hash.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_line_descriptor.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_optflow.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_reg.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_rgbd.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_saliency.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_sfm.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_stereo.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_structured_light.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_surface_matching.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_tracking.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_xfeatures2d.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_ximgproc.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_xobjdetect.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_xphoto.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_photo.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_shape.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_calib3d.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_phase_unwrapping.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_video.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_datasets.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_plot.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_text.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_dnn.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_features2d.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_flann.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_highgui.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_ml.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_videoio.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_imgcodecs.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_objdetect.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_imgproc.so.3.3.1
RubixCubeDetection: /usr/local/lib/libopencv_core.so.3.3.1
RubixCubeDetection: CMakeFiles/RubixCubeDetection.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable RubixCubeDetection"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/RubixCubeDetection.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/RubixCubeDetection.dir/build: RubixCubeDetection

.PHONY : CMakeFiles/RubixCubeDetection.dir/build

CMakeFiles/RubixCubeDetection.dir/requires: CMakeFiles/RubixCubeDetection.dir/main.cpp.o.requires

.PHONY : CMakeFiles/RubixCubeDetection.dir/requires

CMakeFiles/RubixCubeDetection.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/RubixCubeDetection.dir/cmake_clean.cmake
.PHONY : CMakeFiles/RubixCubeDetection.dir/clean

CMakeFiles/RubixCubeDetection.dir/depend:
	cd /home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection /home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection /home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection/cmake-build-debug /home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection/cmake-build-debug /home/CS/users/pwarren/COS351-CV/cube-solver/RubiksCubeDetection/cmake-build-debug/CMakeFiles/RubixCubeDetection.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/RubixCubeDetection.dir/depend

