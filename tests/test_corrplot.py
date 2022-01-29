from magmaviz.corrplot import corrplot
import altair as alt
import pandas as pd
import pytest
from vega_datasets import data


def test_corrplot_error_for_df():
    """Tests that an error is raised when df is not a dataframe"""
    with pytest.raises(TypeError):
        corrplot(["a", 2])

def test_corrplot_error_for_print_corr():
    """Tests that an error is raised when print_corr is not boolean"""
    df = data.cars()
    with pytest.raises(TypeError):
        corrplot(df, 1)

def test_corrplot_error_for_shape():
    """Tests that an error is raised when shape is not string"""
    df = data.cars()
    with pytest.raises(TypeError):
        corrplot(df, True, 2)

def test_corrplot_invalid_shape():
    """Tests an error is raised when shape has an invalid value"""
    df = data.cars()
    with pytest.raises(ValueError):
        corrplot(df, True, "sphere")

def test_corrplot_chart_shape_circle():
    """Tests that the shape in the plot corresponds to the input parameters"""
    df = data.cars()
    plot = corrplot(df)
    assert plot.mark == "circle", "The mark type of the chart should be 'circle'"

def test_corrplot_chart_shape_square():
    """Tests that the shape in the plot corresponds to the input parameters"""
    df = data.cars()
    plot = corrplot(df, shape="square")
    assert plot.mark == "square", "The mark type of the chart should be 'square'"

def test_corrplot_variable_vs_itself():
    """Tests if the correlations between a variable vs itself are set to zero"""
    df = data.cars()
    plot = corrplot(df)
    mysum = 0
    for i in range(len(plot.data["Variable1"].tolist())):
        if plot.data["Variable1"].tolist()[i] == plot.data["Variable2"].tolist()[i]:
            mysum += plot.data["abs"].tolist()[i]

    assert mysum == 0, "Correlations between the variable and itself are different to zero"

def test_corrplot_number_of_numeric_variables():
    """Tests if the plot is taking all the numeric variables in the dataframe"""
    df = data.cars()
    plot = corrplot(df)
    assert (
        len(df.select_dtypes('number').columns.tolist()) == len(plot.data["Variable1"].unique())
    ), "The plot is not taking in consideration the complete set of numeric variables"

def test_corrplot_output_chart_type():
    """Tests that the output is of type Altair Chart"""
    df = data.cars()
    plot = corrplot(df)
    assert (
        type(plot) == alt.vegalite.v4.api.Chart
    ), "The output should be an altair chart type"

def test_corrplot_chart_columns_are_numeric():
    """Tests if all the columns in the chart are numeric"""
    df = data.cars()
    plot = corrplot(df)
    numeric_cols = plot.data["Variable1"].unique().tolist()
    mysum = 0
    for col in numeric_cols:
        if df[col].dtype == 'float' or df[col].dtype == 'int' or df[col].dtype == 'float64' or df[col].dtype == 'int64':
            mysum += 1

    assert len(numeric_cols) == mysum, "There are columns used in the chart that are not numeric"  