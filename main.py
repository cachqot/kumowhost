import requests
from flask import *
import xml.etree.ElementTree as ET

app = Flask(__name__)


#とりあえずアクセスされたらそのファイルを返す
@app.route("/g/f/<get_id>")
def file_read(get_id=None):
    send_content,send_mode = file_get("http://drive.google.com/uc?id={}".format(str(get_id)))
    return send_content



#idmap(自分用の疑似的なパス,ディレクトリみたいなやつ)のトップページ実装
@app.route("/g/d/<get_id>")
def dir_read_top(get_id=None):
    get_content,file_mode = file_get("http://drive.google.com/uc?id={}".format(str(get_id)))
    send_str = ""
    send_content = ""

    if file_mode != "text/xml":
        return get_content
        pass
    
    #文字列をxmlに変換
    xml_content = ET.fromstring(get_content)

    #トップページのidを探す
    child = xml_content[0]
    for child in xml_content:
        if str(child.attrib["dir"]) ==  "/":
            send_str,send_mode = file_get("http://drive.google.com/uc?id={}".format(str(child.attrib["id"])))
            break
            pass
        pass

    #print(send_str)

    if send_str != "":
        send_content = make_response(send_str)
        send_content.headers.set('Content-Type', send_mode)
        pass
    else:
        send_content = "404 Error"
        pass
    
    
    return send_content

#idmapへアクセス
#疑似的な自分用のホームページディレクトリみたいな感じ
#コメントは前とほぼ同じなので省略
@app.route("/g/d/<get_id>/<get_dir>")
def dir_read(get_id=None,get_dir=None):
    get_content,file_mode = file_get("http://drive.google.com/uc?id={}".format(str(get_id)))
    send_str = ""
    send_content = ""

    if file_mode != "text/xml":
        return get_content
        pass
    
    #文字列をxmlに変換
    xml_content = ET.fromstring(get_content)

    #今のディレクトリに対応するidからファイルを持ってくる
    child = xml_content[0]
    for child in xml_content:
        if str(child.attrib["dir"]).replace("/", "") ==  str(get_dir):
            send_str,send_mode = file_get("http://drive.google.com/uc?id={}".format(str(child.attrib["id"])))
            break
            pass
        pass

    #print(send_str)

    if send_str != "":
        send_content = make_response(send_str)
        send_content.headers.set('Content-Type', send_mode)
        pass
    else:
        send_content = "404 Error"
        pass
    
    
    return send_content


#idmapの形式
'''
<?xml version="1.0" encoding="UTF-8" ?>
<idlist>
    <url id="1J6z0uYbt3kDyNlDtPey4k3ho5GPhD3v3" dir="home"></url>

</idlist>
'''
#urlタグのidがgoogle drive上のid
#urlタグの内容は実際のurl
#(dimapのgoogle drive上のid)/指定したurlのディレクトリ

#idmapのidがhogehogeだった場合
#hogehoge/homeになる
#↑は(1J6z0uYbt3kDyNlDtPey4k3ho5GPhD3v3)とアクセスしているのと同じこと





#urlにアクセスしてファイルを持ってくる
def file_get(url):
    #urlにアクセスしてバイナリを取ってくる
    res = requests.get(url)

    #ステータスコードが200じゃなかったら終わり
    if res.status_code != 200:
        return "{} Error".format(str(res.status_code)),"text/html"
        pass
    
    res_binaly = res.content
    #print(res_binaly)

    res_binaly = res_binaly.decode('utf-8')

    #print(res_binaly)

    # /{*start_html_page*}/ を探す
    slash_tmp = "" #/ から / の文字を一時的に保存しておく
    slash_mode = False #slash_tmp　に文字を保存するかしないか
    send_mode = "" #何のモードでレスポンスを返すか(html,css,js,image)など(ファイルの形式)
    send_position = 0 #返す文字列が始まる位置
    send_content = "" #res_binaly = res_binaly.decode('utf-8')

    for i in range(len(res_binaly)):
        # "/" があれば(文字列を)区切る
        if res_binaly[i] == "/":
            if slash_mode == False:
                slash_mode = True
            else:
                slash_mode = False
            pass
        #文字を追加
        if slash_mode == True and res_binaly[i] != "/":
            slash_tmp += res_binaly[i]
            pass

        #{*start_XX_page*}を見つけたら指定された形式にする
        if slash_mode == False:
            if slash_tmp == "{*start_html_page*}":
                send_mode = "text/html"
                send_position = i+1
                break
                pass
            elif slash_tmp == "{*start_css_page*}":
                send_mode = "text/css"
                send_position = i+1
                break
                pass
            elif slash_tmp == "{*start_js_page*}":
                send_mode = "text/js"
                send_position = i+1
                break
                pass
            elif slash_tmp == "{*start_png_page*}":
                send_mode = "image/png"
                send_position = i+1
                break
                pass
            elif slash_tmp == "{*start_xml_page*}":
                send_mode = "text/xml"
                send_position = i+1
                break
                pass

            slash_tmp = ""
            pass

        pass



    if send_mode == "":
        send_mode = "text/html"
        send_content = res_binaly
        return send_content,send_mode
        pass
    

    #print(send_mode)

    #返したいコンテンツとってくる

    send_content = res_binaly[send_position:]
    #print(send_content)

    #取り出したコンテンツとファイルの形式を返す
    return send_content,send_mode



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
