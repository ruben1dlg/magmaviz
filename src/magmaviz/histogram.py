def histogram(df, x, y):
     """Plot a histogram with the magma color scheme

    Parameters
    ----------
    df : dataframe
        Dataframe containing the variables for plotting
    x : string
        Column name of the variable to be plotted on the x-axis
    y : string
        An aggregation function to be plotted on the y-axis.
        The supported aggregation operations are: ['average', 'count',
        'distinct', 'max', 'mean', 'median', 'min', 'missing', 'product',
        'q1', 'q3', 'ci0', 'ci1', 'stderr', 'stdev', 'stdevp', 'sum', 
        'valid', 'values', 'variance', 'variancep']

    Returns
    -------
    altair.vegalite.v4.api.Chart
        A histogram displaying distribution based on the aggregation function

    Examples
    --------
    >>> from magmaviz.magmaviz import histogram
    >>> histogram(mtcars, "cars", "count()")
    """