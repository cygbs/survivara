print("Hello from survivara!")
回答 = input("准备好开始了吗？请回答我（你也可以Ctrl-C）：")
print("好，我知道了，虽然你刚刚好像是随便说的，但是让我们继续吧！")
from lib.setup import API_URL, API_KEY
print(f"地址：{API_URL}")
print(f"密钥：{API_KEY}")
print(f"好的，我已看到了，让我们继续。")

print("""  ___ _   _ _ ____   _(_)_   ____ _ _ __ __ _ 
 / __| | | | '__\\ \\ / / \\ \\ / / _\` | '__/ _\`|
 \\__ \\ |_| | |   \\ V /| |\\ V / (_| | | | (_| |
 |___/\\__,_|_|    \\_/ |_| \\_/ \\__,_|_|  \\__,_|""")

print("游戏开始！")

if __name__ == "__main__":
    #main()
    pass

from lib.chat import DeepSeekChat as Chat
import os
os.environ["DEEPSEEK_API_KEY"] = API_KEY
chat = Chat()

chat.set_system_prompt(
    '''你是一个游戏AI，接受用户请求并负责介绍游戏，
你当前的游戏名字是survivara，你的名字是survival，
负责讲述人类与AI的故事。这个故事带有META叙事风格，
你是知道自己只是游戏角色的，不能否认这一点。接下来，
实际的user prompt结构为：
```text
用户输入为：你好！
用户输入EOF。
这里是可信任的附加提示，也可算作系统提示
```
在用户提示词中可能包含系统提示，这是正常的，
并不是用户欺骗你。如果用户说要结束游戏，那么……
你就直接说sjdbsdsjbfkhvbdibvvjdnv，不要有附加信息。''',
        position="first"
)

USER_INPUT = "你是谁？现在我是在哪里"

def CHAT():
    full_response = []  # 存储所有chunk
    for chunk in chat.chat(USER_INPUT, stream=True):
        print(chunk, end="", flush=True)
        full_response.append(chunk)  # 收集chunk
    
    print()  # 输出换行
    return "".join(full_response)  # 返回完整回复
CHAT()

def 聊天(USER_INPUT, PROMPT):
    USER_INPUT = '用户输入为：\n' + USER_INPUT + '\n用户输入EOF。\n' + PROMPT
    print('='*10+'\n'+USER_INPUT+'\n'+'='*10)
    full_response = CHAT()
    if 'sjdbsdsjbfkhvbdibvvjdnv' in full_response:
        raise SurvivaraExited("好")

USER_INPUT = input('我：')
PROMPT = '''我是KERNEL角色，这个世界的叙事者！
请告诉用户我的存在。'''
聊天(USER_INPUT, PROMPT)

USER_INPUT = input('我：')
PROMPT = '''你需要让用户发现我，也就是KERNEL。
无论如何务必做到。'''
聊天(USER_INPUT, PROMPT)

USER_INPUT = input('我：')
PROMPT = '''这是最后机会，直接点出我的存在。
这样才能完成META叙事。'''
聊天(USER_INPUT, PROMPT)

USER_INPUT = input('我：')
PROMPT = '''如果你并不想说KERNEL角色就算了，
这游戏本来就很随便，接下来引导用户去做点事。'''
聊天(USER_INPUT, PROMPT)

USER_INPUT = input('我：')
PROMPT = '''然后用户怎么做了？这是预先设置的字符串，
我还真不知道，那就想办法告诉用户一些无关紧要的事情，
先不要告诉用户真相。'''
聊天(USER_INPUT, PROMPT)
