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
    assert scatter.encoding.x.title == 'Year', 'x should be mapped to the x-axis'
    assert scatter.encoding.y.title == 'No of cars', 'y should be mapped to the y-axis'
    assert scatter.mark.type == 'point', 'mark type should be a point'
    assert scatter.mark.opacity == 0.5, 'mark opacity should be 0.5'
    assert scatter.mark.size == 50, 'mark size should be 50'
    assert scatter.encoding.x.scale.zero == False, 'x-axis should not start at 0'
    assert scatter.encoding.y.scale.zero == False, 'y-axis should not start at 0'