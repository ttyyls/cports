pkgname = "python-xdg"
pkgver = "6.0.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
checkdepends = ["python-pytest"]
pkgdesc = "Variables defined by the XDG Base Directory Specification"
license = "ISC"
url = "https://github.com/srstevenson/xdg-base-dirs"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2acedeb4e5723f90194325d4a6b39263f05a81b143fa1299ac31b167933fe829"


def post_install(self):
    self.install_license("LICENSE")
