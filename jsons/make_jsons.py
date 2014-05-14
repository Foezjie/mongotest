#!/usr/bin/env python3

import subprocess
import os
import itertools


#file = "/tmp/init.py"
file = "libs/std/plugins/__init__.py"
dep_dir = "dep_managers/"
managers= [file for file in os.listdir(dep_dir) if "." not in file]

orders = []
for length in range(1, len(managers)+1):
    for group in list(itertools.combinations(managers,length)):
        for perm in itertools.permutations(group):
            orders.append(perm)

for order in orders:
    suffix = "_".join(order)
    print("--------------------")
    print("Order: %s" % suffix)
    print("--------------------")
    subprocess.call("cat %s > %s" % (dep_dir+"imports.pre", file), shell=True)
    for dep_manager in order:
        #print("adding %s" % dep_manager)
        subprocess.call("cat %s >> %s" % (dep_dir+dep_manager, file), shell=True)

    subprocess.call("cat %s >> %s" % (dep_dir+"dirs_files.suffix", file), shell=True)

    subprocess.call("imp export -j %s" % "jsons/"+suffix+".json", shell=True)
    #input("Press Enter to continue...")
