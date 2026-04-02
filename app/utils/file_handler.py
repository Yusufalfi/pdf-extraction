import pathlib

def list_files(folder):
    exts = ["*.pdf", "*.jpg", "*.jpeg", "*.png"]
    files = []

    for ext in exts:
        files.extend(pathlib.Path(folder).glob(ext))

    return files