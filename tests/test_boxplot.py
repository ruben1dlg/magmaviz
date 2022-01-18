from magmaviz.boxplot import boxplot
import altair as alt
import pandas as pd
import numpy as np
from vega_datasets import data


def test_boxplot():

    # create dataframe for testing
    df = pd.DataFrame(zip(Miles_per_gallon, Country_of_Origin))
    df.columns = ["Miles_per_gallon", "Country_of_Origin"]

    # input tests
    # checking that type of column name for x is a string
    if not isinstance("Miles_per_gallon", str):
        raise TypeError("'x' should be of type 'str'.")
    # checking that type of column name for y is a string
    if not isinstance("Country_of_Origin", str):
        raise TypeError("'y' should be of type 'str'.")
    # checking that type for facet is a boolean
    if not isinstance(True, bool):
        raise TypeError("'facet' should be of type 'boolean'.")
    # checking that the dataframe is a pandas dataframe type
    if not isinstance(df, pd.core.frame.DataFrame):
        raise TypeError(
            "'df' should be of type 'pandas.core.frame.DataFrame', a pandas dataframe."
        )

    #Output tests
    #checking if facetting is occurring correctly using type
    assert type(boxplot(df, 'Miles_per_Gallon', 'Country_of_Origin', facet=True))==alt.vegalite.v4.api.FacetChart, "The output should be a faceted chart type"

    assert type(boxplot(df, 'Miles_per_Gallon', 'Country_of_Origin, facet=False))==alt.vegalite.v4.api.Chart, "The output should be an altair chart type"

