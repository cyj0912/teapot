from teapot import builder
import os
import shutil
import subprocess

name = 'qt-lite'
source0 = 'qt5-opensource-src-5.5.1.zip'
source1 = 'qtbase-opensource-src-5.5.1.zip'
print("Running: " + builder.spec_file_path(name))
os.chdir(builder.build_path(name))
builder.unpack_archive(builder.source_file_path(source0), '.', None)
builder.unpack_archive(builder.source_file_path(source1), '.', None)
os.rename("qtbase-opensource-src-5.5.1", "qtbase")
os.rename("qt-everywhere-opensource-src-5.5.1", "qtsrc")
shutil.move("qtbase", "qtsrc/")
os.chdir("qtsrc")

batch = """
call "C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\vcvarsall.bat" amd64
call configure.bat -confirm-license -opensource -debug-and-release -shared -nomake examples -nomake tests -opengl desktop -prefix {}
nmake
nmake install
"""
batch = batch.format(builder.build_root(name))
f = open("compile.bat", "w")
f.write(batch)
f.close()
subprocess.run('compile.bat'.split())
