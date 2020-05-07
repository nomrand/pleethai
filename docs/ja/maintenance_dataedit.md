## 単語・例文追加、変更
新たに単語・例文を追加 or 既存の単語・例文を変更などする場合は、以下の手順で行う。

### 1. 管理ページにログイン
ブラウザで、`システムURL + /admin/`にアクセスする。

- システムURLがhttp://127.0.0.1:8000/ (＝開発環境)の場合、以下のURLにアクセスする。
```
http://127.0.0.1:8000/admin/
```

- システムインストール時に決定した管理ユーザ名、パスワードを入力してログインする。


### 2. データの取得　＆　追加、変更
現在システムに登録されているデータを取得(テーブルエクスポート)し、内容を追加、変更する。
既に登録用のデータが存在している場合(サンプルデータなど)は、次の手順に進む。

1. 管理ページで以下のように操作して、変更が必要なデータをエクスポートする。

<img src ="https://user-images.githubusercontent.com/42882840/80270765-ed9fbe00-86f5-11ea-9b75-14d4c7edd064.png" alt="export 01" width="250"> → <img src ="https://user-images.githubusercontent.com/42882840/80270767-ee385480-86f5-11ea-92fb-ca19a18f074b.png" alt="export 02" width="250"> → <img src ="https://user-images.githubusercontent.com/42882840/80270768-eed0eb00-86f5-11ea-8ac0-a9a67df2058a.png" alt="export 03" width="250">


2. エクスポートしたファイルを編集(行追加、変更)する。
- データの各項目については、[Database](./database.md)を参照。


### 3. データの登録
以下の順序で、用意したデータを登録(インポート)する。
変更がないテーブルについては、登録をスキップしてよい。

1. WordClassテーブル登録

<img src ="https://user-images.githubusercontent.com/42882840/80270793-0e681380-86f6-11ea-8804-5045e35f0fd3.png" alt="import 01" width="250"> → <img src ="https://user-images.githubusercontent.com/42882840/80270795-0f00aa00-86f6-11ea-8e47-b45a8a7bfc63.png" alt="import 02" width="250"> → <img src ="https://user-images.githubusercontent.com/42882840/80270796-0f994080-86f6-11ea-8e60-13772c2a17f1.png" alt="import 03" width="250"> → <img src ="https://user-images.githubusercontent.com/42882840/80270797-0f994080-86f6-11ea-9669-30d2d01bcceb.png" alt="import 04" width="250">

2. Tagテーブル登録
    * 上記と同じようにデータを登録する。

3. Wordテーブル登録
    * 上記と同じようにデータを登録する。

4. Wordテーブルの「変更」を選択し、「UPDATE_SYS_WORD_TABLES」をクリックする (内部データが更新される)。

<img src ="https://user-images.githubusercontent.com/42882840/80270814-39eafe00-86f6-11ea-9a9a-c37c644de894.png" alt="Update_Sys_Word_Tables 01" width="300">

5. Exampleテーブル登録
    * 上記と同じようにデータを登録する。

6. Constituentsテーブル登録
    * 上記と同じようにデータを登録する。

