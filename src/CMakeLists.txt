cmake_minimum_required(VERSION 2.8.9)
project(ndk-libc-fix C)

#set(SOURCES crypt.c glob.c issetguid.c crypt-md5.c crypt-nthash.c crypt-sha256.c crypt-sha512.c)
file(GLOB SOURCES *.c)
message(${SOURCES})
set(HDR_PUBLIC crypt.h glob.h)
set(LIB ndk-libc-fix)
add_library(${LIB} STATIC ${SOURCES} ${HDR_PUBLIC})
install(TARGETS ${LIB}
        LIBRARY DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" COMPONENT libraries
        ARCHIVE DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" COMPONENT libraries
        RUNTIME DESTINATION "${CMAKE_INSTALL_PREFIX}/bin" COMPONENT libraries # Windows DLLs
        PUBLIC_HEADER DESTINATION "${CMAKE_INSTALL_PREFIX}/include" COMPONENT dev)