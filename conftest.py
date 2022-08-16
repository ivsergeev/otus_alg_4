# -*- coding: utf-8 -*-
from os import getcwd, listdir
from os.path import exists, join

ARGS = ["inputs", "outputs"]
IN_EXT = ".in"
OUT_EXT = ".out"

def pytest_addoption(parser):
    parser.addoption("--folder", action="store", default="data", help="Path to OTUS test files")
    parser.addoption("--count", action="store", default=None, help="Number of cases")

def pytest_generate_tests(metafunc):
    if all(x in metafunc.fixturenames for x in ARGS):
        path = join(getcwd(), metafunc.config.getoption("folder")) 
        inputs = [file for file in listdir(path) if file.endswith(IN_EXT)]
        inputs = sorted(inputs, key=lambda x: int(x.split('.')[1]))
        cases = []
        for input in inputs:
            output = input[:-len(IN_EXT)] + OUT_EXT
            input_path = join(path, input)
            output_path = join(path, output) 
            if exists(output_path):
                with open(input_path) as fin:
                    input_vals = fin.readlines()
                with open(output_path) as fout:
                    output_vals = fout.readlines()
                cases.append((input_vals, output_vals))
        count = metafunc.config.getoption("count")
        if count is not None:
            cases = cases[:int(count)]
        metafunc.parametrize(",".join(ARGS), cases)
