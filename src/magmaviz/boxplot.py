import altair as alt
import re


def boxplot(df, x, y, facet=False):
    """Plot a boxplot with the magma color scheme and an option to facet.

    Parameters
    ----------
    df : dataframe
        Dataframe containing the variables for plotting
    x : string
        Column name of the numerical variable to view the distribution of
    y : list
        Column name containing the categorical variables to assign boxes to
    facet : boolean
        Determines whether separate graphs will be created for each category

    Returns
    -------
    altair.vegalite.v4.api.Chart
        Boxplot displaying distribution of categorical variables with/without faceting

    Examples
    --------
    >>> from magmaviz.magmaviz import boxplot
    >>> boxplot(cars, "Miles_per_Gallon", "Origin", facet=True)
    """
    # creating titles
    x_title = re.sub(r"[_.,-]", " ", x)

    y_title = re.sub(r"[_.,-]", " ", y)

    # creating plot object
    plot = (
        alt.Chart(df)
        .mark_boxplot()
        .encode(
            x=alt.X(x, title=x_title),
            y=alt.Y(y, title=y_title),
            color=alt.Color(y, scale=alt.Scale(scheme="magma")),
        )
    )

    # facet if required

    if facet == True:
        return plot.facet(row=y)
    else:
        return plot
