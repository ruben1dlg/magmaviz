def corrplot(df, print_corr=True, shape="circle"):
    """Generates a correlation plot for the numeric variables
    in a dataframe, and prints the correlation values.

    Parameters
    ----------
    df : DataFrame
        The dataframe containing the data to be plotted.
    print_corr : boolean
        Determines whether the function will print the
        correlation values after the graph or not.
    shape : string
        Determines the shape to use in the graph to represent
        the value of the correlation. Its possible values 
        are "circle" and "square".

    Returns
    -------
    altair.vegalite.v4.api.Chart
        Correlation plot between the numerical variables
        of a dataframe.

    Examples
    --------
    >>> from magmaviz.magmaviz import corrplot
    >>> corrplot(movies_data, print_corr=True, shape="square")
    """