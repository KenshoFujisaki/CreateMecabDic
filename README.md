CreateMecabDic
=========================

WikipediaとはてなブックマークのデータからMeCabの辞書を作成します。  
作成手順は、Wikipedia辞書、はてな辞書ともに同じ流れです。  
ここでは、MacOSX環境を前提としています。  

### 参考サイト
* wikipedia辞書作成 http://tmp.blogdns.org/archives/2009/12/mecabwikipediah.html
* はてな辞書作成 http://d.hatena.ne.jp/MikuHatsune/20130619/1371623163

### Wikipedia辞書作成手順
1. Wikipediaキーワードデータを取得  
```sh
$ brew install wget # 必要であれば
$ wget http://download.wikimedia.org/jawiki/latest/jawiki-latest-all-titles-in-ns0.gz
$ gunzip -v jawiki-latest-all-titles-in-ns0.gz
$ mv jawiki-latest-all-titles-in-ns0 wikipedia.dat
```

2. WikipediaキーワードをMeCab辞書の入力csvの形式に変換  
```sh
$ ruby create_wikipedia_dic.rb wikipedia.dat > wikipedia_keyword.csv
```

3. csvファイルから辞書dic形式に変換(ファイルパスは適宜変更)  
```sh
$ brew install mecab mecab-ipadic # 必要であれば
$ sudo /usr/local/Cellar/mecab/0.996/libexec/mecab/mecab-dict-index -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic/ -u wikipedia.dic -f euc-jp -t utf8 wikipedia_keyword.csv
```

4. 作成したwikipedia.dicをユーザ辞書に登録(ファイルパスは適宜変更)  
```sh
$ cp wikipedia.dic /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic/wikipedia.dic
$ vim /usr/local/etc/mecabrc
dicdir =  /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic
userdic = /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic/wikipedia.dic
```

5. 適切に辞書の登録ができたか確認  
```sh
$ echo 攻殻機動隊 | mecab
攻殻機動隊	名詞,一般,*,*,*,*,攻殻機動隊,*,*,Wikipediaキーワード,
EOS
```
以下のように形態素がバラけなければOK
```
攻  名詞,固有名詞,人名,名,*,*,攻,オサム,オサム
殻  名詞,一般,*,*,*,*,殻,カラ,カラ
機動  名詞,一般,*,*,*,*,機動,キドウ,キドー
隊  名詞,接尾,一般,*,*,*,隊,タイ,タイ
EOS
```

6. ちなみに，mecab -u wikipedia.dicで辞書指定することも可能  
```sh
$ echo 攻殻機動隊 | mecab -u wikipedia.dic
攻殻機動隊	名詞,一般,*,*,*,*,攻殻機動隊,*,*,Wikipediaキーワード,
EOS
```

### はてブ辞書作成手順
1. はてなキーワードデータを取得  
```sh
$ wget http://d.hatena.ne.jp/images/keyword/keywordlist_furigana.csv -O hatena.dat
```

2. はてなキーワードをMeCab辞書の入力csvの形式に変換  
```sh
$ brew install nkf # 必要であれば
$ nkf -Ew hatena.dat | python create_hatena_dict.py | nkf -e > hatena_keyword.csv
```

3. csvファイルから辞書dic形式に変換(ファイルパスは適宜変更)  
```sh
$ sudo /usr/local/Cellar/mecab/0.996/libexec/mecab/mecab-dict-index -d /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic/ -u hatena.dic -f euc-jp -t utf8 hatena_keyword.csv
```

4. 作成したhatena.dicをユーザ辞書に登録(ファイルパスは適宜変更)  
```sh
$ cp hatena.dic /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic/hatena.dic
$ vim /usr/local/etc/mecabrc
dicdir =  /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic
userdic = /usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic/hatena.dic,/usr/local/Cellar/mecab/0.996/lib/mecab/dic/ipadic/wikipedia.dic
```

5. 適切に辞書の登録ができたか確認  
```sh
$ echo 攻殻機動隊 | mecab
攻殻機動隊  名詞,一般,*,*,*,*,攻殻機動隊,*,*,はてなキーワード,
EOS
```
以下のように形態素がバラけなければOK
```
攻  名詞,固有名詞,人名,名,*,*,攻,オサム,オサム
殻  名詞,一般,*,*,*,*,殻,カラ,カラ
機動  名詞,一般,*,*,*,*,機動,キドウ,キドー
隊  名詞,接尾,一般,*,*,*,隊,タイ,タイ
EOS
```

6. ちなみに，mecab -u hatena.dicで辞書指定することも可能  
```sh
$ echo 攻殻機動隊 | mecab -u hatena.dic
攻殻機動隊  名詞,一般,*,*,*,*,攻殻機動隊,*,*,はてなキーワード,
EOS
```
