実行方法
1. python kadai1.py
-> sim_result.txt,poin_resul.txtが出力される．

2. python fig_o.py sim_result.txt poin_kadai3.txt
-> x-y平面, 時間波形,ポアンカレのグラフが出力

3. python kadai3.py
-> kadai3_result.txt,poin_kadai3.txt,para_change.txtが出力される．

4. python fig_o.py kadai3_result.txt
-> u-v平面出力

5. python fig_o.py para_change.txt poin_kadai3.txt
-> 2.と同様の出力

＜ファイルについて＞
sim_result.txt : ダッフィをルンゲクッタ法でといた結果
poin_result.txt,poin_kadai3.txt: 2パイ起きの解
kadai3_result.txt : ダッフィを平均化法でといた結果
para_change.txt : u.v -> x,yに変更結果
