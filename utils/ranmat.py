"""
Usage: 
python ranmat.py 5 5 10 testdata.json
python ranmat.py 5 5 10 testdata.json --shapes

5 5 are dimensions
10 is number of matrices
shapes mode creates random matrices with 1 - 2*dim specified
"""


from random import randint
import json
import sys

def random_matrix(dim_x, dim_y, low=-100., high=100.):
    return [[randint(low, high) for j in range(dim_y)] for i in range(dim_x)]

def mat_to_str(mat):
    return "\n".join([" ".join(map(str, row)) for row in mat]) + "\n\n"

if __name__ == "__main__":
    if len(sys.argv) > 5 and sys.argv[5] == "--shapes":
        td = [mat_to_str(random_matrix(int(randint(1, int(sys.argv[1]) * 2)), randint(1, int(sys.argv[2]) * 2))) for i in range(int(sys.argv[3]))]
    else:
        td = [mat_to_str(random_matrix(int(sys.argv[1]), int(sys.argv[2]))) for i in range(int(sys.argv[3]))]
    with open(sys.argv[4], "w") as f:
        f.write(json.dumps(td))