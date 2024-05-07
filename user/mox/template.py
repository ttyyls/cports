pkgname = "mox"
pkgver = "0.0.11"
pkgrel = 0
build_style = "go"
make_dir = "."
hostmakedepends = ["bash", "go", "nodejs"]
checkdepends = ["staticcheck"]
pkgdesc = "Modern, secure, all-in-one email server"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT AND BSD-3-Clause AND MPL-2.0"
url = "https://www.xmox.nl"
source = f"https://github.com/mjl-/mox/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "920cd666a32d08dc16121b9e11e5b00cbc26ef023b2fd6b0df975ea604c43db9"


def init_prepare(self):
    self.do("npm", "ci", "--loglevel", "info", allow_network=True)


def pre_build(self):
    self.do("make", "build0")


def post_check(self):
    self.do("make", "fuzz")


def do_install(self):
    self.install_bin("mox")
    self.install_license("LICENSE.MIT")
    self.install_license("LICENSE.MPLv2.0")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="mox.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="mox.conf",
    )
    self.install_service(self.files_path / "mox")
