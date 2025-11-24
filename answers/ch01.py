import marimo

__generated_with = "0.18.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # 第1章: 準備運動
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 00. パタトクカシーー
    2つの文字列「パトカー」と「タクシー」の文字を先頭から交互に連結し、文字列「パタトクカシーー」を得よ。
    """)
    return


@app.cell
def _():
    a = "パトカー"
    b = "タクシー"
    ans0 = "".join([f"{c}{d}" for c, d in zip(a, b)])
    ans0
    return (ans0,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 01. タクシー
    文字列「パタトクカシーー」の2, 4, 6, 8文字目を取り出し、それらを連結した文字列を得よ。
    """)
    return


@app.cell
def _(ans0):
    ans1 = ans0[1::2]
    ans1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 02. 文字列の逆順
    文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ。
    """)
    return


@app.cell
def _():
    q2 = "stressed"
    q2[::-1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 03. 円周率
    "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し、各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ。
    """)
    return


@app.cell
def _():
    q3 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    words = q3.split()
    ans3 = [len(w) for w in words]
    ans3
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 04. 元素記号
    "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し、1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字、それ以外の単語は先頭の2文字を取り出し、取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ。
    """)
    return


@app.cell
def _():
    def get_elm_symbol(text, idx):
        if idx in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            return text[0]
        return text[:2]

    q4 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    elm_symbols_dict = {}
    for i, text in enumerate(q4.split(), 1):
        elm_symbols_dict[i] = get_elm_symbol(text, i)
    print(elm_symbols_dict)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 05. n-gram
    与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ。この関数を用い、"I am an NLPer"という文から文字tri-gram、単語bi-gramを得よ。
    """)
    return


@app.cell
def _():
    from typing import Sequence

    def get_n_gram(target: Sequence, n: int) -> list[str]:
        return [target[i : i + n] for i in range(len(target) - n + 1)]

    q5 = "I am an NLPer"
    # str
    print(get_n_gram(q5, 3))  # tri-gram
    print(get_n_gram(q5, 2))  # bi-gram
    # list
    q5_list = q5.split()
    print(get_n_gram(q5_list, 3))  # tri-gram
    print(get_n_gram(q5_list, 2))  # bi-gram
    return (get_n_gram,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を、それぞれ, $X$ と $Y$ として求め、$X$ と $Y$ の和集合（$X \cup Y$）、積集合（$X \cap Y$）、差集合（$X \setminus Y$）を求めよ。さらに、'se'というbi-gramがXおよびYに含まれるかどうかを調べよ。
    """)
    return


@app.cell
def _(get_n_gram):
    X = set(get_n_gram("paraparaparadise", 2))
    Y = set(get_n_gram("paragraph", 2))
    print("和集合", X | Y)
    print("積集合", X & Y)
    print("差集合", X - Y)
    print("Xにseが含まれるか", "se" in X)
    print("Yにseが含まれるか", "se" in Y)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 07. テンプレートによる文生成
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ。さらに、x=12, y="気温", z=22.4として、実行結果を確認せよ。
    """)
    return


@app.cell
def _():
    def template(x, y, z) -> str:
        return f"{x}時の{y}は{z}"

    args = {"x": 12, "y": "気温", "z": 22.4}
    template(**args)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 08. 暗号文
    与えられた文字列の各文字を、以下の仕様で変換する関数cipherを実装せよ。

    * 英小文字ならば (219 - 文字コード) のASCIIコードに対応する文字に置換
    * その他の文字はそのまま出力

    この関数を用い、英語のメッセージを暗号化・復号化せよ。
    """)
    return


@app.cell
def _():
    def cipher(c) -> str:
        if "a" <= c <= "z":
            new_code = 219 - ord(c)
            return chr(new_code)
        return c

    q8_text = "I wanna eat banana!"
    ans8 = "".join(map(cipher, q8_text))
    print(ans8)
    print("".join(map(cipher, ans8)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 09. Typoglycemia
    スペースで区切られた単語列に対して、各単語の先頭と末尾の文字は残し、それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ。ただし、長さが４以下の単語は並び替えないこととする。適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え、その実行結果を確認せよ。
    """)
    return


@app.cell
def _():
    import random

    def shuffle(text: str) -> str:
        if len(text) <= 4:
            return text
        a, *b, c = list(text)
        random.shuffle(b)
        return a + "".join(b) + c

    q9 = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    " ".join(map(shuffle, q9.split()))
    return


if __name__ == "__main__":
    app.run()
