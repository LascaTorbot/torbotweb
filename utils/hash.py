import hashlib

def file_hash(fin):
    h = hashlib.sha256()
    for b in iter(lambda : fin.read(128*1024), b''):
        h.update(b)

    return h.hexdigest()

