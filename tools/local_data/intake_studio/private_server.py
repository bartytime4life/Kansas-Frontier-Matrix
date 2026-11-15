#!/usr/bin/python3
"""Explicit private Studio entrypoint; the historical intake_server entry is secured too."""
from pathlib import Path
import sys

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from tools.local_data.intake_studio.intake_server import main

if __name__ == '__main__':
    main()
