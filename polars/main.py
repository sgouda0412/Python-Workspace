import polars as pl
from IPython.display import display

df_polar = pl.read_csv("data.csv")
display(df_polar.head(2))
