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
    # 第2章: UNIXコマンド

    [popular-names.txt](/data/popular-names.txt)は、アメリカで生まれた赤ちゃんの「名前」「性別」「人数」「年」をタブ区切り形式で格納したファイルである。以下の処理を行うプログラムを作成し、[popular-names.txt](/data/popular-names.txt)を入力ファイルとして実行せよ。さらに、同様の処理をUNIXコマンドでも実行し、プログラムの実行結果を確認せよ。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 10. 行数のカウント
    ファイルの行数をカウントせよ。確認にはwcコマンドを用いよ。
    """)
    return


@app.cell
def _():
    import os
    from pathlib import Path

    # UNIX
    root_dir = Path(__file__).parent.parent
    popular_names_text = root_dir / "data" / "popular-names.txt"
    ans10 = f"wc -l {popular_names_text}"
    os.system(ans10)

    # Python
    with popular_names_text.open("r", encoding="utf-8") as f10:
        print(len(f10.readlines()))
    return os, popular_names_text


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 11. 先頭からN行を出力
    ファイルの先頭N行だけを表示せよ。例えば、N=10として先頭10行を表示せよ。確認にはheadコマンドを用いよ。
    """)
    return


@app.cell
def _(os, popular_names_text):
    # UNIX
    os.system(f"head -10 {popular_names_text}")

    # Python
    from itertools import islice

    print("=-" * 16)
    with popular_names_text.open("r", encoding="utf-8") as f11:
        head_lines = list(islice(f11, 10))
        print("".join(head_lines))
    return (islice,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 12. 末尾のN行を出力
    ファイルの末尾N行だけを表示せよ。例えば、N=10として末尾10行を表示せよ。確認にはtailコマンドを用いよ。
    """)
    return


@app.cell
def _(os, popular_names_text):
    # UNIX
    os.system(f"tail -10 {popular_names_text}")

    # Python
    from collections import deque

    print("=-" * 16)
    with popular_names_text.open("r", encoding="utf-8") as f:
        tail_lines = deque(f, maxlen=10)
        print("".join(tail_lines))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 13. タブをスペースに置換
    ファイルの先頭10行に対して、タブ1文字につきスペース1文字に置換して出力せよ。確認にはsedコマンド、trコマンド、もしくはexpandコマンドなどを用いよ。
    """)
    return


@app.cell
def _(islice, os, popular_names_text):
    # UNIX
    os.system(f"head -10 {popular_names_text} | tr '\t' ' '")

    # Python
    print("=-" * 16)
    with popular_names_text.open("r", encoding="utf-8") as f13:
        head_lines13 = list(islice(f13, 10))
        print("".join(map(lambda x: x.replace("\t", " "), head_lines13)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 14. 1列目を出力
    ファイルの先頭10行に対して、各行の1列目だけを抜き出して表示せよ。確認にはcutコマンドなどを用いよ。
    """)
    return


@app.cell
def _(islice, os, popular_names_text):
    # UNIX
    os.system(f"head -n 10 {popular_names_text} | cut -f 1")

    # Python
    print("=-" * 16)
    with popular_names_text.open("r", encoding="utf-8") as f14:
        head_lines14 = list(islice(f14, 10))
        print("\n".join(map(lambda x: x.split()[0], head_lines14)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 15. ファイルをN分割する
    ファイルを行単位でN分割し、別のファイルに格納せよ。例えば、N=10としてファイルを10分割せよ。同様の処理をsplitコマンドで実現せよ。
    """)
    return


@app.cell
def _(os, popular_names_text):
    # UNIX
    # NOTE: 実行環境がMacなので１０分割分の行数をハードコーディングして動作を確認した
    os.system(f"split -l 278 -d {popular_names_text} split_files_")

    # Python
    import math

    import polars as pl

    df15 = pl.read_csv(popular_names_text, separator="\t", has_header=False)
    N15 = 10
    lines_per_chunk = math.ceil(len(df15) / N15)
    for i in range(N15):
        cdf15 = df15.slice(i * lines_per_chunk, lines_per_chunk)
        filename = f"split_files_{i:01d}.txt"
        cdf15.write_csv(filename, separator="\t", include_header=False)
    return (pl,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 16. ランダムに各行を並び替える
    ファイルを行単位でランダムに並び替えよ（注意: 各行の内容は変更せずに並び替えよ）。同様の処理をshufコマンドで実現せよ。
    """)
    return


@app.cell
def _(os, pl, popular_names_text):
    ## UNIX
    os.system(f"sort -R {popular_names_text} | head -n 10")

    ## Polars
    df16 = pl.read_csv(popular_names_text, separator="\t", has_header=False)
    shuffled_df = df16.sample(fraction=1.0, shuffle=True)
    shuffled_df.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 17. １列目の文字列の異なり
    1列目の文字列の異なり（文字列の種類）を求めよ。確認にはcut, sort, uniqコマンドを用いよ。
    """)
    return


@app.cell
def _(os, pl, popular_names_text):
    # UNIX
    os.system(f"cut -f1 -d$'\t' {popular_names_text} | LANG=C sort | uniq")
    # Python
    df17 = pl.read_csv(popular_names_text, separator="\t", has_header=False)
    ans17 = df17[:, 0].unique().sort()
    ans17[:10]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 18. 各行の1列目の文字列の出現頻度を求め、出現頻度の高い順に並べる
    1列目の文字列の出現頻度を求め、出現頻度と名前を出現頻度の多い順に並べて表示せよ。確認にはcut, uniq, sortコマンドを用いよ。
    """)
    return


@app.cell
def _(os, pl, popular_names_text):
    # UNIX
    os.system(f"cut -f 1 {popular_names_text} | sort | uniq -c | sort -rn | head -n 10")
    # Python
    df18 = pl.read_csv(popular_names_text, separator="\t", has_header=False)
    ans18 = df18[:, 0].value_counts(sort=True, name="count")
    ans18.head(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 19. 3列目の数値の降順に各行を並び替える
    3列目の数値の逆順でファイルの各行を整列せよ（注意: 各行の内容は変更せずに並び替えよ）。同様の処理をsortコマンドで実現せよ。
    """)
    return


@app.cell
def _(os, pl, popular_names_text):
    # UNIX
    os.system(f"sort -k 3 -n -r -t $'\t' {popular_names_text} | head -n 10")
    # Python
    df19 = pl.read_csv(popular_names_text, separator="\t", has_header=False)
    sorted_df = df19.sort("column_3", descending=True)
    sorted_df.head(10)
    return


if __name__ == "__main__":
    app.run()
