pkgname = "pimsync"
pkgver = "0.4.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Synchronize calendars and address books"
license = "EUPL-1.2"
url = "https://pimsync.whynothugo.nl"
source = f"https://git.sr.ht/~whynothugo/pimsync/archive/v{pkgver}.tar.gz"
sha256 = "f38769ee1c3842aec6a3c93d90f626fb67036aca62fbbc807bc26e9150b6d3f6"
env = {"PIMSYNC_VERSION": pkgver}


def post_install(self):
    self.install_service("^/pimsync.user")
    self.install_man("pimsync.1")
    self.install_man("pimsync.conf.5")
    self.install_man("pimsync-migration.7")
