import numpy as np
import pandas as pd

serie = pd.Series([1, 2, 3, np.nan, 5, 6])

print("\nOur Serie: \n", serie)

date = pd.date_range("20220801", periods=6)
df = pd.DataFrame(np.random.rand(6, 4), index=date, columns=list("ABCD"))

print("\nOur DataFrame with dates in index: \n", df)

df = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20220701"),
        "C": pd.Series(2.5, index=list(range(5)), dtype="float32"),
        "D": pd.Categorical(["Prod01", "Test01", "Prod02", "Test02", "Train01"]),
        "E": np.array([5] * 5, dtype="int32"),
    }
)

print("\nOther DataFrame: \n", df)
