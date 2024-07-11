pkgname = "python-jeepney"
pkgver = "0.8.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = [
    "python-async-timeout",
    "python-pytest",
    "python-testpath",
    "python-trio",
]
pkgdesc = "Python dbus portocol wrapper"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://gitlab.com/takluyver/jeepney"
source = f"$(PYPI_SITE)/j/jeepney/jeepney-{pkgver}.tar.gz"
sha256 = "5efe48d255973902f6badc3ce55e2aa6c5c3b3bc642059ef3a91247bcfcc5806"
