pkgname = "python-beautifulsoup4"
pkgver = "4.12.3"
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
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://www.crummy.com/software/BeautifulSoup"
source = f"$(PYPI_SITE)/b/beautifulsoup4/beautifulsoup4-{pkgver}.tar.gz"
sha256 = "74e3d1928edc070d21748185c46e3fb33490f22f52a3addee9aee0f4f7781051"


def post_install(self):
    self.install_license("LICENSE")
