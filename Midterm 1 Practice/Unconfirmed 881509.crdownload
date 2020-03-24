#!/usr/bin/env python3

import os
from hashlib import sha256

def read_files(dname):
    titles = []
    documents = []
    for f in os.listdir(dname):
        bookname = f.split(".")[0]
        with open(os.path.join(dname,f),'r', encoding = 'utf-8') as fn:
            text = fn.readlines()
            text = ''.join(text)
        titles.append(bookname)
        documents.append(text)
    return titles, documents

def gen_file_path(basename):
    from os.path import isdir
    return f'./resource/asnlib/publicdata/{basename}'

def open_file(basename, *args):
    return open(gen_file_path(basename), *args)

def make_hash(doc):
    return sha256(doc.encode()).hexdigest()

def check_hash(doc, key):
    return make_hash(doc) == key

def where_strings_differ(a, b):
    first_difference = None
    for k, (a_k, b_k) in enumerate(zip(a, b)):
        if a_k != b_k:
            first_difference = k
            break
    if first_difference is None: # strings match up to min(len(a), len(b)), so check for extra chars
        if len(a) < len(b):
            print(f'Strings are the same except the second one has these extra letters: "{b[len(a):]}"\n')
            first_difference = len(a)
        elif len(b) < len(a):
            print(f'Strings are the same except the first one has these extra letters: "{a[len(b):]}"\n')
            first_difference = len(b)
    if first_difference is None:
        print("==> Strings appear to be identical.")
    else:
        print(f"==> Strings differ starting at position {first_difference}:")
        start_snip = max(0, first_difference-5)
        snip_prefix = "..." if start_snip > 0 else ''
        snip_a = snip_prefix + a[start_snip:first_difference+1]
        snip_b = snip_prefix + b[start_snip:first_difference+1]
        print(f"    {snip_a} <-- position {first_difference}")
        print(f"vs.")
        print(f"    {snip_b} <--")
    return first_difference

# eof
