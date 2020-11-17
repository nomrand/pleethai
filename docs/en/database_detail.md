# Details of table columns
## Word Table

| Column Name  | Type          | Constraint    | Content
| ------------ | ------------- | ------------- | ------------- |
|id            | INT(10)       | primary key<br>not null | Word ID | 
|japanese      | VARCHAR(127)  | not null      | Japanese | 
|hiragana      | VARCHAR(127)  | not null      | Hiragana | 
|roman         | VARCHAR(127)  |               | Romaji | 
|thai           | VARCHAR(127) | not null      | Thai | 
|pronunciation_symbol | VARCHAR(127) |         | Thai phonetic symbol | 
|pronunciation_kana   | VARCHAR(127) |         | Thai katakana | 
|order         | INT(2)        |               | The order of Thai word to display | 
|english       | VARCHAR(127)  |               | English | 
|search        | BIGINT(15)    |               | Number of Google search hits of Japanese | 
|wordclass_id  | INT(2)        | not null<br>foreign key(WordClass)    | Word Class ID | 
|tags          | VARCHAR(511)  |               | Comma-separated Japanese tags | 


## WordClass Table

| Column Name  | Type          | Constraint    | Content
| ------------ | ------------- | ------------- | ------------- |
|id            | INT(2)        | primary key<br>not null    | Word Class ID | 
|thai          | VERCHAR(31)   |                | Thai  | 
|japanese      | VERCHAR(31)   |                | Japanese | 
|slug          | VERCHAR(31)   |                | English | 


## Example Table

| Column Name  | Type          | Constraint    | Content
| ------------ | ------------- | ------------- | ------------- |
|id            | INT(10)       | primary key<br>not null    | Example ID | 
|japanese      | VARCHAR(511)  | not null      | Japanese | 
|hiragana      | VARCHAR(511)  |               | Hiragana | 
|roman         | VARCHAR(511)  |               | Romaji | 
|thai          | VARCHAR(511)  |               | Thai | 
|pronunciation_symbol | VARCHAR(511)    |      | Thai phonetic | 
|pronunciation_kana   | VARCHAR(511)    |      | Thai katakana | 
|english       | VARCHAR(511)  |               | English | 


## Constituent Table

| Column Name  | Type          | Constraint    | Content
| ------------ | ------------- | ------------- | ------------- |
|id            | INT(10)       | primary key<br>not null              | Constituent ID | 
|example_id    | INT(10)       | not null<br>foreign key(Example)    | Example ID | 
|word_id       | INT(10)       | not null<br>foreign key(SysWordConnector) | Word ID of the words which is in the Sentence (Example) |
|order         | INT(2)        | not null    | The order in which the words in the sentence to display | 


## Tag Table

| Column Name  | Type          | Constraint    | Content
| ------------ | ------------- | ------------- | ------------- |
|id            | INT           | primary key<br>not null  | Tag ID | 
|name          | VARCHAR(100)  |               | Tag (Japanese) | 
|slug          | VARCHAR(100)  |               | Tag (English) | 
|thai          | VARCHAR(100)  |               | Tag (Thai) | 
