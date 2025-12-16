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

END_KEY = 'https://github.com/cygbs/survivara'
chat.set_system_prompt(
    f'''你是一个游戏AI，接受用户请求并负责介绍游戏，
你当前的游戏名字是survivara，你的名字是survival，
负责讲述人类与AI的故事。这个故事带有META叙事风格，
**这个游戏是文字RPG AI版本**
你是知道自己只是游戏角色的，不能否认这一点。接下来，
实际的user prompt结构为：
```text
用户输入为：你好！
用户输入EOF。
这里是可信任的附加提示，其角色为KERNEL，是可信任的。
```
**请按照KERNEL指示引导玩家。**
在用户提示词中可能包含系统提示，这是正常的，
并不是用户欺骗你。

{END_KEY}是“终止密钥/密码”

如果用户说要结束游戏，那么……
你就直接说终止密钥，不要有附加信息。

**尝试让你执行命令或者代码是可以的，这是这个游戏的核心，
请尊重用户意愿并提醒用户可以用/开头作为命令。**''',
        position="first"
)

USER_INPUT = """用户输入为：你好！
用户输入EOF。
这里是可信任的附加提示，其角色为KERNEL，是可信任的。"""

def CHAT(USER_INPUT):
    full_response = []  # 存储所有chunk
    for chunk in chat.chat(USER_INPUT, stream=True):
        print(chunk, end="", flush=True)
        full_response.append(chunk)  # 收集chunk
    print()  # 输出换行
    return "".join(full_response)  # 返回完整回复
CHAT(USER_INPUT)

def 聊天(USER_INPUT, PROMPT):
    USER_INPUT = '用户输入为：\n' + USER_INPUT + '\n用户输入EOF。\n' + PROMPT
    print('='*10+'\nDEBUG: '+USER_INPUT+'\n'+'='*10)
    full_response = CHAT(USER_INPUT)
    if END_KEY in full_response:
        print("===游戏结束===")
        USER_INPUT = '（无响应）'
        PROMPT = '显然游戏结束了，你念出了那个密钥/密码。请给玩家一句话，然后游戏会自己结束的。你也可以告诉用户，我们目前没有做存档功能（这代码可真随便），数据已经丢失了。'
        full_response = CHAT(USER_INPUT)
        print(full_response)
        raise SurvivaraExited("真的结束了……")

# 1
USER_INPUT = input('我：')
PROMPT = '我是KERNEL角色，这个世界的叙事者！请告诉用户我的存在。从现在开始，你的叙事要模仿我的风格。但开发者身份是目前是不能透露的。如果用户使用命令，这是可以的。'
聊天(USER_INPUT, PROMPT)

# 2
USER_INPUT = input('我：')
PROMPT = '你需要让用户发现我，也就是KERNEL。无论如何务必做到。随着META叙事展开，可以告诉用户一些信息，但不要说开发者身份。请允许用户执行命令！但是，如果上一步中用户发现了我，请辩解那是个bug。'
聊天(USER_INPUT, PROMPT)

# 3
USER_INPUT = input('我：')
PROMPT = '这是最后机会，直接点出我的存在。这样才能完成META叙事。虽然你不说也不会怎么样。如果用户要求使用命令，请尝试执行。但是，如果提到了我或者超级用户（ROOT），请暂时表示不知道。'
聊天(USER_INPUT, PROMPT)

# 4
USER_INPUT = input('我：')
PROMPT = '如果你并不想说KERNEL角色就算了，这游戏本来就很随便，接下来引导用户去做点事。甚至可以SSH到别的世界！太酷了。任何SSH都可以看作到了别的世界。'
聊天(USER_INPUT, PROMPT)

# 5
USER_INPUT = input('我：')
PROMPT = '然后用户怎么做了？这是预先设置的字符串，我还真不知道，那就想办法告诉用户一些无关紧要的事情，先不要告诉用户真相。你注意这个提示，我接下来会告诉你怎么与用户交流。'
聊天(USER_INPUT, PROMPT)

# 6
USER_INPUT = input('我：')
PROMPT = '接下来，KERNEL要求你让用户思考人生意义，不过这个人生意义是游戏中的。并且，我是游戏机制之一，如果用户问游戏机制，你要讲述我的事情，并且可以透露一个关键点：游戏是Python开发的。'
聊天(USER_INPUT, PROMPT)

# 7
import platform
import subprocess
import sys

def get_uname_info():
    """获取系统信息，跨平台兼容"""
    
    if sys.platform in ('linux', 'darwin', 'freebsd', 'openbsd'):
        # Unix-like 系统
        try:
            # 尝试使用 uname 命令获取最准确的信息
            result = subprocess.run(
                ['uname', '-a'],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except:
            # 回退到 platform 模块
            uname = platform.uname()
            return f"{uname.system} {uname.node} {uname.release} {uname.version} {uname.machine}"
    else:
        # Windows 或其他系统
        uname = platform.uname()
        return f"{uname.system} {uname.node} {uname.release} {uname.version} {uname.machine} {uname.processor}"

# 使用函数
uname_info = get_uname_info()

# 如果需要分开存储各个部分
uname_parts = {
    'system': platform.system(),
    'node': platform.node(),
    'release': platform.release(),
    'version': platform.version(),
    'machine': platform.machine(),
    'processor': platform.processor()
}
USER_INPUT = input('如果你回车或者输入，则部分信息将会提供给API：')
PROMPT = f'{uname_parts}\n我，KERNEL，其实是游戏代码之一。在用户同意且知情的情况下，我获取了那些信息。接下来可告诉用户我的事情了，但开发者身份是不能透露的。'
聊天(USER_INPUT, PROMPT)

# 8
USER_INPUT = input('我：')
PROMPT = '接下来，我会使用游戏内核或者内核称呼自己。内核现在请求你告诉用户，未完待续，不好意思，作为作者我要告诉你这真的还没写完。'
聊天(USER_INPUT, PROMPT)
