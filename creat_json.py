import kfc_parser
import ziko_parser
import monomax_parser

import os
import json

kfc = kfc_parser.kfc_parser()
ziko = ziko_parser.ziko_parser()
monomax = monomax_parser.monomax_parser()

if "json_files" not in os.listdir():
    os.mkdir("json_files")

with open("json_files/kfc_file.json", "w", encoding='utf-8') as write_file:
    json.dump(kfc, write_file, ensure_ascii=False)

with open("json_files/ziko_file.json", "w", encoding='utf-8') as write_file:
    json.dump(ziko, write_file, ensure_ascii=False)

with open("json_files/monomax_file.json", "w", encoding='utf-8') as write_file:
    json.dump(monomax, write_file, ensure_ascii=False)
