pkgname = "minetest"
pkgver = "5.8.0"
_irrlichtver = "1.9.0mt13"
pkgrel = 0
build_wrksrc = f"{pkgname}-{pkgver}"
build_style = "cmake"
configure_args = [
    "-DBUILD_SERVER=TRUE",
    "-DENABLE_PROMETHEUS=ON",
    "-DENABLE_UPDATE_CHECKER=FALSE",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext-devel"]
makedepends = [
    "bzip2-devel",
    "freetype-devel",
    "gettext-devel",
    "gmp-devel",
    "hiredis-devel",
    "libcurl-devel",
    "libjpeg-turbo-devel",
    "libogg-devel",
    "libpng-devel",
    "libvorbis-devel",
    "libxi-devel",
    "luajit-devel",
    "mesa-devel",
    "openal-soft-devel",
    "openssl-devel",
    "sqlite-devel",
    "zstd-devel",
]
pkgdesc = "Voxel game creation platform"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-2.1-or-later"
url = "https://www.minetest.net"
source = [
    f"https://github.com/minetest/minetest/archive/refs/tags/{pkgver}.tar.gz",
    f"https://github.com/minetest/irrlicht/archive/refs/tags/{_irrlichtver}.tar.gz",
]
sha256 = [
    "610c85a24d77acdc3043a69d777bed9e6c00169406ca09df22ad490fe0d68c0c",
    "2fde8e27144988210b9c0ff1e202905834d9d25aaa63ce452763fd7171096adc",
]
tool_flags = {"CXXFLAGS": ["-Wno-deprecated-declarations"]}
hardening = ["!int"]


def post_extract(self):
    self.mv(
        self.builddir / f"{pkgname}-{pkgver}" / f"irrlicht-{_irrlichtver}",
        f"{pkgname}-{pkgver}/lib/irrlichtmt",
    )


def post_install(self):
    self.install_service(self.files_path / "minetest")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="minetest.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="minetest.conf",
    )
    self.install_file(
        "minetest.conf.example",
        "etc/minetest",
        name="minetest.conf",
    )


@subpackage("minetest-common")
def _common(self):
    self.pkgdesc = f"{pkgdesc} (common files)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["usr/share/minetest"]


@subpackage("minetest-server")
def _server(self):
    self.pkgdesc = f"{pkgdesc} (server)"
    self.depends = ["minetest-common"]

    return [
        "usr/bin/minetestserver",
        "etc/minetest/minetest.conf",
        "etc/dinit.d/minetest",
    ]
