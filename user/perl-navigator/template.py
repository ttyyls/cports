pkgname = "perl-navigator"
pkgver = "0.8.16"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl Language Server"
license = "MIT"
url = "https://github.com/bscan/PerlNavigator"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cd520cb4aea4eb129715d5d065acf1c0982e55f6199a6e8631ad632251322afe"


def post_install(self):
    self.install_license("LICENSE")
