pkgname = "reaction"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Scans logs for repeated patterns and takes action"
license = "AGPL-3.0-or-later"
url = "https://reaction.ppom.me"
source = f"https://framagit.org/ppom/reaction/-/archive/v{pkgver}/reaction-v{pkgver}.tar.gz"
sha256 = "b5571cff639e631eb11eb31c73fde15547af774cf2e69311e1c9501edd136e0e"

if self.profile().wordsize == 32:
    broken = "needs atomicu64"


def install(self):
    with self.pushd(f"target/{self.profile().triplet}/release"):
        self.install_bin("reaction")
        self.install_man("reaction*.1", glob=True)
    self.install_license("LICENSE")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "reaction")
    self.install_file("./config/example.jsonnet", "usr/share/reaction")
    self.install_file("./config/example.yml", "usr/share/reaction")
