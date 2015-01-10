# -*- encoding: utf-8 -*-
# original: http://d.hatena.ne.jp/MikuHatsune/20130619/1371623163
import sys
import re

#数字四桁が入ったキーワードは役に立ちませんので検出して飛ばします。
year = re.compile("[0-9]{4}")

#驚くべきことにはてなキーワードには%00というキーワードがありますが、
#これがcsvとして提供されているダンプではヌル文字になっているのでシステム制御文字を非許可にします。
ng = [chr(i) for i in range(0,32)] 

def main():
    for x in sys.stdin:
        if re.search(year,x):
            continue #日付スキップ
        k = re.sub(",", "", x.split("\t")[1].strip()) # 改変箇所。カンマ除去
                if len(k) < 2:
                    continue #一文字スキップ
                for word in ng:
                    if word in k:
                        continue #システム制御文字スキップ

                k = k.lower() #MeCabはケースセンシティブなので小文字に統一して辞書作成
                cost = int(max(-36000, -400 * len(k)**1.5)) #コストについては後述
                print "%s,0,0,%s,名詞,一般,*,*,*,*,%s,*,*,はてなキーワード," % (k,cost,k) #0については後述

if __name__ == '__main__':
    main()
