pkgname = "khard"
pkgver = "0.19.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-sphinx",
    "python-wheel",
]
depends = [
    "python-configobj",
    "python-ruamel.yaml",
    "python-unidecode",
    "python-vobject",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Console vcard client"
license = "GPL-3.0-or-later"
url = "https://github.com/lucc/khard"
source = f"$(PYPI_SITE)/k/khard/khard-{pkgver}.tar.gz"
sha256 = "59f30a0da3c3da3eb04f4dbe18ee4763913b685d99ec8418fd574a88c491c490"
