pkgname = "containers-common"
pkgver = "0.60.2"
pkgrel = 0
make_cmd = "gmake"
make_build_args = ["-C", "docs"]
make_install_args = [*make_build_args]
hostmakedepends = ["gmake", "go-md2man"]
pkgdesc = "Shared docs and configs for Containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/containers/common"
_base_url = url.removesuffix("/common")
_common_ver = pkgver
_storage_ver = "1.55.0"
_image_ver = "5.32.2"
_shortnames_ver = "2023.02.20"
source = [
    f"{_base_url}/common/archive/v{_common_ver}.tar.gz",
    f"{_base_url}/storage/archive/v{_storage_ver}.tar.gz",
    f"{_base_url}/image/archive/v{_image_ver}.tar.gz",
    f"{_base_url}/shortnames/archive/v{_shortnames_ver}.tar.gz",
]
source_paths = [
    "common",
    "storage",
    "image",
    "shortnames",
]
sha256 = [
    "45a83663c634797461810fc8743a4b941592d506099cc8679838ffdfac9d5e71",
    "d6c2d3af9e0f674c248477d521d0f8fc5eac050c65e2fd3f823cc42502b22847",
    "2e0a4f21416cd287a39fe3556197f258ca02ffc5825a74b4ad6c3f52f08446b5",
    "336ba679d4e510d2eb59cb11321bf16a36ef2dba58024e79dd76b89ffee539e6",
]
# no tests
options = ["!check"]


def do_build(self):
    self.do("gmake", wrksrc="common/docs")
    self.do("gmake", wrksrc="storage/docs")
    self.do("gmake", "docs", wrksrc="image")


def do_install(self):
    self.install_dir("etc/containers/certs.d")
    self.install_dir("etc/containers/oci/hooks.d")
    self.install_dir("var/lib/containers/sigstore", empty=True)

    with self.pushd("common"):
        self.install_file("pkg/config/containers.conf", "etc/containers")
        self.install_file("pkg/config/containers.conf", "usr/share/containers")
        self.install_file("pkg/seccomp/seccomp.json", "etc/containers")
        self.install_file("pkg/seccomp/seccomp.json", "usr/share/containers")
        self.do(
            "gmake",
            "install",
            "PREFIX=/usr",
            f"DESTDIR={self.chroot_destdir}",
            wrksrc="docs",
        )

    with self.pushd("storage"):
        self.install_file("storage.conf", "etc/containers")
        self.install_file("storage.conf", "usr/share/containers")
        self.do(
            "gmake", "install", f"DESTDIR={self.chroot_destdir}", wrksrc="docs"
        )

    with self.pushd("image"):
        self.install_file("registries.conf", "etc/containers")
        self.do("gmake", "install", f"DESTDIR={self.chroot_destdir}")

    with self.pushd("shortnames"):
        self.install_file(
            "shortnames.conf",
            "etc/containers/registries.conf.d",
            name="00-shortnames.conf",
        )
