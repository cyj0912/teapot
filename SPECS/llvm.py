from teapot import builder
import os
import subprocess

name = 'llvm'
version = '3.7.0'
source0 = 'llvm-%s.src.tar.xz' % version
source0folder = 'llvm-%s.src' % version
# source1 = 'cfe-%s.src.tar.xz' % version
# source1folder = 'cfe-%s.src' % version
print("Running: " + builder.spec_file_path(name))
os.chdir(builder.build_path(name))
builder.unpack_archive(builder.source_file_path(source0), '.', None)
# builder.unpack_archive(builder.source_file_path(source1), source0folder + '/tools', None)
# os.rename(source0folder + '/tools/' + source1folder, source0folder + '/tools/clang')
os.chdir(source0folder)

cmake_generator = 'Visual Studio 14 2015 Win64'
cmake_variant = 'Release'
batch = """
cmake -G "{0}" -DCMAKE_INSTALL_PREFIX={1} -DCMAKE_CONFIGURATION_TYPES={2} -DLLVM_TARGETS_TO_BUILD="X86"
cmake --build . --target install --config {2}
"""
batch = batch.format(cmake_generator, builder.build_root(name), cmake_variant)
f = open("compile.bat", "w")
f.write(batch)
f.close()
subprocess.run('compile.bat'.split())
