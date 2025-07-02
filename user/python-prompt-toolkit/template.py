pkgname = "python-prompt-toolkit"
pkgver = "3.0.51"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
depends = ["python-wcwidth"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Interactive command lines library in Python"
license = "BSD-3-Clause"
url = "https://python-prompt-toolkit.readthedocs.io"
source = f"$(PYPI_SITE)/p/prompt_toolkit/prompt_toolkit-{pkgver}.tar.gz"
sha256 = "931a162e3b27fc90c86f1b48bb1fb2c528c2761475e57c9c06de13311c7b54ed"


def post_install(self):
    self.install_license("LICENSE")
