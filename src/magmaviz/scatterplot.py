import altair as alt
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
import re

def scatterplot(df, x, y, c="", t="", xtitle="", ytitle="", ctitle=""):
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
    t : string
        Title of the plot. Default value is blank. If not provided,
        title will be computed based on x, y and/or c
    xtitle : string
             Title of the x-axis. Default value is blank. If not provided,
             title will be proper case of the x axis column
    ytitle : string
             Title of the y-axis. Default value is blank. If not provided,
             title will be proper case of the y axis column
    ctitle : string
             Title of the color legend. Default value is blank. If not provided,
             title will be proper case of the color column

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

    # check if title is a string
    if not isinstance(t, str):
        raise TypeError("Invalid value passed to 't' variable: Assign title as a 'string'.")

    # check if x-axis title is a string
    if not isinstance(xtitle, str):
        raise TypeError("Invalid value passed to 'xtitle' variable: Assign x-axis title as a 'string'.")

    # check if y-axis title is a string
    if not isinstance(ytitle, str):
        raise TypeError("Invalid value passed to 'ytitle' variable: Assign y-axis title as a 'string'.")

    # check if color legend title is a string
    if not isinstance(ctitle, str):
        raise TypeError("Invalid value passed to 'ctitle' variable: Assign color legend title as a 'string'.")

    # check if column name assigned to x-axis is present in the dataframe
    assert x in list(
        df.columns
    ), "The column specified for 'x' axis does not exist in the dataframe."

    # check if column name assigned to y-axis is present in the dataframe
    assert y in list(
        df.columns
    ), "The column specified for 'y' axis does not exist in the dataframe."

    # check if column name assigned to color is present in the dataframe
    if c != "":
        assert c in list(
            df.columns
        ), "The column specified for 'color' does not exist in the dataframe."

    # check if x-axis column is numeric or not
    assert is_numeric_dtype(df[x]), "The column assigned to 'x' axis is not of type numeric."

    # check if y-axis column is numeric or not
    assert is_numeric_dtype(df[y]), "The column assigned to 'y' axis is not of type numeric."

    # check if color column is string or not
    if c != "":
        assert is_string_dtype(df[c]), "The column assigned to 'color' is not of type string."

    # Added proper titles to axes, legend and plot
    if xtitle == "":
        xtitle = re.sub(r"[_.,-]", " ", x)
    if ytitle == "":
        ytitle = re.sub(r"[_.,-]", " ", y)
    if ctitle == "":
        ctitle = re.sub(r"[_.,-]", " ", c)
    if t == "":
        if c == "":
            t = f"{xtitle.title()} vs {ytitle.title()}"
        else:
            t = f"{xtitle.title()} vs {ytitle.title()} by {ctitle.title()}"

    if c == "":
        plot = alt.Chart(
            data=df, title=t
        ).mark_point(
            color="purple"
        ).encode(
            alt.X(x, title=xtitle.capitalize()),
            alt.Y(y, title=ytitle.capitalize())
        )
    else:
        plot = alt.Chart(
            data=df, title=t
        ).mark_point(
        ).encode(
            alt.X(x, title=xtitle.capitalize()),
            alt.Y(y, title=ytitle.capitalize()),
            alt.Color(c, title=ctitle.capitalize(), scale=alt.Scale(scheme="magma"))
        )

    return plot