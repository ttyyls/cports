pkgname = "python-vobject"
pkgver = "0.9.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-dateutil", "python-pytz"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python module for parsing and creating iCalendar and vCard files"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/py-vobject/vobject"
source = f"$(PYPI_SITE)/v/vobject/vobject-{pkgver}.tar.gz"
sha256 = "ac44e5d7e2079d84c1d52c50a615b9bec4b1ba958608c4c7fe40cbf33247b38e"
