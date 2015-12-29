import os
import shutil
import zipfile
import tarfile
import teapot


def delete_if_exist(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path)


def mkdir_if_not_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)


def build_path(pkgname):
    return os.path.normpath(teapot.build + "/" + pkgname)


def build_root(pkgname):
    return os.path.normpath(teapot.buildroot + "/" + pkgname)


def spec_file_path(pkgname):
    return os.path.realpath(teapot.specs + "/" + pkgname + ".py")


def source_file_path(filename):
    return os.path.realpath(teapot.sources + "/" + filename)


def pkg_file_path(pkgname):
    return os.path.normpath(teapot.pkgdir + "/" + pkgname + ".zip")


def unpack_archive(archive, target, subdir):
    if subdir and not subdir.endswith("/"):
        subdir += '/'

    if tarfile.is_tarfile(archive):
        tar_file = tarfile.open(archive, 'r')
        members = None
        if subdir:
            members = [
                member for member in tar_file.getmembers()
                if os.path.normpath(member.name)
                    .startswith(subdir) and not os.path.normpath(member.name)
                    .endswith("/.git")
                ]
        tar_file.extractall(target, members)
        tar_file.close()

    elif zipfile.is_zipfile(archive):
        print("Unpacking zip")
        zipFile = zipfile.ZipFile(archive, 'r')
        names = None
        if subdir:
            names = [
                name for name in zipFile.namelist()
                if os.path.normpath(name).startswith(subdir)
                ]
        zipFile.extractall(target, names)
        zipFile.close()


def create_archive(archive, source):
    f = zipfile.ZipFile(archive, 'w')
    parent = os.path.dirname(source)
    for dir_name, subdirs, files in os.walk(source):
        for file in files:
            f.write(os.path.join(dir_name, file), os.path.relpath(os.path.join(dir_name, file), parent), zipfile.ZIP_DEFLATED)
    f.close()


def run_builder():
    print("Build starts from " + teapot.rootdir)
    queue = ["test"]
    for pkgname in queue:
        print(pkgname)
        delete_if_exist(build_path(pkgname))
        delete_if_exist(build_root(pkgname))
        delete_if_exist(pkg_file_path(pkgname))
        mkdir_if_not_exist(build_path(pkgname))
        mkdir_if_not_exist(build_root(pkgname))
        exec(open(spec_file_path(pkgname)).read())
        create_archive(pkg_file_path(pkgname), build_root(pkgname))
