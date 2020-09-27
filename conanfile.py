import os
from conans import ConanFile, CMake, tools


class NdkLibcFixConan(ConanFile):
    name = "ndk-libc-fix"
    version = "0.1"
    description = "Add glob.c and crypt.c from freebsd"
    license = "BSD License"
    exports = "LICENSE.md"
    exports_sources = "CMakeLists.txt"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    @property
    def _build_subfolder(self):
        return "build_subfolder"

    def configure(self):
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd
    
    def export_sources(self):
        self.copy("CMakeLists.txt")
        self.copy("src/*")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
        
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)