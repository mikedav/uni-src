import random
import json

def random_matrix(dim_x, dim_y, low=-100., high=100.):
    return [[random.randint(low, high) for j in range(dim_y)] for i in range(dim_x)]

def mat_to_str(mat):
    return "\n".join([" ".join(map(str, row)) for row in mat])

if __name__ == "__main__":
    td = [mat_to_str(random_matrix(5, 5)) for i in range(10)]
    with open("testdata.json", "w") as f:
        f.write(json.dumps(td))