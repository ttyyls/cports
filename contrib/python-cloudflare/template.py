pkgname = "python-cloudflare"
pkgver = "2.20.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest", "python-requests", "python-pytz"]
pkgdesc = "Python wrapper for the Cloudflare v4 API"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/cloudflare/python-cloudflare"
source = f"$(PYPI_SITE)/c/cloudflare/cloudflare-{pkgver}.tar.gz"
sha256 = "46aefc39dfaa2365d639b423cec2cd5350ae11153c7247d3eb3545bdcf01a68a"
# tests hang half way through
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
