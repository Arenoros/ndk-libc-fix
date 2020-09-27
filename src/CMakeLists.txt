cmake_minimum_required(VERSION 2.8.9)
project(ndk-fix C)

set(SOURCES crypt.c glob.c issetguid.c)
set(HDR_PUBLIC crypt.h glob.h)
set(LIB ndk-fix)
add_library(ndk-fix STATIC ${SOURCES})# ${HDR_PUBLIC})
install(TARGETS ${LIB}
        LIBRARY DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" COMPONENT libraries
        ARCHIVE DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" COMPONENT libraries
        RUNTIME DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" COMPONENT libraries # Windows DLLs
        PUBLIC_HEADER DESTINATION "${CMAKE_INSTALL_PREFIX}/include" COMPONENT dev)