pkgname = "himitsu-secret-service"
pkgver = "0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Himitsu secret service integration"
license = "MIT"
url = "https://git.sr.ht/~apreiml/himitsu-secret-service"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "59d6610a7b701b47d53861245dc6a0d1b4e973c818d0e95c1c14ed6582ecfaae"
