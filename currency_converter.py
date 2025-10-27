import requests
import os
import tkinter as tk
from tkinter import messagebox

# APIキーを環境変数から取得python --version
API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
if not API_KEY:
    messagebox.showerror("エラー", "APIキーが設定されていません。環境変数 'EXCHANGE_RATE_API_KEY' を設定してください。")
    exit(1)

# APIエンドポイント
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/JPY"

def get_rates():
    """APIからレートを取得"""
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        data = response.json()
        return data['conversion_rates']
    except requests.exceptions.RequestException as e:
        messagebox.showerror("APIエラー", f"レート取得に失敗しました: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    """換算計算"""
    if from_currency == 'JPY':
        rate = rates[to_currency]
        return amount * rate
    elif to_currency == 'JPY':
        rate = rates[from_currency]
        return amount / rate
    else:
        messagebox.showerror("エラー", "サポートされていない変換です。")
        return None

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("通貨換算アプリ")
        self.rates = get_rates()
        if not self.rates:
            self.root.quit()

        # モード選択（ドロップダウン）
        tk.Label(root, text="換算モード:").grid(row=0, column=0, padx=10, pady=10)
        self.mode_var = tk.StringVar(value="1")
        modes = {
            "1": "円 → ウォン (JPY → KRW)",
            "2": "円 → シンガポールドル (JPY → SGD)",
            "3": "ウォン → 円 (KRW → JPY)",
            "4": "シンガポールドル → 円 (SGD → JPY)"
        }
        self.mode_menu = tk.OptionMenu(root, self.mode_var, *modes.keys(), command=self.update_mode_label)
        self.mode_menu.grid(row=0, column=1, padx=10, pady=10)
        self.mode_label = tk.Label(root, text=modes["1"])
        self.mode_label.grid(row=0, column=2, padx=10, pady=10)

        # 金額入力
        tk.Label(root, text="金額:").grid(row=1, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        # 換算ボタン
        self.convert_button = tk.Button(root, text="換算", command=self.convert)
        self.convert_button.grid(row=2, column=0, columnspan=2, pady=10)

        # 結果表示
        tk.Label(root, text="結果:").grid(row=3, column=0, padx=10, pady=10)
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=3, column=1, padx=10, pady=10)

        # 終了ボタン
        self.quit_button = tk.Button(root, text="終了", command=root.quit)
        self.quit_button.grid(row=4, column=0, columnspan=2, pady=10)

    def update_mode_label(self, value):
        modes = {
            "1": "円 → ウォン (JPY → KRW)",
            "2": "円 → シンガポールドル (JPY → SGD)",
            "3": "ウォン → 円 (KRW → JPY)",
            "4": "シンガポールドル → 円 (SGD → JPY)"
        }
        self.mode_label.config(text=modes[value])

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            mode = self.mode_var.get()
            if mode == '1':
                result = convert_currency(amount, 'JPY', 'KRW', self.rates)
                self.result_label.config(text=f"{amount} JPY = {result:.2f} KRW")
            elif mode == '2':
                result = convert_currency(amount, 'JPY', 'SGD', self.rates)
                self.result_label.config(text=f"{amount} JPY = {result:.2f} SGD")
            elif mode == '3':
                result = convert_currency(amount, 'KRW', 'JPY', self.rates)
                self.result_label.config(text=f"{amount} KRW = {result:.2f} JPY")
            elif mode == '4':
                result = convert_currency(amount, 'SGD', 'JPY', self.rates)
                self.result_label.config(text=f"{amount} SGD = {result:.2f} JPY")
        except ValueError:
            messagebox.showerror("エラー", "金額は数値を入力してください。")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
