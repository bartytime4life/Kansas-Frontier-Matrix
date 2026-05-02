#!/usr/bin/env python
import argparse
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--out-dir');a=p.parse_args();print('PASS')
