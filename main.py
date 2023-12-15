import pandas as pd


url = 'https://www.ritsumei.ac.jp/profile/info/calendar/'
dfs = pd.read_html(url)

# 学部
df_gakubu = pd.concat([dfs[0], dfs[1]], ignore_index=True)
df_gakubu.to_csv("gakubu.csv", index=False)

# 大学院文系研究科セメスター制
df_daigakuin_bunkei_semester = pd.concat([dfs[2], dfs[3]], ignore_index=True)
df_daigakuin_bunkei_semester.to_csv("daigakuin_semester_bunkei.csv", index=False)

# 大学院理系セメスター制
df_daigakuin_rikei_semester = pd.concat([dfs[4], dfs[5]], ignore_index=True)
df_daigakuin_rikei_semester.to_csv("daigakuin_semester_rikei.csv", index=False)

# 大学院クオーター制
df_daigakuin_quarter = pd.concat([dfs[6], dfs[7]], ignore_index=True)
df_daigakuin_quarter.to_csv("daigakuin_semester_quarter.csv", index=False)

# 大学院法務研究科
df_daigakuin_houmu = pd.concat([dfs[8], dfs[9]], ignore_index=True)
df_daigakuin_houmu.to_csv("daigakuin_houmu.csv", index=False)
