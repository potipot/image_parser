import pytest
import pandas as pd
from image_parser import *


def test_csv_converter(data_dir, names_json_file, tmp_path):
    expected_output = pd.read_csv(data_dir / 'expected_output.csv')
    output_file = tmp_path/'output.csv'

    converters.to_csv(names_json_file, output_file)
    output = pd.read_csv(output_file)

    assert output.equals(expected_output)


@pytest.mark.parametrize("json_file", ("names_json_file", "ids_json_file"))
def test_csv_converter_multifile(json_file, data_dir, tmp_path, request):
    json_file = request.getfixturevalue(json_file)
    expected_output = pd.read_csv(data_dir / 'expected_output.csv')
    output_file = tmp_path / 'output.csv'

    converters.to_csv(json_file, output_file)
    output = pd.read_csv(output_file)

    assert output.equals(expected_output)
