import argparse
import random
import string
import sys

def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                    use_digits=True, use_symbols=True):
    """
    指定された条件でパスワードを生成する
    
    Args:
        length (int): パスワードの長さ
        use_uppercase (bool): 大文字を使用するか
        use_lowercase (bool): 小文字を使用するか
        use_digits (bool): 数字を使用するか
        use_symbols (bool): 記号を使用するか
    
    Returns:
        str: 生成されたパスワード
    """
    chars = ""
    
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not chars:
        raise ValueError("少なくとも1つの文字種を選択してください。")
    
    return ''.join(random.choice(chars) for _ in range(length))

def evaluate_strength(password):
    """
    パスワードの強度を評価する
    
    Args:
        password (str): 評価するパスワード
    
    Returns:
        str: 強度評価（弱い/普通/強い）
    """
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

def main():
    parser = argparse.ArgumentParser(
        description="パスワード生成器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  python password_generator_cli.py                    # デフォルト設定でパスワード生成
  python password_generator_cli.py -l 16             # 16文字のパスワード生成
  python password_generator_cli.py --no-symbols      # 記号なしでパスワード生成
  python password_generator_cli.py -l 20 -c 5        # 20文字のパスワードを5個生成
        """
    )
    
    parser.add_argument('-l', '--length', type=int, default=12,
                       help='パスワードの長さ (デフォルト: 12)')
    parser.add_argument('-c', '--count', type=int, default=1,
                       help='生成するパスワードの数 (デフォルト: 1)')
    parser.add_argument('--no-uppercase', action='store_true',
                       help='大文字を使用しない')
    parser.add_argument('--no-lowercase', action='store_true',
                       help='小文字を使用しない')
    parser.add_argument('--no-digits', action='store_true',
                       help='数字を使用しない')
    parser.add_argument('--no-symbols', action='store_true',
                       help='記号を使用しない')
    parser.add_argument('--show-strength', action='store_true',
                       help='パスワードの強度を表示する')
    
    args = parser.parse_args()
    
    # 文字種の設定
    use_uppercase = not args.no_uppercase
    use_lowercase = not args.no_lowercase
    use_digits = not args.no_digits
    use_symbols = not args.no_symbols
    
    try:
        # パスワード生成
        for i in range(args.count):
            password = generate_password(
                length=args.length,
                use_uppercase=use_uppercase,
                use_lowercase=use_lowercase,
                use_digits=use_digits,
                use_symbols=use_symbols
            )
            
            if args.count > 1:
                print(f"{i+1}. {password}")
            else:
                print(password)
            
            if args.show_strength:
                strength = evaluate_strength(password)
                print(f"強度: {strength}")
                print()
    
    except ValueError as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
