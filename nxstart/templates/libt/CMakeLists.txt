cmake_minimum_required(VERSION 3.9)
project(FOLDER_NAME_PLACEHOLDER)

set(CMAKE_CXX_STANDARD 11)

include_directories($ENV{LIBTRANSISTOR_HOME}/lib)
include_directories($ENV{LIBTRANSISTOR_HOME}/include)
link_directories($ENV{LIBTRANSISTOR_HOME}/lib)
link_directories($ENV{LIBTRANSISTOR_HOME}/include)

add_executable(FOLDER_NAME_PLACEHOLDER source/main.cpp)
