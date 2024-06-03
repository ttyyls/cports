pkgname = "qutebrowser"
pkgver = "3.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "asciidoc",
    "gmake",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-adblock",
    "python-jinja2",
    "python-pygments",
    "python-pyqt6",
    "python-pyqt6-webengine",
    "python-pyqt6_sip",
    "python-pyyaml",
    "python-tldextract",
    "qt6-qtbase",
    "qt6-qtbase-dbus",
    "qt6-qtbase-sql",
    "qt6-qtwebengine",
]
checkdepends = depends + [
    "python-beautifulsoup4",
    "python-cheroot",
    "python-flask",
    "python-hypothesis",
    "python-jaraco.classes",
    "python-jaraco.functools",
    "python-more-itertools",
    "python-pytest",
    "python-pytest-bdd",
    "python-pytest-benchmark",
    "python-pytest-instafail",
    "python-pytest-mock",
    "python-pytest-qt",
    "python-pytest-rerunfailures",
    "python-soupsieve",
    "python-vulture",
    "xwayland-run",
]
pkgdesc = "Keyboard driven web browser with a minimalist gui"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-only"
url = "https://qutebrowser.org"
source = f"https://github.com/qutebrowser/qutebrowser/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6558bc55bdd7d7a5cefbb9166eea14cd7eaa53ba3e97f6814eb3ebaa548f68e2"


def do_check(self):
    self.do(
        "xwfb-run",
        "--",
        "python",
        "-m",
        "pytest",
        "-q",
    )


def post_install(self):
    self.do(
        "gmake",
        "-f",
        "misc/Makefile",
        f"DESTDIR={self.chroot_destdir}",
        "PREFIX=/usr",
        "install",
    )
