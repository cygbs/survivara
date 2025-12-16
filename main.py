def main():
    print("Hello from survivara!")
    回答 = input("准备好开始了吗？请回答我：")
    print("好，我知道了，虽然你刚刚好像是随便说的，但是让我们继续吧！")
    import time
    time.sleep(1)
    from lib.setup import API_URL, API_KEY
    print(f"地址：{API_URL}")
    print(f"密钥：{API_KEY}")
    print(f"好的，我已看到了，让我们继续。")

print("""  ___ _   _ _ ____   _(_)_   ____ _ _ __ __ _ 
 / __| | | | '__\\ \\ / / \\ \\ / / _\` | '__/ _\`|
 \\__ \\ |_| | |   \\ V /| |\\ V / (_| | | | (_| |
 |___/\\__,_|_|    \\_/ |_| \\_/ \\__,_|_|  \\__,_|""")

if __name__ == "__main__":
    main()
