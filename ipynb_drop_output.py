#!/usr/bin/env python

"""
Script is based on the following gist:
https://gist.github.com/pbugnion/ea2797393033b54674af
"""

import sys
import json

with open(sys.argv[1]) as nb:
    json_in = json.loads(nb.read())

ipy_version = int(json_in["nbformat"]) - 1

def strip_output_from_cell(cell):
    if "outputs" in cell:
        cell["outputs"] = []
    if "prompt_number" in cell:
        del cell["prompt_number"]
    if "metadata" in cell:
        cell["metadata"] = {}

if ipy_version == 2:
    for sheet in json_in["worksheets"]:
        for cell in sheet["cells"]:
            strip_output_from_cell(cell)
else:
    for cell in json_in["cells"]:
        strip_output_from_cell(cell)

with open(sys.argv[1], 'w') as of:
    json.dump(json_in, of, sort_keys=True, indent=1, separators=(",",": "), ensure_ascii=False)