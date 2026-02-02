import pandas as pd

df = pd.read_csv("results/data.csv")
df["kernel_ratio"] = df["kernel_n"] / df["n"]

summary = df.groupby("family").agg(
    trials=("trial","count"),
    n=("n","mean"),
    edges=("edges","mean"),
    kernel_ratio_mean=("kernel_ratio","mean"),
    kernel_ratio_std=("kernel_ratio","std"),
    passes_mean=("passes","mean"),
    time_mean=("time_sec","mean"),
    nid_mean=("NID","mean"),
).reset_index()

summary.to_csv("results/summary.csv", index=False)
print(summary)
print("Wrote results/summary.csv")
