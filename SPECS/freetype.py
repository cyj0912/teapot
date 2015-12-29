from teapot import builder
import os
import subprocess

name = 'freetype'
version = '2.6.2'
source0 = 'ft262.zip'

print("Running: " + builder.spec_file_path(name))

os.chdir(builder.build_path(name))
builder.unpack_archive(builder.source_file_path(source0), '.', None)
os.mkdir('build')
os.chdir('build')

cmake_generator = 'Visual Studio 14 2015 Win64'
cmake_variant = 'Debug'
configcmd = 'cmake -G PLACEHOLDER {} -DCMAKE_INSTALL_PREFIX={} -DCMAKE_CONFIGURATION_TYPES={}'\
    .format('../freetype-' + version, os.path.join(builder.build_root(name), cmake_variant), cmake_variant)
cmake_command = configcmd.split()
cmake_command[2] = cmake_generator
subprocess.run(cmake_command)
subprocess.run('cmake --build . --target install --config {}'.format(cmake_variant).split())

os.chdir(builder.build_path(name))
os.mkdir('build2')
os.chdir('build2')

cmake_generator = 'Visual Studio 14 2015 Win64'
cmake_variant = 'Release'
configcmd = 'cmake -G PLACEHOLDER {} -DCMAKE_INSTALL_PREFIX={} -DCMAKE_CONFIGURATION_TYPES={}'\
    .format('../freetype-' + version, os.path.join(builder.build_root(name), cmake_variant), cmake_variant)
cmake_command = configcmd.split()
cmake_command[2] = cmake_generator
subprocess.run(cmake_command)
subprocess.run('cmake --build . --target install --config {}'.format(cmake_variant).split())
