import pandas as pd
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
#source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]


### 検索ツール
def search():
    df = pd.read_csv('source.csv')
    source = list(df["name"])

    while True:

        word =input("鬼滅の登場人物の名前を入力してください >>> ")

        ### ここに検索ロジックを書く
        if word in source:

            print("{}が見つかりました".format(word))

        else:
            print("{}が見つかリませんでした".format(word))
            print(word + 'を追加しました')
            source.append(word)

        df = pd.DataFrame(source, columns=["name"])
        df.to_csv("source.csv")
        print(df)

if __name__ == "__main__":
    search()
