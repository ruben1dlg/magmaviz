from magmaviz.scatterplot import scatterplot
import altair as alt
import pandas as pd
import numpy as np
from vega_datasets import data

# sample cars data
sample_data = pd.DataFrame({
        'brand': np.array(["toyota", "hyundai", "volkswagen",
                           "toyota", "hyundai", "volkswagen",
                           "toyota", "hyundai", "volkswagen"]),
        'year': ([2017, 2017, 2017,
                  2016, 2016, 2016,
                  2015, 2015, 2015]),
        'no_of_cars': np.array([10466051, 7218391, 10382334,
                                10213486, 7889538, 10126281,
                                10083831, 7988479, 9872424])
    })

scatter = scatterplot(sample_data, "year", "no_of_cars", "brand")
scatter


def test_scatterplot():
    # check if the dataframe is a pandas dataframe
    if not isinstance(sample_data, pd.core.frame.DataFrame):
        raise TypeError(
            "sample_data should be of a pandas dataframe of type: 'pandas.core.frame.DataFrame'"
        )

def test_enc_x_shorthand():
    """check if the x column is mapped to x-axis"""
    assert scatter.encoding.x.shorthand == 'year', 'x should be mapped to the x-axis'

def test_enc_y_shorthand():
    """check if the y column is mapped to y-axis"""
    assert scatter.encoding.y.shorthand == 'no_of_cars', 'y should be mapped to the y-axis'

def test_color_title():
    """check if the color title reflects the color variable"""
    assert scatter.encoding.color.title == "Brand"

def test_enc_color_scheme():
    """check if the color scheme is set to magma"""
    assert scatter.encoding.color.scale.scheme == 'magma', 'color scale scheme should be magma'

def test_mark_type():
    """check if the mark type is point"""
    assert scatter.mark.type == 'point', 'mark type should be a point'

def test_mark_opacity():
    """check if the mark opacity is 0.5"""
    assert scatter.mark.opacity == 0.5, 'mark opacity should be 0.5'

def test_mark_size():
    """check if the mark size is 50"""
    assert scatter.mark.size == 50, 'mark size should be 50'

def test_enc_x_scale():
    """check if the x axis does not start from zero"""
    assert scatter.encoding.x.scale.zero == False, 'x-axis should not start at 0'

def test_enc_y_scale():
    """check if the y axis does not start from zero"""
    assert scatter.encoding.y.scale.zero == False, 'y-axis should not start at 0'

def test_plot_title():
    """check if the title is correctly updated based on field names"""
    assert scatter.title == 'Year vs No Of Cars by Brand', 'title should be "Year vs No of Cars by Brand"'