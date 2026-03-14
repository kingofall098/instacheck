import mimetypes

def what(filename, h=None):
    mime, _ = mimetypes.guess_type(filename)
    if mime and mime.startswith("image/"):
        return mime.split("/")[1]
    return None
