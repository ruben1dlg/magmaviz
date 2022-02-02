from magmaviz.boxplot import boxplot
import altair as alt
import pandas as pd

import pytest


def toy_df():
    Miles_per_gallon = [18.0, 15.0, 18.0, 16.0, 17.0, 15.0, 14.0, 14.0, 14.0, 15.0]
    Country_of_origin = [
        "USA",
        "Europe",
        "Europe",
        "Europe",
        "Japan",
        "Japan",
        "Japan",
        "USA",
        "USA",
        "Europe",
    ]

    Engine = [
        2,
        4,
        4,
        2,
        8,
        8,
        8,
        8,
        4,
        2,
    ]

    df = pd.DataFrame(zip(Miles_per_gallon, Country_of_origin, Engine))
    df.columns = ["Miles_per_gallon", "Country_of_origin", "Engine"]

    return df


def test_boxplot_input():

    df = toy_df()

    # input tests
    # checking that type of column name for x is a string
    if not isinstance("Miles_per_gallon", str):
        raise TypeError("'x' should be of type 'str'.")
    # checking that type of column name for y is a string
    if not isinstance("Country_of_origin", str):
        raise TypeError("'y' should be of type 'str'.")
    # checking that type for facet is a boolean
    if not isinstance("Engine", str):
        raise TypeError("'facet_col' should be of type 'str'.")
    # checking that the dataframe is a pandas dataframe type
    if not isinstance(df, pd.core.frame.DataFrame):
        raise TypeError(
            "'df' should be of type 'pandas.core.frame.DataFrame', a pandas dataframe."
        )


def test_error_inputs_df():
    """checking that the dataframe is a pandas dataframe type"""

    df = toy_df()
    with pytest.raises(TypeError):
        boxplot("df", "Miles_per_gallon", "Country_of_origin")


def test_error_inputs_x():
    """checking type error for wrong type of x column name"""
    df = toy_df()
    with pytest.raises(TypeError):
        boxplot(df, ["Miles_per_gallon"], "Country_of_origin")


def test_error_inputs_y():
    """checking type error for wrong type of  y column name"""

    df = toy_df()
    with pytest.raises(TypeError):
        boxplot(df, "Miles_per_gallon", ["Country_of_origin"])


def test_error_inputs_facet():
    """checking error for faceting"""
    df = toy_df()
    with pytest.raises(TypeError):
        boxplot(df, "Miles_per_gallon", "Country_of_origin", facet_col=False)


def test_boxplot_columns_assert():
    """checking assert statemetns for column name tests"""

    df = toy_df()

    # checking if x is a column name in the dataframe
    assert "Miles_per_gallon" in list(
        df.columns
    ), "This column specified for 'x' does not exist in the dataframe."
    # checking if y is a column name in the dataframe
    assert "Country_of_origin" in list(
        df.columns
    ), "This column specified for 'y' does not exist in the dataframe."
    assert "Engine" in list(
        df.columns
    ), "This column specified for 'facet_col' does not exist in the dataframe."


def test_boxplot_output_type_assert():
    """checking output type with/without faceting"""
    df = toy_df()

    # Output tests
    # checking if facetting is occurring correctly using type
    assert (
        type(boxplot(df, "Miles_per_gallon", "Country_of_origin", facet_col="Engine"))
        == alt.vegalite.v4.api.FacetChart
    ), "The output should be a faceted chart type"
    assert (
        type(boxplot(df, "Miles_per_gallon", "Country_of_origin"))
        == alt.vegalite.v4.api.Chart
    ), "The output should be an altair chart type"


def test_boxplot_axis_mapping_assert():
    """Testing the mapping of column names to the axis"""
    df = toy_df()

    assert (
        boxplot(df, "Miles_per_gallon", "Country_of_origin").encoding.x.shorthand
        == "Miles_per_gallon"
    ), "x column should be mapped to the x axis"
    assert (
        boxplot(df, "Miles_per_gallon", "Country_of_origin").encoding.y.shorthand
        == "Country_of_origin"
    ), "y column should be mapped to the y axis"
