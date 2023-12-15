import pandas as pd

pd.set_option('display.max_rows', 150)

url = 'https://www.ritsumei.ac.jp/profile/info/calendar/'
dfs = pd.read_html(url)

print(len(dfs))

# for item in dfs:
#     print(item)

df_gakubu = pd.concat([dfs[0], dfs[1]], ignore_index=True)

df_gakubu.to_csv("gakubu.csv")
