import os
import json
import sys

scriptname = sys.argv[1]

with open(sys.argv[2], "r") as f:
    testdata = json.loads(f.read())

def execlog(command):
    print(f"executing {{command}}", flush=True)
    os.system(command)

for td, num in zip(testdata, range(len(testdata))):
    print(f"Test set {num + 1}")
    print(f"tmp contents:\n{td}", flush=True)
    with open("tmp", "w") as f:
        f.write(td)
    execlog(f"type tmp | python {scriptname}")
    print("\n\n\n", flush=True)

execlog("del tmp")
    