def histogram(df, x, y):
    """Plot a histogram with the color scheme magma

    Parameters
    ----------
    df : dataframe
        Dataframe containing the variables for plotting
    x : string
        Column name of the variable to be plotted on the x-axis
    y : string
        An aggregation function to be plotted on the y-axis

    Returns
    -------
    altair.vegalite.v4.api.Chart
        A histogram displaying distribution based on the aggregation function

    Examples
    --------
    >>> from magmaviz.magmaviz import histogram
    >>> histogram(mtcars, "cars", "count()")
    """
