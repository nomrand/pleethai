## Database Structure
| Table Name   | Contents      |
| ------------ | ------------- |
| Word         | Manage words (One record means one combination of Japanese-Thai word. If one Japanese word has multiple Thai meanings, it uses 2 or more records) |
| WordClass   | Manage word classes |
| Example      | Manage sentences (One record means one sentence) |
| Constituent  | Manage the relationship between one sentence and words (One record means one combination of a sentence and a word. One sentence uses 2 or more records) |
| Tag          | Manage tags |


* The followings are system managed tables. Non-developers don't have to consider them.

| Table Name   | Contents      |
| ------------ | ------------- |
| TaggedItem  | Table for the package that uses tag (Django-Taggit) |
| SysWordJapanese | Table separated from "Word". One record means one Japanese word |
| SysWordThai     | Table separated from "Word". One record means one Thai word |


[Click here for details on each table column](./database_detail.md)


## Entity-relationship Model
[Entity-relationship Model by draw.io](https://app.diagrams.net/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=gaifaaER#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1-tuw7_afYUL0Ud8UwnJKSjUGH_FEF4Oa%26export%3Ddownload)
