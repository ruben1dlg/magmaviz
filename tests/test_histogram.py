from magmaviz.histogram import histogram
import altair as alt
import pandas as pd
import pytest
from vega_datasets import data


# def test_histogram_error_for_df():
#     """Tests that an error is raised when df is not a dataframe"""
#     with pytest.raises(TypeError):
#         histogram(["a", 'x', 'y'])


def test_histogram():
    """Unit tests for the histogram function"""
    example1 = histogram(data.iris(), "species", "median(sepalLength)")
    assert example1.encoding.x.shorthand == "species", 'x_axis should be mapped to the x axis'
    assert example1.encoding.y.shorthand == 'median(sepalLength)', 'y_axis should be mapped to the y axis'
    assert example1.encoding.color.scale.scheme == 'magma', 'The color schema should be magma'

