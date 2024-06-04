pkgname = "python-pypresence"
pkgver = "4.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
pkgdesc = "Discord RPC client written in Python"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/qwertyquerty/pypresence"
source = f"$(PYPI_SITE)/p/pypresence/pypresence-{pkgver}.tar.gz"
sha256 = "a6191a3af33a9667f2a4ef0185577c86b962ee70aa82643c472768a6fed1fbf3"
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
