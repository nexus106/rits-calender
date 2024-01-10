import pandas as pd


def df_year_csv(df, name):
    # 基本は2023年で、1月2月3月のときは2024年の列を追加
    df["年"] = 2023
    df.loc[df["月"].isin([1, 2, 3]), "年"] = 2024
    # 順番を整理
    df = df[["年", "月", "日", "曜", "行事"]]
    df.to_csv(name + ".csv", index=False)


url = "https://www.ritsumei.ac.jp/profile/info/calendar/"
dfs = pd.read_html(url)

# 学部
df_gakubu = pd.concat([dfs[0], dfs[1]], ignore_index=True)
df_year_csv(df_gakubu, "gakubu")

# 大学院文系研究科セメスター制
df_daigakuin_bunkei = pd.concat([dfs[2], dfs[3]], ignore_index=True)
df_year_csv(df_daigakuin_bunkei, "daigakuin_bunkei")

# 大学院理系セメスター制
df_daigakuin_rikei = pd.concat([dfs[4], dfs[5]], ignore_index=True)
df_year_csv(df_daigakuin_rikei, "daigakuin_rikei")

# 大学院クオーター制
df_daigakuin_quarter = pd.concat([dfs[6], dfs[7]], ignore_index=True)
df_year_csv(df_daigakuin_quarter, "daigakuin_quarter")

# 大学院法務研究科
df_daigakuin_houmu = pd.concat([dfs[8], dfs[9]], ignore_index=True)
df_year_csv(df_daigakuin_houmu, "daigakuin_houmu")
