cmake_minimum_required(VERSION 2.9)
 # 工程vscode_cmake
project(vscode_cmake)
 
#dubug 模式
set (CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} -g")
 
set(SRC_LIST main.cpp)
# 可执行程序 result
add_executable(result ${SRC_LIST})