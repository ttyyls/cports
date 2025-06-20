pkgname = "todoman"
pkgver = "4.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-sphinx",
]
depends = [
    "python-click",
    "python-click-log",
    "python-click-repl",
    "python-dateutil",
    "python-humanize",
    "python-icalendar",
    "python-parsedatetime",
    "python-prompt-toolkit",
    "python-urwid",
    "python-xdg",
]
checkdepends = [
    "python-hypothesis",
    "python-mypy",
    "python-pytest",
    "python-pytz",
    "python-freezegun",
    *depends,
]
pkgdesc = "CLI task manager"
license = "ISC"
url = "https://github.com/pimutils/todoman"
source = f"$(PYPI_SITE)/t/todoman/todoman-{pkgver}.tar.gz"
sha256 = "2e81dba7b34a2cba6fe74f381c579500ab525ebf3f82847e56127c69d382f121"
# XXX: skip faulty check
options = ["!check"]


# def post_build(self):
#     self.do(
#         "make",
#         "-C",
#         "docs",
#         "man",
#         env={"PYTHONPATH": self.chroot_cwd},
#     )


def post_install(self):
    self.install_license("LICENCE")
