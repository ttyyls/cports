pkgname = "umurmur"
pkgver = "0.3.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "libconfig-devel",
    "openssl3-devel",
    "protobuf-c-devel",
]
pkgdesc = "Mumble server"
license = "BSD-3-Clause"
url = "https://github.com/umurmur/umurmur"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8327dd0b2c5bd187a38d098295e896a6b85d698c9268205bcb27f6244f760a73"


def install(self):
    self.install_bin("build/bin/umurmurd")
    self.install_service(self.files_path / "umurmurd")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file("umurmur.conf.example", "usr/share/umurmur")
    self.install_license("LICENSE")
