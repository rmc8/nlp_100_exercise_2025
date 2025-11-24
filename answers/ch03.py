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
    # 第3章: 正規表現
    Wikipediaの記事を以下のフォーマットで書き出したファイル[jawiki-country.json.gz](/data/jawiki-country.json.gz)がある。

    * 1行に1記事の情報がJSON形式で格納される
    * 各行には記事名が"title"キーに、記事本文が"text"キーの辞書オブジェクトに格納され、そのオブジェクトがJSON形式で書き出される
    * ファイル全体はgzipで圧縮される

    以下の処理を行うプログラムを作成せよ。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 20. JSONデータの読み込み
    Wikipedia記事のJSONファイルを読み込み、「イギリス」に関する記事本文を表示せよ。問題21-29では、ここで抽出した記事本文に対して実行せよ。
    """)
    return


@app.cell
def _():
    from pathlib import Path
    import polars as pl

    root_dir = Path(__file__).parent.parent
    enwiki = root_dir / "data" / "enwiki-country.json.gz"

    df20 = pl.read_ndjson(enwiki)
    uk_text = df20.filter(pl.col("title") == "United Kingdom").select("text").item()
    uk_text
    return (uk_text,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 21. カテゴリ名を含む行を抽出
    記事中でカテゴリ名を宣言している行を抽出せよ。
    """)
    return


@app.cell
def _(uk_text):
    uk_texts = uk_text.split("\n")
    ans21 = list(filter(lambda x: "[Category:" in x, uk_texts))
    ans21
    return (ans21,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 22. カテゴリ名の抽出
    記事のカテゴリ名を（行単位ではなく名前で）抽出せよ。
    """)
    return


@app.cell
def _(ans21):
    import re

    ptn22 = re.compile(r"^\[\[Category:(.+?)(?:\|.*)?\]\]$")
    ans22 = [ptn22.match(line).group(1) for line in ans21]
    "\n".join(ans22)
    return (re,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 23. セクション構造
    記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ。
    """)
    return


@app.cell
def _(re, uk_text):
    ptn23 = re.compile(r"^(=+)\s*(.*?)\s*\1$", re.MULTILINE)
    for match in ptn23.finditer(uk_text):
        level_str = match.group(1)
        name = match.group(2)
        level = len(level_str) - 1    
        print(f"{level} {name}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 24. ファイル参照の抽出
    記事から参照されているメディアファイルをすべて抜き出せ。
    """)
    return


@app.cell
def _(re, uk_text):
    ptn24 = re.compile(r"\[\[(?:File|ファイル):([^|\]]+)")
    for f24 in ptn24.findall(uk_text):
        print(f24)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 25. テンプレートの抽出
    記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し、辞書オブジェクトとして格納せよ。
    """)
    return


@app.cell
def _(re, uk_text):
    ptn25 = re.compile(r"^\{\{(?:Infobox).*?(?:^\}\}$)", re.MULTILINE | re.DOTALL)
    block_match = ptn25.search(uk_text)
    if block_match:
        template_content = block_match.group(0)
        pattern_field = re.compile(r"^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n\}\}))", re.MULTILINE | re.DOTALL)
        infobox_dict = {m[0].strip(): m[1].strip() for m in pattern_field.findall(template_content)}
        for k, v in list(infobox_dict.items())[:16]: # 16個だけ表示
            print(f"[{k}] : {v}")
    return


if __name__ == "__main__":
    app.run()
