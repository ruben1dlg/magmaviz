def color_boxplot(df, x, y, facet=False):
    """Plot a boxplot with the magma color scheme and an option to facet.

    Parameters
    ----------
    df : dataframe
        Dataframe containing the variables for plotting
    x : string
        Column name of the numerical variable to view the distribution of
    y : list
        Column names of the categorical variables to assign boxes to
    facet : boolean
        Determines whether separate graphs will be created for each category

    Returns
    -------
    altair.vegalite.v4.api.Chart
        Boxplot displaying distribution of categorical variables with/without faceting

    Examples
    --------
    >>> from magmaviz.magmaviz import boxplot
    >>> boxplot(mtcars, horsepower, cars, facet=True)
    """
