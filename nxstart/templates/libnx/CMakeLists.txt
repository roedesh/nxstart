cmake_minimum_required(VERSION 3.9)
project(FOLDER_NAME_PLACEHOLDER)

set(CMAKE_CXX_STANDARD 11)

include_directories($ENV{DEVKITPRO}/libnx/lib)
include_directories($ENV{DEVKITPRO}/libnx/include)
include_directories($ENV{DEVKITARM})
link_directories($ENV{DEVKITPRO}/libnx/lib)
link_directories($ENV{DEVKITPRO}/libnx/include)
add_executable(FOLDER_NAME_PLACEHOLDER source/main.cpp)
