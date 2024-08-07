import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("allwell.csv")
df.drop(["All Time Peak","Peak","Actual gross(in 2022 dollars)"],axis=1,inplace=True)
lst = "[]"

print(df.head())
# print(df["Actual gross(in 2022 dollars)"].head())
df["Ref."] = df["Ref."].str.strip("[]")
df["Tour title"] = df["Tour title"].str.strip("[] †*‡[21][a]‡[4][a]")
df["Actual gross"] = df["Actual gross"].str.strip("[b][e]$")
# df["Actual gross"].astype(int)
df.loc[16,"Ref."] = 18
# df[]
df.loc[10,"Ref."] = 15
print(df.to_string())
print(df.shape)
rank = df["Rank"]
ref = df["Ref."].astype(int)
show = df["Shows"]
# for x in df.index:
#   if df.loc[x] > 120:
#     df.drop(x, inplace = True)
print(df.head())
print(df.info())
print(df[["Rank","Shows","Ref."]].corr())

# plt.scatter(ref,rank, c ="red")
f = plt.figure()
f.set_figwidth(10.5)
plt.bar(df["Artist"],df["Shows"])
plt.legend("Artist")
plt.title("Artists and show!")
plt.xlabel("Artist")
plt.ylabel("Shows")
# plt.scatter(ref,show, c ="blue")
# plt.scatter(rank,show, c ="purple")

# plt.scatter(age,weight, c ="red")
plt.show()
# plt.show()
# plt.show()
    
print(rank)
print(ref)