import os
import teapot
from teapot import builder


def main():
    teapot.rootdir = os.path.dirname(os.path.realpath(__file__))
    teapot.sources = os.path.realpath(teapot.rootdir + "/SOURCES")
    teapot.specs = os.path.realpath(teapot.rootdir + "/SPECS")
    teapot.build = os.path.realpath(teapot.rootdir + "/BUILD")
    teapot.buildroot = os.path.realpath(teapot.rootdir + "/BUILDROOT")
    teapot.pkgdir = os.path.realpath(teapot.rootdir + "/PKGS")
    builder.run_builder()

if __name__ == "__main__":
    main()
