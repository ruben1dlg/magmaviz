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

    # check if the dataframe is a pandas dataframe
    if not isinstance(df, pd.core.frame.DataFrame):
        raise TypeError("'df' should be of type 'pandas.core.frame.DataFrame', a pandas dataframe.")

    # check if column name for x-axis is a string
    if not isinstance(x, str):
        raise TypeError("Invalid value passed to 'x' axis: Assign column name as a 'string'.")
        
    # check if column name for y-axis is a string
    if not isinstance(y, str):
        raise TypeError("Invalid value passed to 'y' axis: Assign column name as a 'string'.")

    # check if column name for color is a string
    if not isinstance(c, str):
        raise TypeError("Invalid value passed to 'color' variable: Assign column name as a 'string'.")
    
    # check if column name assigned to x-axis is present in the dataframe
    assert x in list(
        df.columns
    ), "The column specified for 'x' axis does not exist in the dataframe."

    # check if column name assigned to y-axis is present in the dataframe
    assert y in list(
        df.columns
    ), "The column specified for 'y' axis does not exist in the dataframe."
    
    # check if column name assigned to color is present in the dataframe
    assert c in list(
        df.columns
    ), "The column specified for 'color' does not exist in the dataframe."

    # check if x-axis column is numeric or not
    assert is_numeric_dtype(df[x]), "The column assigned to 'x' axis is not of type numeric."
    
    # check if y-axis column is numeric or not
    assert is_numeric_dtype(df[y]), "The column assigned to 'y' axis is not of type numeric."
    
    # check if color column is numeric or not
    assert is_string_dtype(df[c]), "The column assigned to 'color' is not of type string."

    if c == "":
        plot = alt.Chart(
            data=df
        ).mark_point(
            color="purple"
        ).encode(
            alt.X(x, title=f"{x}"),
            alt.Y(y, title=f"{y}")
        )