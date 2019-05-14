from hashlib import md5, sha1

def streamhasher(algorithm, chunk_size=4096):
    def hash(stream):
        hasher = algorithm()
        for chunk in iter(lambda: stream.read(chunk_size), ''):
            print("chunk", chunk)
            hasher.update(chunk.encode('utf-8'))
        return hasher.hexdigest()

    return hash

md5_hasher = streamhasher(md5)
sha1_hasher = streamhasher(sha1)

# assumes workingdir is top-level dir
fname = './strategy/stream.py' 
print("MD5", md5_hasher(open(fname)))
print("SHA1", sha1_hasher(open(fname)))




