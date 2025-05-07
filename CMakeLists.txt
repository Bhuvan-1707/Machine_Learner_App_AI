cmake_minimum_required(VERSION 3.15)
project(MyApp)

# Specify Pybind11 location if not installed system-wide
set(pybind11_DIR "/home/bhuvandiya/Machine_Learner/venv/lib/python3.13/site-packages/pybind11/share/cmake/pybind11")

# Find Python and Pybind11
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 REQUIRED)

# Add the Pybind11 module
pybind11_add_module(simplecalc cpp/simplecalc.cpp)

# Install to virtualenv's site-packages
set_target_properties(simplecalc PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${Python3_SITEARCH}
)
