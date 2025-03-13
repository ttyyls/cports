pkgname = "python-readability"
pkgver = "0.3.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Measure the readability of a given text using surface characteristics"
license = "Apache-2.0"
url = "https://github.com/andreasvc/readability"
source = f"$(PYPI_SITE)/r/readability/readability-{pkgver}.tar.gz"
sha256 = "5aace888855cb3ef1b7dd059e41bbc6ac1f7daba321b2d24062ca75fdf6e576d"
# maybe later
options = ["!check"]
