cmake_minimum_required(VERSION 3.1)
# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/..)
SET(OpenCV_DIR /usr/local/lib/cmake/opencv4)

set(QT_VERSION_REQ "5.12")

PROJECT(qt-test)

find_package( OpenCV REQUIRED )

# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)
# Instruct CMake to run moc automatically when needed
set(CMAKE_AUTOMOC ON)
# Create code from a list of Qt designer ui files
set(CMAKE_AUTOUIC ON)

# find_package(Qt5Core)

# Find the QtWidgets library
find_package(Qt5Core CONFIG REQUIRED)
# find_package(Qt5Quick CONFIG REQUIRED)
find_package(Qt5Widgets CONFIG REQUIRED)
find_package(Qt5Gui CONFIG REQUIRED)

QT5_WRAP_UI( UI_HDRS ${UI_FILES} )

# ADD_EXECUTABLE(${MOC_HEADERS})

# include_directories(/usr/include/x86_64-linux-gnu/qt5/QtWidgets)
include_directories( ${OpenCV_INCLUDE_DIRS})

MACRO(add_example name)
  # Populate a CMake variable with the sources, all the neccessary files
  set(name_SRCS
    mainwindow.ui
    mainwindow.cpp
    camviewer.cpp
    ${name}.cpp
  )
  # ADD_EXECUTABLE(${name} ${name}.cpp)
  ADD_EXECUTABLE(${name} ${name_SRCS})
  # TARGET_LINK_LIBRARIES(${name} ${OpenCV_LIBS})
  # Use the Widgets module from Qt 5
  TARGET_LINK_LIBRARIES(${name} ${OpenCV_LIBS} Qt5::Widgets)
ENDMACRO()


add_example(main)

# target_link_libraries(${PROJECT_NAME}
#   Qt5::Core
#   # Qt5::Quick
#   Qt5::Widgets  
#   Qt5::Gui  
# )