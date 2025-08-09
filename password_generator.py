import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import json
import os
from datetime import datetime

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("パスワード生成器")
        self.window.geometry("600x700")
        self.window.configure(bg='#f0f0f0')
        
        # シンプルなカラーテーマ（古いPC対応）
        self.colors = {
            'bg': '#f0f0f0',
            'fg': '#2c3e50',
            'accent': '#3498db',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'card_bg': '#ffffff',
            'button_bg': '#3498db',
            'button_fg': '#ffffff'
        }
        
        # パスワード履歴を保存するファイル
        self.history_file = "password_history.json"
        self.password_history = self.load_history()
        
        self.setup_ui()
        
    def setup_ui(self):
        # メインコンテナ
        main_container = tk.Frame(self.window, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # ヘッダーセクション
        self.create_header(main_container)
        
        # 設定セクション
        self.create_settings_section(main_container)
        
        # 生成セクション
        self.create_generation_section(main_container)
        
        # 履歴セクション
        self.create_history_section(main_container)
        
        self.update_history_display()
        
    def create_header(self, parent):
        """ヘッダーセクションの作成"""
        header_frame = tk.Frame(parent, bg=self.colors['bg'])
        header_frame.pack(fill=tk.X, pady=(0, 15))
        
        # タイトル
        title_label = tk.Label(header_frame, 
                              text="パスワード生成器", 
                              font=("Arial", 18, "bold"),
                              bg=self.colors['bg'],
                              fg=self.colors['accent'])
        title_label.pack()
        
        # サブタイトル
        subtitle_label = tk.Label(header_frame,
                                 text="安全で強力なパスワードを簡単に生成",
                                 font=("Arial", 10),
                                 bg=self.colors['bg'],
                                 fg=self.colors['fg'])
        subtitle_label.pack(pady=(3, 0))
        
    def create_settings_section(self, parent):
        """設定セクションの作成"""
        settings_frame = tk.LabelFrame(parent, 
                                      text="設定", 
                                      font=("Arial", 12, "bold"),
                                      bg=self.colors['card_bg'],
                                      fg=self.colors['fg'],
                                      relief=tk.RAISED,
                                      bd=1)
        settings_frame.pack(fill=tk.X, pady=(0, 15))
        
        # パスワード長設定
        length_frame = tk.Frame(settings_frame, bg=self.colors['card_bg'])
        length_frame.pack(fill=tk.X, padx=15, pady=8)
        
        tk.Label(length_frame, 
                text="パスワード長:", 
                font=("Arial", 10, "bold"),
                bg=self.colors['card_bg'],
                fg=self.colors['fg']).pack(side=tk.LEFT)
        
        self.length_var = tk.StringVar(value="12")
        length_entry = tk.Entry(length_frame, 
                               textvariable=self.length_var, 
                               width=8,
                               font=("Arial", 10),
                               bg=self.colors['bg'],
                               fg=self.colors['fg'])
        length_entry.pack(side=tk.LEFT, padx=(8, 0))
        
        # 文字種選択
        chars_frame = tk.Frame(settings_frame, bg=self.colors['card_bg'])
        chars_frame.pack(fill=tk.X, padx=15, pady=8)
        
        tk.Label(chars_frame, 
                text="文字種:", 
                font=("Arial", 10, "bold"),
                bg=self.colors['card_bg'],
                fg=self.colors['fg']).pack(anchor=tk.W)
        
        # チェックボックスフレーム
        checkbox_frame = tk.Frame(chars_frame, bg=self.colors['card_bg'])
        checkbox_frame.pack(fill=tk.X, pady=(3, 0))
        
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        
        # チェックボックススタイル
        checkbox_style = {
            'bg': self.colors['card_bg'],
            'fg': self.colors['fg'],
            'font': ("Arial", 9),
            'selectcolor': self.colors['accent']
        }
        
        tk.Checkbutton(checkbox_frame, text="大文字 (A-Z)", variable=self.use_uppercase, **checkbox_style).pack(anchor=tk.W)
        tk.Checkbutton(checkbox_frame, text="小文字 (a-z)", variable=self.use_lowercase, **checkbox_style).pack(anchor=tk.W)
        tk.Checkbutton(checkbox_frame, text="数字 (0-9)", variable=self.use_digits, **checkbox_style).pack(anchor=tk.W)
        tk.Checkbutton(checkbox_frame, text="記号 (!@#$%^&*)", variable=self.use_symbols, **checkbox_style).pack(anchor=tk.W)
        
    def create_generation_section(self, parent):
        """生成セクションの作成"""
        generation_frame = tk.LabelFrame(parent,
                                        text="パスワード生成",
                                        font=("Arial", 12, "bold"),
                                        bg=self.colors['card_bg'],
                                        fg=self.colors['fg'],
                                        relief=tk.RAISED,
                                        bd=1)
        generation_frame.pack(fill=tk.X, pady=(0, 15))
        
        # 生成ボタン
        generate_btn = tk.Button(generation_frame,
                                text="パスワード生成",
                                font=("Arial", 12, "bold"),
                                bg=self.colors['button_bg'],
                                fg=self.colors['button_fg'],
                                relief=tk.RAISED,
                                bd=2,
                                command=self.generate_password)
        generate_btn.pack(pady=15)
        
        # パスワード表示エリア
        password_frame = tk.Frame(generation_frame, bg=self.colors['card_bg'])
        password_frame.pack(fill=tk.X, padx=15, pady=(0, 15))
        
        tk.Label(password_frame,
                text="生成されたパスワード:",
                font=("Arial", 10, "bold"),
                bg=self.colors['card_bg'],
                fg=self.colors['fg']).pack(anchor=tk.W)
        
        # パスワード表示フィールド
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(password_frame,
                                      textvariable=self.password_var,
                                      font=("Courier", 12, "bold"),
                                      width=35,
                                      bg=self.colors['bg'],
                                      fg=self.colors['fg'],
                                      relief=tk.SUNKEN,
                                      bd=1)
        self.password_entry.pack(fill=tk.X, pady=(3, 0))
        
        # ボタンフレーム
        button_frame = tk.Frame(password_frame, bg=self.colors['card_bg'])
        button_frame.pack(fill=tk.X, pady=(8, 0))
        
        # パスワード選択ボタン
        select_btn = tk.Button(button_frame,
                              text="パスワードを選択",
                              font=("Arial", 9),
                              bg=self.colors['success'],
                              fg=self.colors['button_fg'],
                              command=self.select_password)
        select_btn.pack(side=tk.LEFT, padx=(0, 8))
        
        # 強度表示
        self.strength_label = tk.Label(button_frame,
                                      text="",
                                      font=("Arial", 10, "bold"),
                                      bg=self.colors['card_bg'],
                                      fg=self.colors['fg'])
        self.strength_label.pack(side=tk.RIGHT)
        
    def create_history_section(self, parent):
        """履歴セクションの作成"""
        history_frame = tk.LabelFrame(parent,
                                     text="生成履歴",
                                     font=("Arial", 12, "bold"),
                                     bg=self.colors['card_bg'],
                                     fg=self.colors['fg'],
                                     relief=tk.RAISED,
                                     bd=1)
        history_frame.pack(fill=tk.BOTH, expand=True)
        
        # 履歴リストボックス
        listbox_frame = tk.Frame(history_frame, bg=self.colors['card_bg'])
        listbox_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=8)
        
        # スクロールバー付きリストボックス
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.history_listbox = tk.Listbox(listbox_frame,
                                         height=6,
                                         width=50,
                                         font=("Courier", 9),
                                         bg=self.colors['bg'],
                                         fg=self.colors['fg'],
                                         selectbackground=self.colors['accent'],
                                         yscrollcommand=scrollbar.set)
        self.history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.history_listbox.yview)
        
        # 履歴操作ボタン
        history_button_frame = tk.Frame(history_frame, bg=self.colors['card_bg'])
        history_button_frame.pack(fill=tk.X, padx=15, pady=(0, 8))
        
        select_history_btn = tk.Button(history_button_frame,
                                      text="選択したパスワードを表示",
                                      font=("Arial", 9),
                                      bg=self.colors['accent'],
                                      fg=self.colors['button_fg'],
                                      command=self.select_from_history)
        select_history_btn.pack(side=tk.LEFT, padx=(0, 8))
        
        clear_history_btn = tk.Button(history_button_frame,
                                     text="履歴をクリア",
                                     font=("Arial", 9),
                                     bg=self.colors['danger'],
                                     fg=self.colors['button_fg'],
                                     command=self.clear_history)
        clear_history_btn.pack(side=tk.LEFT)
        
    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length <= 0:
                messagebox.showerror("エラー", "パスワード長は1以上の整数を入力してください。")
                return
        except ValueError:
            messagebox.showerror("エラー", "パスワード長は数値を入力してください。")
            return
        
        # 使用する文字種を決定
        chars = ""
        if self.use_uppercase.get():
            chars += string.ascii_uppercase
        if self.use_lowercase.get():
            chars += string.ascii_lowercase
        if self.use_digits.get():
            chars += string.digits
        if self.use_symbols.get():
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        if not chars:
            messagebox.showerror("エラー", "少なくとも1つの文字種を選択してください。")
            return
        
        # パスワード生成
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)
        
        # 強度評価
        strength = self.evaluate_strength(password)
        strength_color = self.get_strength_color(strength)
        self.strength_label.config(text=f"強度: {strength}", fg=strength_color)
        
        # 履歴に保存
        self.save_to_history(password, length)
        self.update_history_display()
        
        # 成功メッセージ
        messagebox.showinfo("成功", f"パスワードが生成されました！\n強度: {strength}")
        
    def evaluate_strength(self, password):
        score = 0
        
        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            score += 1
        
        if score <= 2:
            return "弱い"
        elif score <= 4:
            return "普通"
        else:
            return "強い"
    
    def get_strength_color(self, strength):
        """強度に応じた色を返す"""
        if strength == "弱い":
            return self.colors['danger']
        elif strength == "普通":
            return self.colors['warning']
        else:
            return self.colors['success']
    
    def select_password(self):
        password = self.password_var.get()
        if password:
            self.password_entry.select_range(0, tk.END)
            messagebox.showinfo("成功", "パスワードが選択されました。Ctrl+Cでコピーしてください。")
        else:
            messagebox.showwarning("警告", "選択するパスワードがありません。")
    
    def save_to_history(self, password, length):
        history_item = {
            "password": password,
            "length": length,
            "timestamp": datetime.now().isoformat(),
            "strength": self.evaluate_strength(password)
        }
        
        self.password_history.append(history_item)
        
        # 履歴は最新の20件まで保持
        if len(self.password_history) > 20:
            self.password_history = self.password_history[-20:]
        
        self.save_history()
    
    def load_history(self):
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_history(self):
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.password_history, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"履歴の保存に失敗しました: {e}")
    
    def update_history_display(self):
        self.history_listbox.delete(0, tk.END)
        for item in reversed(self.password_history):
            timestamp = datetime.fromisoformat(item["timestamp"]).strftime("%Y-%m-%d %H:%M")
            display_text = f"{timestamp} - 長さ:{item['length']} - 強度:{item['strength']} - {item['password']}"
            self.history_listbox.insert(0, display_text)
    
    def select_from_history(self):
        selection = self.history_listbox.curselection()
        if selection:
            index = selection[0]
            actual_index = len(self.password_history) - 1 - index
            if 0 <= actual_index < len(self.password_history):
                password = self.password_history[actual_index]["password"]
                self.password_var.set(password)
                strength = self.password_history[actual_index]["strength"]
                strength_color = self.get_strength_color(strength)
                self.strength_label.config(text=f"強度: {strength}", fg=strength_color)
                messagebox.showinfo("成功", "選択したパスワードが表示されました。")
        else:
            messagebox.showwarning("警告", "履歴からパスワードを選択してください。")
    
    def clear_history(self):
        if messagebox.askyesno("確認", "パスワード履歴をすべて削除しますか？"):
            self.password_history = []
            self.save_history()
            self.update_history_display()
            messagebox.showinfo("完了", "履歴をクリアしました。")
    
    def run(self):
        self.window.mainloop()

def main():
    app = PasswordGenerator()
    app.run()

if __name__ == "__main__":
    main()
