import requests
import time

def main():

    cookie = input("请输入cookie").strip()
    cookies = []
    while input().strip() != "y":
        cookie = input("请输入cookie").strip()
        cookies.append(cookie)
    times = int(input("请输入抽奖次数"))

    headers = {
        'Cookie':cookie,
        'Content-Type': 'application/json'
    }

    cnt = 0
    
    while cnt < times:
        time.sleep(1)
        cnt += 1
        response = requests.Session().post(
            "https://ccc.hi.163.com/ty-ty_xz_20250901_server/ccc-lottery/get/luck",
            headers=headers,
            timeout=30
        )
        print("第" + str(cnt) + "次请求, 请求结果:" + response.text)


if __name__ == "__main__":
    main()

