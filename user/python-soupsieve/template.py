pkgname = "python-soupsieve"
pkgver = "2.5"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
checkdepends = ["python-beautifulsoup4", "python-pytest"]
pkgdesc = "CSS selector implementation for python-beautifulsoup"
license = "MIT"
url = "https://github.com/facelessuser/soupsieve"
source = f"$(PYPI_SITE)/s/soupsieve/soupsieve-{pkgver}.tar.gz"
sha256 = "5663d5a7b3bfaeee0bc4372e7fc48f9cff4940b3eec54a6451cc5299f1097690"
# cyclic dep bs4 -> soupsieve -> bs4
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
