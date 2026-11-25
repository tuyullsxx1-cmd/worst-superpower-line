import os

# the most useless power wins
LINE = "The power to know exactly when a meeting could have been an email \u2014 but only after it ends."


def main():
    os.makedirs("/output", exist_ok=True)
    fd = os.open("/output/entry.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, LINE.encode("utf-8"))
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
