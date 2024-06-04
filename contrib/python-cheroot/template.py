pkgname = "python-cheroot"
pkgver = "10.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python http server"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://cheroot.cherrypy.dev"
source = f"$(PYPI_SITE)/c/cheroot/cheroot-{pkgver}.tar.gz"
sha256 = "e0b82f797658d26b8613ec8eb563c3b08e6bd6a7921e9d5089bd1175ad1b1740"
# unpackaged deps
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
