from hashlib import md5, sha1


def streamhasher(algorithm, chunk_size=4096):
    def hash(stream):
        hasher = algorithm()
        for chunk in iter(lambda: stream.read(chunk_size), ''):
            hasher.update(chunk.encode('utf-8'))
        return hasher.hexdigest()

    return hash


md5_hasher = streamhasher(md5)
sha1_hasher = streamhasher(sha1)

print(f"Different Hashes of {__file__}:")
print("MD5", md5_hasher(open(__file__)))
print("SHA1", sha1_hasher(open(__file__)))
