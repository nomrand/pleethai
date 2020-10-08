## DBテーブル (詳細)
### Word (単語)テーブル
| カラム名      | Type          | 制約          |内容
| ------------ | ------------- | ------------- | ------------- |
|id            | INT(10)       | primary key<br>not null | 単語ID | 
|japanese      | VARCHAR(127)  | not null      | 日本語 | 
|hiragana      | VARCHAR(127)  | not null      | ひらがな | 
|roman         | VARCHAR(127)  |               | ローマ字 | 
|thai           | VARCHAR(127) | not null      | タイ語訳 | 
|pronunciation_symbol | VARCHAR(127) |         | タイ語発音記号 | 
|pronunciation_kana   | VARCHAR(127) |         | タイ語カタカナ | 
|order         | INT(2)        |               | タイ語訳表示順 | 
|english       | VARCHAR(127)  |               | 英語 | 
|search        | BIGINT(15)    |               | 日本語名のGoogle検索件数 | 
|wordclass_id  | INT(2)        | not null<br>foreign key(WordClass)    | 品詞ID | 
|tags          | VARCHAR(511)  |               | タグの日本語名をカンマ(,)区切りで記述する | 

### WordClass (品詞)テーブル
| カラム名      | Type          | 制約          |内容
| ------------ | ------------- | ------------- | ------------- |
|id            | INT(2)        | primary key<br>not null    | 品詞ID | 
|thai          | VERCHAR(31)   |                | タイ語 | 
|japanese      | VERCHAR(31)   |                | 日本語 | 
|slug          | VERCHAR(31)   |                | 英語 | 


### Example (例文)テーブル
| カラム名      | Type          | 制約          |内容
| ------------ | ------------- | ------------- | ------------- |
|id            | INT(10)       | primary key<br>not null    | 例文ID | 
|japanese      | VARCHAR(511)  | not null      | 日本語 | 
|hiragana      | VARCHAR(511)  |               | ひらがな | 
|roman         | VARCHAR(511)  |               | ローマ字 | 
|thai          | VARCHAR(511)  |               | タイ語訳 | 
|pronunciation_symbol | VARCHAR(511)    |      | タイ語発音記号 | 
|pronunciation_kana   | VARCHAR(511)    |      | タイ語カタカナ | 
|english       | VARCHAR(511)  |               | 英語 | 

### Constituent (例文構成)テーブル
| カラム名      | Type          | 制約          |内容
| ------------ | ------------- | ------------- | ------------- |
|id            | INT(10)       | primary key<br>not null              | 例文構成ID | 
|example_id    | INT(10)       | not null<br>foreign key(Example)    | 例文ID | 
|word_id       | INT(10)       | not null<br>foreign key(SysWordThai) | 例文を構成している単語ID |
|order         | INT(2)        | not null    | 例文を構成している単語の表示順 | 


### Tag (タグ)テーブル
| カラム名      | Type          | 制約          |内容
| ------------ | ------------- | ------------- | ------------- |
|id            | INT           | primary key<br>not null  | タグID | 
|name          | VARCHAR(100)  |               | タグ名 (日本語) | 
|slug          | VARCHAR(100)  |               | タグ名 (英語) | 
|thai          | VARCHAR(100)  |               | タグ名 (タイ語) | 
