import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. データの読み込み
# ファイル名を実際にアップロードしたものに書き換えてください
df = pd.read_csv('トレード結果を出力.csv')

# 2. データのクリーニング（決済行だけを抽出して重複を防ぐ）
# 「タイプ」列に「決済」という文字が含まれる行だけを抽出します
df_clean = df[df['タイプ'].str.contains('決済')].copy()

# 3. 損益データの抽出（列名を正確に指定）
# CSVに合わせて '純損益 JPY' を使用します
trades = df_clean['純損益 JPY'].values

print(f"分析対象のトレード数: {len(trades)}")
print(f"平均損益: {np.mean(trades):.0f} JPY")

# --- モンテカルロ・シミュレーション ---
# 今のトレード結果を1000パターン、ランダムに並び替えてシミュレーションします
n_simulations = 1000
plt.figure(figsize=(12, 6))

for i in range(n_simulations):
    # トレード結果をランダムにシャッフル
    shuffled_trades = np.random.choice(trades, size=len(trades), replace=True)
    # 累積損益を計算
    equity_curve = np.cumsum(shuffled_trades)
    plt.plot(equity_curve, color='blue', alpha=0.05) # 薄い青線で表示

# 実際の累積損益を太い赤線で表示
plt.plot(np.cumsum(trades), color='red', linewidth=2, label='Actual Result')

plt.title('Monte Carlo Simulation (Profit Stability Analysis)')
plt.xlabel('Trade Count')
plt.ylabel('Cumulative Profit (JPY)')
plt.legend()
plt.grid(True)
plt.show()

# --- リスク分析 ---
drawdowns = []
for i in range(1000):
    shuffled = np.random.choice(trades, size=len(trades), replace=True)
    cum_sum = np.cumsum(shuffled)
    # ドローダウンの計算
    running_max = np.maximum.accumulate(cum_sum)
    dd = running_max - cum_sum
    drawdowns.append(np.max(dd))

print(f"--- 統計的リスク診断 ---")
print(f"最悪ケースの予想最大ドローダウン: {np.max(drawdowns):.0f} JPY")
print(f"平均的な最大ドローダウン: {np.mean(drawdowns):.0f} JPY")
