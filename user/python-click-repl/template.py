pkgname = "python-click-repl"
pkgver = "0.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Subcommand REPL for click apps"
license = "MIT"
url = "https://github.com/click-contrib/click-repl"
source = f"$(PYPI_SITE)/c/click-repl/click-repl-{pkgver}.tar.gz"
sha256 = "17849c23dba3d667247dc4defe1757fff98694e90fe37474f3feebb69ced26a9"


def post_install(self):
    self.install_license("LICENSE")
