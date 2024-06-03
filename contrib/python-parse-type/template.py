pkgname = "python-parse-type"
pkgver = "0.6.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-parse", "python-six"]
checkdepends = ["python-pytest"]
pkgdesc = "Simplifies to build parse types based on the parse module"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jenisys/parse_type"
source = f"$(PYPI_SITE)/p/parse-type/parse_type-{pkgver}.tar.gz"
sha256 = "79b1f2497060d0928bc46016793f1fca1057c4aacdf15ef876aa48d75a73a355"
# tox dependency
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
