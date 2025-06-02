pkgname = "workrave"
pkgver = "1.10.53"
_commit = "10868b0a561aa678d0214acb2f216a6df8f3b97a"
pkgrel = 0
# build_style = "gnu_configure"
# configure_args = [
#     "--disable-static",
#     "--disable-gsettings",
# ]
# configure_env = {"NOCONFIGURE": "1"}
# configure_gen = ["./autogen.sh"]
build_style = "cmake"
hostmakedepends = [
    "automake",
    "bash",
    "cmake",
    "gettext-devel",
    "intltool",
    "ninja",
    "pkgconf",
    "python",
    "slibtool",
]
makedepends = [
    "boost-devel",
    "fmt-devel",
    "gtk4-devel",
    "gtkmm3.0-devel",
    "libxscrnsaver-devel",
    "pipewire-devel",
    "python-jinja2",
    "qt6-qtbase-devel",
    "spdlog-devel",
]
depends = [
    "dconf",
    "python-jinja2",
]
pkgdesc = "RSI prevention and recovery assistant"
license = "GPL-3.0-or-later"  # TODO: double check
url = "https://workrave.org"
# source = f"https://github.com/rcaelers/workrave/archive/refs/tags/v{pkgver.replace('.', '_')}.tar.gz"
source = f"https://github.com/rcaelers/workrave/archive/{_commit}.tar.gz"
sha256 = "e6c61db0aecfeb24ba30778cf71ad52a0c757eefc346e0a2d1abcc349d3b6a57"
hardening = ["vis", "cfi"]
