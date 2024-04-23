url = "https://api.github.com/repos/minio/minio/git/refs/tags"
pattern = r"refs/tags/RELEASE\.([0-9-]{10})T[0-9\-]+Z"


def fetch_versions(self, src):
    return map(lambda v: v.replace(".", "-"), self.fetch_versions(src))
