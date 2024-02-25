pkgname = "radvd"
pkgver = "2.19"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-check"]
hostmakedepends = ["flex", "bison", "pkgconf"]
makedepends = ["check-devel", "libdaemon-devel", "linux-headers"]
pkgdesc = "IPv6 router advertisement daemon"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-Advertising-Acknowledgement"
url = "https://radvd.litech.org"
source = f"https://radvd.litech.org/dist/radvd-{pkgver}.tar.gz"
sha256 = "c36470706fec3a9e6bed394ffea08acaff5dac647848d26b96bb9b9c65d58da0"
hardening = ["vis", "cfi"]
# FIXME: some tests fail
options = ["!check"]


# def init_check(self):
#     self.make_check_env = {
#         "CFLAGS": f"{self.get_cflags(shell=True)} -funsigned-char",
#         "LDLFGAS": f"{self.get_ldflags(shell=True)} -lcheck",
#     }


def post_install(self):
    self.install_license("COPYRIGHT")
    self.install_file("radvd.conf.example", "etc", name="radvd.conf")
    self.install_service(self.files_path / "radvd")


configure_gen = []
