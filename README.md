<p align="center">
            <h2 align="center">KumoWhost</h2>
            <p align="center">This can hosting your website in Google Drive.Have a nice day! ;)</p>
            <p align="center">
                <img src="http://img.shields.io/badge/license-MIT-blue.svg?style=flat">
                <img src="http://img.shields.io/badge/language-python-yellow.svg?style=flat">
                <img src="http://img.shields.io/badge/pull requests-welcome-green.svg?style=flat">
                <img src="http://img.shields.io/badge/issue-welcome-green.svg?style=flat">
            </p>
            <br>


## 普通にファイルにアクセスする
https://kumowhost.rihitosan.com/g/f/(google driveのファイルのid)

## ファイルの基本的な作り方

拡張子をbmp,jpg,png,gifなどの画像ファイルの拡張子に変えてください。

そして基本的にファイルの先頭に
```
/{*start_(ファイルの形式)_page*}/
```

を書いて、あとは普通のファイルと変わりはありません。

ファイルの先頭でなくても、レスポンスを返したいコンテンツの先頭に書いてください。

### example

htmlの場合
```
/{*start_html_page*}/
```

cssの場合
```
/{*start_css_page*}/
```

javascriptの場合
```
/{*start_js_page*}/
```


## idmap(疑似的なパス,ディレクトリにアクセスする。あたかも自分用のフォルダーがあるように見せる)
https://kumowhost.rihitosan.com/g/d/(google driveのidmapのid)/(idmapに書いたpath)



## idmap(xml)の中身

表示したいページのidとオリジナルのパスを対応させることができます。

```
<?xml version="1.0" encoding="UTF-8" ?>
<idlist>
    <url id="(表示したいページのid)" dir="(path)"></url>
</idlist>
```

### example


idmap.bmp

```
<?xml version="1.0" encoding="UTF-8" ?>
<idlist>
    <url id="1sK24SecfQ6UB3JnORlmRlJ4LaB_jQk7m" dir="/"></url>
    <url id="16edtxu4mV2xebL5XCVY0ELL1pVbsEFAR" dir="home"></url>
</idlist>
```

この状態でidmap.bmpのidが

```
1zvSgxytPxpQjhiyBIFWzu-ykUttgeuHE
```

だとすると

https://kumowhost.rihitosan.com/g/d/1zvSgxytPxpQjhiyBIFWzu-ykUttgeuHE/home

にアクセスすると

https://kumowhost.rihitosan.com/g/f/16edtxu4mV2xebL5XCVY0ELL1pVbsEFAR

にアクセスしたことになります。



## サイト、ファイル関係

サイトはbmpファイルやjpg,png,gifファイルなどの画像ファイルにしてください。(svgは例外)

htmlファイルやphp（その他zip,exe,txt,bf）などでは管理できません。

サイトを公開するときは、右クリックから[リンクの取得]をクリックして[制限付き]から[リンクを知っている人全員]を選択してください。


## ファイル(サイト)の編集

ファイルの編集は基本的にパソコンのエディターソフトでも行えますが、googledrive上で行うこともできます。

anyfile notepad などを使えばgoogle drive上でも編集できます。

※anyfile notepadを使って損害を負っても一切責任は取りません。



## google search consoleへの登録

google search consoleに登録するためにはidmapを使用しなければなりません。


> 詳しくは idmap(疑似的な...　を参照してください。


まず、google search consoleでメニューでプロパティを選択して自分のサイトのパスを入力します。

すると所有権の確認の画面が出てくるので、

google*****.htmlをダウンロードして


> ファイルの基本的な...


を参考にしてgoogle driveへファイルをアップロードしてください。

そしてgoogle*****.htmlを公開してidを取得します。


そのあとに
>  idmap(疑似的な...


を参考にして、idlistの中に
```
<url id="(取得したid)" dir="google*****.html"></url>
```

あとは確認ボタンを押して完了です。

sitemapなども作ってみてください。
