pkgname = "python-jsonpickle"
pkgver = "3.4.2"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # needs pandas
    "--ignore=jsonpickle/ext/pandas.py",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python"]
checkdepends = [
    "python-atheris",
    "python-numpy",
    # "python-pandas",
    "python-pytest",
]
pkgdesc = "Serializing any arbitrary object graph into JSON"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://github.com/jsonpickle/jsonpickle"
source = f"$(PYPI_SITE)/j/jsonpickle/jsonpickle-{pkgver}.tar.gz"
sha256 = "2efa2778859b6397d5804b0a98d52cd2a7d9a70fcb873bc5a3ca5acca8f499ba"


def post_install(self):
    self.install_license("LICENSE")
