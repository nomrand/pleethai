## DBテーブル
| テーブル名    | 内容           |
| ------------ | ------------- |
| Word         | 単語を管理する。(日本語-タイ語の組み合わせ1つが1レコード。1つの日本語単語が複数のタイ語の意味を持つ場合、複数レコードで表現される) |
| WordClass   | 単語の品詞(名詞、動詞など)を管理する。 |
| Example      | 例文を管理する。 (1つの例文が1レコード) |
| Constituent  | 例文1つがどの単語から構成されているかを管理する。 (例文と単語の組み合わせ1つが1レコード。1つの例文には複数の単語が含まれるため、複数レコードで表現される) |
| Tag          | 単語に紐づくタグ1つを管理する。 |


※以下は、システムが管理するテーブルのため、開発者以外は考慮する必要はない。
| テーブル名    | 内容           |
| ------------ | ------------- |
| TaggedItem  | タグを使用するためのパッケージ (Django-Taggit) に、Tagテーブルをタグと認識させるためのテーブル。 |
| SysWordJapanese | Wordテーブルを分解して、1つの日本語単語を1レコードで表現したもの。 |
| SysWordConnector | Wordテーブルを分解して、単語のタイ語の意味1つを1レコードで表現したもの |


[テーブルの各カラムなどの詳細は、こちらを参照](./database_detail.md)


## ER図
[ER図 by draw.io](https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=gaifaaER#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1-tuw7_afYUL0Ud8UwnJKSjUGH_FEF4Oa%26export%3Ddownload)