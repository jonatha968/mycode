#!/usr/bin/env python3

import os

path = '~/mycode/mycode'

for root, directories, files in os.walk(path, topdown=False):
	for name in files:
		print(os.path.join(root, name))
	for name in directories:
		print(os.path.join(root, name))
