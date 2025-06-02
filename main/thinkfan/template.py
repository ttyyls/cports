pkgname = "thinkfan"
pkgver = "2.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DUSE_ATASMART=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libatasmart-devel",
    "lm-sensors-devel",
    "yaml-cpp-devel",
]
pkgdesc = "Simple fan control program"
license = "GPL-3.0-or-later"
url = "https://github.com/vmatare/thinkfan"
source = f"https://github.com/vmatare/thinkfan/archive/{pkgver}.tar.gz"
sha256 = "0fc94eb378dcba8c889e91f41dab3a8d6eebc7324a59a0704cc39aa66551987e"
hardening = ["vis"]


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "thinkfan")
