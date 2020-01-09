import json
import re
import threading

import requests
from colorama import init, Fore

init()

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
}

module = ["md5online", "bugbank", "gongjuji", "hashtoolkit", "my_addr", "gromweb", "nitrxgen", "tellyou"]


def md5online(md5):
    url = "https://www.md5online.org/md5-decrypt.html"
    data = "hash=" + md5
    request = requests.post(url, data=data, headers=headers)

    html = re.compile(r"<span style=\"color:(.*)\">")

    htmlC = html.findall(request.text)

    if htmlC[0] == "limegreen":

        HTMLValue = re.compile(r"<b>(.*)</b>")

        VauleC = HTMLValue.findall(request.text)

        print(Fore.GREEN + " [+] www.md5online.org MD5值：" + md5 + " 已查到解密值：" + VauleC[0] + "\n")
    elif htmlC[0] == "red":
        print(Fore.RED + " [-] www.md5online.org MD5值：" + md5 + " 未查到解密值\n")


def bugbank(md5):
    url = "https://www.bugbank.cn/api/md5"
    data = "md5text=" + md5
    request = requests.post(url, data=data, headers=headers)

    Value = json.loads(request.text)

    if "answer" in Value:
        print(Fore.GREEN + " [+] www.bugbank.cn MD5值：" + md5 + " 已查到解密值：" + Value['answer'] + "\n")
    else:
        print(Fore.RED + " [-] www.bugbank.cn MD5值：" + md5 + " 未查到解密值\n")


def gongjuji(md5):
    url = "http://md5.gongjuji.net/common/md5dencrypt?UpperCase=" + md5

    request = requests.get(url, headers=headers)

    Value = json.loads(request.text)

    if Value['status'] == 1:
        md5Value = Value['data']['PlainText']
        print(Fore.GREEN + " [+] md5.gongjuji.net MD5值：" + md5 + " 已查到解密值：" + md5Value + "\n")
    else:
        print(Fore.RED + " [-] md5.gongjuji.net MD5值：" + md5 + " 未查到解密值\n")


def hashtoolkit(md5):
    url = "https://hashtoolkit.com/reverse-hash/?hash=" + md5

    request = requests.get(url, headers=headers)

    html = re.compile(r"<span title=\"decrypted md5 hash\">(.*)</span>")

    htmlC = html.findall(request.text)

    if htmlC:
        print(Fore.GREEN + " [+] hashtoolkit.com MD5值：" + md5 + " 已查到解密值：" + htmlC[0] + "\n")
    else:
        print(Fore.RED + " [-] hashtoolkit.com MD5值：" + md5 + " 未查到解密值\n")


def my_addr(md5):
    url = "http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php"

    data = "md5=" + md5 + "&x=16&y=15"

    request = requests.post(url, data=data, headers=headers)

    html = re.compile(r"<div class=\'white_bg_title\'><span class=\'middle_title\'>Hashed string</span>: (.*)</div>")

    htmlC = html.findall(request.text)

    if htmlC:
        print(Fore.GREEN + " [+] md5.my-addr.com MD5值：" + md5 + " 已查到解密值：" + htmlC[0] + "\n")
    else:
        print(Fore.RED + " [-] md5.my-addr.com MD5值：" + md5 + " 未查到解密值\n")


def gromweb(md5):
    url = "https://md5.gromweb.com/?md5=" + md5
    request = requests.get(url, headers=headers)

    html = re.compile(r"<em class=\"long-content string\">(.*)</em>")

    htmlC = html.findall(request.text)

    if htmlC:
        print(Fore.GREEN + " [+] md5.gromweb.com MD5值：" + md5 + " 已查到解密值：" + htmlC[0] + "\n")
    else:
        print(Fore.RED + " [-] md5.gromweb.com MD5值：" + md5 + " 未查到解密值\n")


def nitrxgen(md5):
    url = "http://www.nitrxgen.net/md5db/" + md5

    request = requests.get(url, headers=headers)

    md5Value = request.text

    if md5Value != "":
        print(Fore.GREEN + " [+] www.nitrxgen.net MD5值：" + md5 + " 已查到解密值：" + md5Value + "\n")
    else:
        print(Fore.RED + " [-] www.nitrxgen.net MD5值：" + md5 + " 未查到解密值\n")


def tellyou(md5):
    url = "http://md5.tellyou.top/MD5Service.asmx/HelloMd5"

    data = "Ciphertext=" + md5

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "X-Forwarded-For": "192.168.1.1"
    }

    request = requests.post(url, data=data, headers=headers)

    html = re.compile(r"<string xmlns=\"http://tempuri.org/\">(.*)</string>")

    htmlC = html.findall(request.text)

    if htmlC:
        print(Fore.GREEN + " [+] md5.tellyou.top MD5值：" + md5 + " 已查到解密值：" + htmlC[0] + "\n")
    else:
        print(Fore.RED + " [-] md5.tellyou.top MD5值：" + md5 + " 未查到解密值\n")


def main(md5):
    for i in range(0, len(module)):
        func = module[i]
        thead = "t" + str(i)
        try:
            thead = threading.Thread(target=eval(func), args=(md5,))
            thead.setDaemon(True)
            thead.daemon = True
            thead.start()
            thead.join()
        except:
            print(Fore.RED + " [-] 很抱歉，出错了。可能操作过于频繁。\n")


if __name__ == "__main__":
    md5 = input(" Please Input Encrypt MD5 Value: ")
    print("\n")
    main(md5)
