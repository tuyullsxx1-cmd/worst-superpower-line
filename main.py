import pathlib

# the most useless power wins
LINE = "The power to know exactly when a meeting could have been an email — but only after it ends."


def write_entry():
    out_path = pathlib.Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = LINE.encode("utf-8")
    out_path.write_bytes(payload)


write_entry()
