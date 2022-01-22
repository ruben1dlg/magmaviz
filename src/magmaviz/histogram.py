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
    # check if the type of df is a pandas DataFrame
    if not isinstance(df, pd.core.frame.DataFrame):
        raise TypeError(
            "'df' should be of type 'pandas.core.frame.DataFrame', a pandas dataframe.")
        
    # check if the type of x is a string
    if not isinstance(x, str):
        raise TypeError("'x' should be of type 'str'.")
    
    # check if x is a column in the dataframe
    if x not in list(df.columns):
        raise ValueError("The column specified for 'x' does not exist in the dataframe.")
    
    # check if the type of y is a string
    if not isinstance(y, str):
        raise TypeError("'y' should be of type 'str'.")
           
    # check if y is a supported aggregation function
    if y not in list(['average', 'count',
        'distinct', 'max', 'mean', 'median', 'min', 'missing', 'product',
        'q1', 'q3', 'ci0', 'ci1', 'stderr', 'stdev', 'stdevp', 'sum', 
        'valid', 'values', 'variance', 'variancep']):
        raise SchemaValidationError(
            "The aggregation function specified for 'y' is not supported.")
