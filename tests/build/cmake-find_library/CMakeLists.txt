cmake_minimum_required(VERSION 3.6.0)

add_library(native-lib SHARED jni/foo.cpp)
find_library(log-lib log)
target_link_libraries(native-lib ${log-lib})
