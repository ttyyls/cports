pkgname = "python-pytest-qt"
pkgver = "4.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
makedepends = ["python-pyqt6"]
checkdepends = makedepends + [
    "python-pytest",
    "xserver-xorg-xvfb",
]
pkgdesc = "Pytest plugin for PyQt and PySide applications"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/pytest-dev/pytest-qt"
source = f"$(PYPI_SITE)/p/pytest-qt/pytest-qt-{pkgver}.tar.gz"
sha256 = "76896142a940a4285339008d6928a36d4be74afec7e634577e842c9cc5c56844"


def do_check(self):
    self.do(
        "xvfb-run",
        "--",
        "python",
        "-m",
        "pytest",
        "-k not test_basics",
        env={"PYTHONPATH": "src"},
    )


def post_install(self):
    self.install_license("LICENSE")
