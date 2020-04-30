import json
import os
from inspect import getsourcefile

from some_function import transform

here = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
source_path = os.path.abspath(os.path.join(here, '../..'))


def test_transform():
    input_path = os.path.join(source_path, "data_input")
    output_expected_path = "data_output_expected"
    with open(input_path, 'r') as f:
        input_data = json.load(f)

    actual = transform(input_data)

    assert actual == output_expected_path
