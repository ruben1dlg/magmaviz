from magmaviz.histogram import histogram
import altair as alt
import pandas as pd
import pytest
from vega_datasets import data


def test_histogram():
    """Unit tests for the histogram function"""
    example1 = histogram(data.iris(), "species", "median(sepalLength)")
    assert example1.encoding.x.shorthand == "species", 'x_axis should be mapped to the x axis'
    assert example1.encoding.y.shorthand == 'median(sepalLength)', 'y_axis should be mapped to the y axis'
    assert example1.encoding.color.scale.scheme == 'magma', 'The color schema should be magma'


def test_error_inputs_df():
    """Check if TypeError is raised for incorrect input df"""
    with pytest.raises(TypeError):
        histogram('df','x','count()')
        histogram([3,2,3,2], 'x', 'mean()')
        histogram(1, 'x', 'mean()')
        histogram(True, 'x', 'mean()')

def test_error_inputs_x():
    """Check if TypeError and ValueError are raised for incorrect input x"""
    with pytest.raises(TypeError):
        histogram(data.iris(), 1, 'mean()')
        histogram(data.iris(), species, 'mean()')

    with pytest.raises(ValueError):
        histogram(data.iris(), 'brand', 'mean()')
        histogram(data.iris(), 'specie', 'mean()')

def test_validate():
    """Unit tests for the validate function
    
        Check if ValueError and TypeError are raised for incorrect input y"""
    with pytest.raises(TypeError):
        histogram(data.iris(), 'species', True)
        histogram(data.iris(), 'species', count())
        histogram(data.iris(), 'species', 100.)

    with pytest.raises(ValueError):
        histogram(data.iris(), 'species', 'mean')
        histogram(data.iris(), 'species', 'mean()')
        histogram(data.iris(), 'species', 'mean(petal)')
