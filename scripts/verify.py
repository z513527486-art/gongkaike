#!/usr/bin/env python3
"""Basic verification for generated lesson HTML files."""

import os
import re
import sys
from pathlib import Path


def verify_html(path: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f'File not found: {path}')

    text = p.read_text(encoding='utf-8')
    required = [
        '<html',
        '<title>',
        '学习目标',
        '场景总览',
        '课题练习',
    ]

    missing = [x for x in required if x not in text]
    if missing:
        raise ValueError(f'Missing required content markers: {missing}')

    print(f'PASS: {path}')


def main():
    if len(sys.argv) < 2:
        print('Usage: verify.py <html_file>')
        raise SystemExit(1)
    verify_html(sys.argv[1])


if __name__ == '__main__':
    main()
