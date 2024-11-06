pkgname = "python-atheris"
pkgver = "2.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "bash",
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
makedepends = ["python-pybind11"]
pkgdesc = "Coverage-guided fuzzer for Python and Python extensions"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/google/atheris"
source = f"$(PYPI_SITE)/a/atheris/atheris-{pkgver}.tar.gz"
sha256 = "cf1fdf5fa220a41a2f262b32363fc566549502b2cb0addf4e1baad5531c0e825"
