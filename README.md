# 概要
立命館大学の学年暦 (https://www.ritsumei.ac.jp/profile/info/calendar/) をcsvファイルに書き出し、私のGoogleカレンダーに登録するプログラムです。学年暦を確認するときに、いちいち検索するのが面倒くさいため作成しました。  
現在は2023年度の学年暦が反映されています。

# 仕組み
main.pyでpandasのtableスクレイピング機能を使い、csvファイルに書き出す  
↓  
csv_to_calender.pyでcscファイルを読み取り、Google Calender APIを通じて登録  
Pushされたタイミングに、Github Actions上でプログラムを実行しています。