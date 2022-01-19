import altair as alt
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

import re

def scatterplot(df, x, y, c=""):
    """Plot a scatterplot on the dataframe with the magma color scheme.
    
    Parameters
    ----------
    df : dataframe
        Dataframe containing the numerical features x and y
    x : string
        Column-name of the numerical variable to be plotted on the x-axis
    y : string
        Column-name of the numerical variable to be plotted on the y-axis
    c : string
        Column-name of the categorical variable to color-code the data points
        Default value is blank

    Returns
    -------
    altair.vegalite.v4.api.Chart
        Scatterplot between the numerical variables x and y

    Example
    -------
    >>> from magmaviz.magmaviz import scatterplot
    >>> scatterplot(iris, "Sepal.Length", "Sepal.Width", Species)
    """

    # check if column name for x-axis is a string
    if not isinstance(x, str):
        raise TypeError("Invalid value passed to 'x' axis: Assign column name as a 'string'.")
        
    # check if column name for y-axis is a string
    if not isinstance(y, str):
        raise TypeError("Invalid value passed to 'y' axis: Assign column name as a 'string'.")

    # check if column name for color is a string
    if not isinstance(c, str):
        raise TypeError("Invalid value passed to 'color' variable: Assign column name as a 'string'.")