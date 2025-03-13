pkgname = "python-readability-lxml"
pkgver = "0.8.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Html to text parser"
license = "Apache-2.0"
url = "https://github.com/buriy/python-readability"
source = f"$(PYPI_SITE)/r/readability-lxml/readability-lxml-{pkgver}.tar.gz"
sha256 = "e51fea56b5909aaf886d307d48e79e096293255afa567b7d08bca94d25b1a4e1"
