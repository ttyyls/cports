pkgname = "pounce"
pkgver = "3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-notify", "--enable-palaver"]
configure_gen = []
make_dir = "."
make_build_target = "all"
hostmakedepends = ["pkgconf"]
makedepends = ["libretls-devel", "libcurl-devel", "sqlite-devel"]
pkgdesc = "Multi-client, TLS-only IRC bouncer"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://git.causal.agency/pounce"
source = f"{url}/snapshot/pounce-{pkgver}.tar.gz"
sha256 = "97f245556b1cc940553fca18f4d7d82692e6c11a30f612415e5e391e5d96604e"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "calico")
    self.install_service(self.files_path / "pounce")
    self.install_license("LICENSE")
