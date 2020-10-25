from ows_language_model import __version__ as _version
from ows_language_model.predict import (make_single_prediction)


def test_make_single_prediction(test_input_data):
    # Given

    # When
    results = make_single_prediction(input_text=test_input_data)

    # Then
    assert results['predictions'] is not None
    assert results['version'] == _version
