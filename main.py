#!/usr/bin/env python3
"""make.fun news-image-20261117 entry.

This program is a deterministic copy. The cover image (entry.png) is final;
the program produces byte-identical output on every run, with no network,
no randomness and no clock dependence, copying entry.png to /output/entry.png.
"""
import os
import shutil


def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        raise SystemExit(
            f"Error: Copied file size mismatch! Source: {src_size} bytes, Destination: {dst_size} bytes"
        )
    print(f"Wrote {dst_size} bytes to {dst}")


if __name__ == "__main__":
    main()
