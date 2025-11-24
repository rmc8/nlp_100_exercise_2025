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
    # 第5章: 大規模言語モデル

    この章では、大規模言語モデル (LLM; Large Language Model) の利用し、様々なタスクに取り組む。大規模言語モデルをプログラムからAPI経由で呼び出すことを想定しており、そのAPIの利用で費用が発生する可能性があることに留意せよ。
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 40. Zero-Shot推論

    以下の問題の解答を作成せよ。ただし、解答生成はzero-shot推論とせよ。

    ```
    9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

    ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
    イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
    ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。
    ```

    出典: [令和5年度第1回高等学校卒業程度認定試験問題](https://www.mext.go.jp/a_menu/koutou/shiken/kakomon/1411255_00010.htm) [日本史AB 問題](https://www.mext.go.jp/content/20240523-mxt_syogai02-mext_000031286_03nihonshi.pdf) 日本史B 1 問3
    """)
    return


@app.cell
def _():
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_google_genai import ChatGoogleGenerativeAI

    model_id = "gemini-2.5-flash"
    llm = ChatGoogleGenerativeAI(model=model_id)
    q40 = """
    9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

    ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
    イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
    ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。

    解答：
    """
    prompt40 = ChatPromptTemplate(messages=[("human", q40)])
    chain40 = prompt40 | llm | StrOutputParser()
    print(chain40.invoke({}))
    return ChatPromptTemplate, StrOutputParser, llm


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 41. Few-Shot推論

    以下の問題と解答を与え、問題40で示した質問の解答をfew-shot推論（この場合は4-shot推論）で生成せよ。

    ```
    日本の近代化に関連するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

    ア　府知事・県令からなる地方官会議が設置された。
    イ　廃藩置県が実施され，中央から府知事・県令が派遣される体制になった。
    ウ　すべての藩主が，天皇に領地と領民を返還した。

    解答: ウ→イ→ア
    ```

    出典: [令和5年度第1回高等学校卒業程度認定試験問題](https://www.mext.go.jp/a_menu/koutou/shiken/kakomon/1411255_00010.htm) [日本史AB 問題](https://www.mext.go.jp/content/20240523-mxt_syogai02-mext_000031286_03nihonshi.pdf) 日本史A 1 問8


    ```
    江戸幕府の北方での対外的な緊張について述べた次の文ア～ウを年代の古い順に正しく並べよ。

    ア　レザノフが長崎に来航したが，幕府が冷淡な対応をしたため，ロシア船が樺太や択捉島を攻撃した。
    イ　ゴローウニンが国後島に上陸し，幕府の役人に捕らえられ抑留された。
    ウ　ラクスマンが根室に来航し，漂流民を届けるとともに通商を求めた。

    解答: ウ→ア→イ
    ```

    出典: [令和5年度第1回高等学校卒業程度認定試験問題](https://www.mext.go.jp/a_menu/koutou/shiken/kakomon/1411255_00010.htm) [日本史AB 問題](https://www.mext.go.jp/content/20240523-mxt_syogai02-mext_000031286_03nihonshi.pdf) 日本史B 3 問3

    ```
    中居屋重兵衛の生涯の期間におこったできごとについて述べた次のア～ウを，年代の古い順に正しく並べよ。

    ア　アヘン戦争がおこり，清がイギリスに敗北した。
    イ　異国船打払令が出され，外国船を撃退することが命じられた。
    ウ　桜田門外の変がおこり，大老の井伊直弼が暗殺された。

    解答: イ→ア→ウ
    ```

    出典: [令和4年度第1回高等学校卒業程度認定試験問題](https://www.mext.go.jp/a_menu/koutou/shiken/kakomon/1411255_00007.htm) [日本史 問題](https://www.mext.go.jp/content/20240513-mxt_syogai02-mext_00002452_03nihonshi.pdf) 日本史A 1 問1


    ```
    加藤高明が外務大臣として提言を行ってから、内閣総理大臣となり演説を行うまでの時期のできごとについて述べた次のア～ウを，年代の古い順に正しく並べよ。

    ア　朝鮮半島において，独立を求める大衆運動である三・一独立運動が展開された。
    イ　関東大震災後の混乱のなかで，朝鮮人や中国人に対する殺傷事件がおきた。
    ウ　日本政府が，袁世凱政府に対して二十一カ条の要求を突き付けた。

    解答: ウ→ア→イ
    ```

    出典: [令和4年度第1回高等学校卒業程度認定試験問題](https://www.mext.go.jp/a_menu/koutou/shiken/kakomon/1411255_00007.htm) [日本史 問題](https://www.mext.go.jp/content/20240513-mxt_syogai02-mext_00002452_03nihonshi.pdf) 日本史A 2 問4
    """)
    return


@app.cell
def _(ChatPromptTemplate, StrOutputParser, llm):
    q41 = """
    以下の例を参考に、最後の問題の解答を導き出してください。

    例題1:
    日本の近代化に関連するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

    ア　府知事・県令からなる地方官会議が設置された。
    イ　廃藩置県が実施され，中央から府知事・県令が派遣される体制になった。
    ウ　すべての藩主が，天皇に領地と領民を返還した。

    解答: ウ→イ→ア

    例題2:
    江戸幕府の北方での対外的な緊張について述べた次の文ア～ウを年代の古い順に正しく並べよ。

    ア　レザノフが長崎に来航したが，幕府が冷淡な対応をしたため，ロシア船が樺太や択捉島を攻撃した。
    イ　ゴローウニンが国後島に上陸し，幕府の役人に捕らえられ抑留された。
    ウ　ラクスマンが根室に来航し，漂流民を届けるとともに通商を求めた。

    解答: ウ→ア→イ

    例題3:
    中居屋重兵衛の生涯の期間におこったできごとについて述べた次のア～ウを，年代の古い順に正しく並べよ。

    ア　アヘン戦争がおこり，清がイギリスに敗北した。
    イ　異国船打払令が出され，外国船を撃退することが命じられた。
    ウ　桜田門外の変がおこり，大老の井伊直弼が暗殺された。

    解答: イ→ア→ウ

    例題4:
    加藤高明が外務大臣として提言を行ってから、内閣総理大臣となり演説を行うまでの時期のできごとについて述べた次のア～ウを，年代の古い順に正しく並べよ。

    ア　朝鮮半島において，独立を求める大衆運動である三・一独立運動が展開された。
    イ　関東大震災後の混乱のなかで，朝鮮人や中国人に対する殺傷事件がおきた。
    ウ　日本政府が，袁世凱政府に対して二十一カ条の要求を突き付けた。

    解答: ウ→ア→イ

    問題:
    9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

    ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
    イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
    ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。

    解答： 
    """

    prompt41 = ChatPromptTemplate(messages=[("human", q41)])
    chain41 = prompt41 | llm | StrOutputParser()
    print(chain41.invoke({}))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 42. 多肢選択問題の正解率

    [JMMLU](https://github.com/nlp-waseda/JMMLU) のいずれかの科目を大規模言語モデルに解答させ、その正解率を求めよ。
    """)
    return


@app.cell
def _(ChatPromptTemplate, llm):
    from typing_extensions import Literal

    import httpx
    import polars as pl
    from pydantic import BaseModel
    from tqdm import tqdm


    class AnswerModel(BaseModel):
        answer: Literal["A", "B", "C", "D"]


    class JMMLUEvaluator:
        prompt = """
        # 指示
        以下の問題に対して、選択肢の中から最も適切なものを1つ選んでください。

        # 問題
        {q}
    
        ## 選択肢
        A. {a}
        B. {b}
        C. {c}
        D. {d}
        """

        def __init__(self, df, llm):
            self.llm = llm
            self.df = df
            self.accuracy_count = 0

        def run_benchmark(self):
            self.accuracy_count = 0
            prompt = ChatPromptTemplate(messages=[("human", self.prompt)])
            chain = prompt | self.llm.with_structured_output(AnswerModel)
            for row in tqdm(self.df.iter_rows(named=True)):
                res = chain.invoke(
                    {
                        "q": row["column_1"],
                        "a": row["column_2"],
                        "b": row["column_3"],
                        "c": row["column_4"],
                        "d": row["column_5"],
                    }
                )
                answer = res.answer
                self.accuracy_count += answer == row["column_6"]

        def get_accuracy_rate(self):
            return self.accuracy_count / len(self.df)


    BASE_URL42 = "https://raw.githubusercontent.com/nlp-waseda/JMMLU/refs/heads/main/JMMLU/{}"
    subject42 = "global_facts.csv"
    url42 = BASE_URL42.format(subject42)
    res = httpx.get(url42)
    df42 = pl.read_csv(res.content, separator=",", has_header=False)
    je = JMMLUEvaluator(df=df42, llm=llm)
    je.run_benchmark()
    je.get_accuracy_rate()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
