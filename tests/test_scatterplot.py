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