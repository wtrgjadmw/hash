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
include test/CMakeFiles/test_md.dir/depend.make

# Include the progress variables for this target.
include test/CMakeFiles/test_md.dir/progress.make

# Include the compile flags for this target's objects.
include test/CMakeFiles/test_md.dir/flags.make

test/CMakeFiles/test_md.dir/test_md.c.o: test/CMakeFiles/test_md.dir/flags.make
test/CMakeFiles/test_md.dir/test_md.c.o: /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main/test/test_md.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object test/CMakeFiles/test_md.dir/test_md.c.o"
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/test_md.dir/test_md.c.o   -c /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main/test/test_md.c

test/CMakeFiles/test_md.dir/test_md.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test_md.dir/test_md.c.i"
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main/test/test_md.c > CMakeFiles/test_md.dir/test_md.c.i

test/CMakeFiles/test_md.dir/test_md.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test_md.dir/test_md.c.s"
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main/test/test_md.c -o CMakeFiles/test_md.dir/test_md.c.s

# Object files for target test_md
test_md_OBJECTS = \
"CMakeFiles/test_md.dir/test_md.c.o"

# External object files for target test_md
test_md_EXTERNAL_OBJECTS =

bin/test_md: test/CMakeFiles/test_md.dir/test_md.c.o
bin/test_md: test/CMakeFiles/test_md.dir/build.make
bin/test_md: lib/librelic_s.a
bin/test_md: test/CMakeFiles/test_md.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable ../bin/test_md"
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_md.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/CMakeFiles/test_md.dir/build: bin/test_md

.PHONY : test/CMakeFiles/test_md.dir/build

test/CMakeFiles/test_md.dir/clean:
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test && $(CMAKE_COMMAND) -P CMakeFiles/test_md.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/test_md.dir/clean

test/CMakeFiles/test_md.dir/depend:
	cd /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-main/test /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test /usr1/anawin/Desktop/ABE_software/00.RELIC/test/relic-target/test/CMakeFiles/test_md.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/test_md.dir/depend

