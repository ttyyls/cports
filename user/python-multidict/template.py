pkgname = "python-multidict"
pkgver = "6.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Multidict implementation for Python"
license = "Apache-2.0"
url = "https://github.com/aio-libs/multidict"
source = f"$(PYPI_SITE)/m/multidict/multidict-{pkgver}.tar.gz"
sha256 = "942bd8002492ba819426a8d7aefde3189c1b87099cdf18aaaefefcf7f3f7b6d2"
# depends on pytest cov
options = ["!check"]
