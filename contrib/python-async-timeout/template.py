pkgname = "python-async-timeout"
pkgver = "4.0.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest-asyncio"]
pkgdesc = "Timeout context manager for asyncio programs"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/aio-libs/async-timeout"
source = f"$(PYPI_SITE)/a/async-timeout/async-timeout-{pkgver}.tar.gz"
sha256 = "4640d96be84d82d02ed59ea2b7105a0f7b33abe8703703cd0ab0bf87c427522f"
