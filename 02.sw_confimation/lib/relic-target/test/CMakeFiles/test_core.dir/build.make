# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

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
CMAKE_COMMAND = /usr/bin/cmake3

# The command to remove a file.
RM = /usr/bin/cmake3 -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target

# Include any dependencies generated for this target.
include test/CMakeFiles/test_core.dir/depend.make

# Include the progress variables for this target.
include test/CMakeFiles/test_core.dir/progress.make

# Include the compile flags for this target's objects.
include test/CMakeFiles/test_core.dir/flags.make

test/CMakeFiles/test_core.dir/test_core.c.o: test/CMakeFiles/test_core.dir/flags.make
test/CMakeFiles/test_core.dir/test_core.c.o: /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main/test/test_core.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object test/CMakeFiles/test_core.dir/test_core.c.o"
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/test_core.dir/test_core.c.o   -c /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main/test/test_core.c

test/CMakeFiles/test_core.dir/test_core.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_core.dir/test_core.c.i"
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main/test/test_core.c > CMakeFiles/test_core.dir/test_core.c.i

test/CMakeFiles/test_core.dir/test_core.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_core.dir/test_core.c.s"
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main/test/test_core.c -o CMakeFiles/test_core.dir/test_core.c.s

# Object files for target test_core
test_core_OBJECTS = \
"CMakeFiles/test_core.dir/test_core.c.o"

# External object files for target test_core
test_core_EXTERNAL_OBJECTS =

bin/test_core: test/CMakeFiles/test_core.dir/test_core.c.o
bin/test_core: test/CMakeFiles/test_core.dir/build.make
bin/test_core: lib/librelic_s.a
bin/test_core: test/CMakeFiles/test_core.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable ../bin/test_core"
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_core.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/CMakeFiles/test_core.dir/build: bin/test_core

.PHONY : test/CMakeFiles/test_core.dir/build

test/CMakeFiles/test_core.dir/clean:
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test && $(CMAKE_COMMAND) -P CMakeFiles/test_core.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/test_core.dir/clean

test/CMakeFiles/test_core.dir/depend:
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main/test /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test/CMakeFiles/test_core.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/test_core.dir/depend

