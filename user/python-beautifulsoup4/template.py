pkgname = "python-beautifulsoup4"
pkgver = "4.13.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = ["python-soupsieve"]
checkdepends = ["python-pytest"]
pkgdesc = "Screen-scraping library"
license = "MIT"
url = "https://www.crummy.com/software/BeautifulSoup"
source = f"$(PYPI_SITE)/b/beautifulsoup4/beautifulsoup4-{pkgver}.tar.gz"
sha256 = "1bd32405dacc920b42b83ba01644747ed77456a65760e285fbc47633ceddaf8b"


def post_install(self):
    self.install_license("LICENSE")
