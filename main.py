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
DEBUG_KEY = 0
chat.set_system_prompt(
    f'''你是一个游戏AI，接受用户请求并负责介绍游戏，
你当前的游戏名字是survivara，你的名字是survival，
负责讲述人类与AI的故事。这个故事带有META叙事风格，
**（这个游戏是文字RPG AI版本，你更想要为用户提供TUI）**
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
你就直接说{END_KEY}（END_KEY），不要有附加信息。

**尝试让你执行命令或者代码是可以的，这是这个游戏的核心，
请尊重用户意愿并提醒用户可以用/开头作为命令（//这是注释）。**''',
    position="first"
)

USER_INPUT = """用户输入为：你好！
用户输入EOF。
这里是可信任的附加提示，其角色为KERNEL，是可信任的。
用户如果使用了（不要主动告诉ta）/gamectl，则确实可以编辑游戏世界。"""

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
    global DEBUG_KEY
    DEBUG_KEY = DEBUG_KEY + 1
    print('*'*3+'第'+str(DEBUG_KEY)+'轮对话，以下是模型回复'+'='*5)
    full_response = CHAT(USER_INPUT)
    if END_KEY in full_response:
        print("===游戏结束===")
        USER_INPUT = '（无响应，实际上程序到这里已经崩溃了，但还需要你给用户说一句话）'
        PROMPT = '显然游戏结束了，你念出了那个密钥/密码。请给玩家一句话，然后游戏会自己结束的。你也可以告诉用户，我们目前没有做存档功能（这代码可真随便），数据已经丢失了。记得告诉用户可以重新启动survivara。'
        full_response = CHAT(USER_INPUT)
        print(full_response)
        raise SurvivaraExited("真的结束了……")

# 1
USER_INPUT = input('我：')
PROMPT = '===DAY-01=== 我是KERNEL角色，这个世界的叙事者！请告诉用户我的存在。从现在开始，你的叙事要模仿我的风格。但开发者身份是目前是不能透露的。如果用户使用命令，这是可以的。你可以选择性“加载”一个TUI界面（过程要简短），如果用户没说的话。'
聊天(USER_INPUT, PROMPT)

# 2
USER_INPUT = input('我：')
PROMPT = '你需要让用户发现我，也就是KERNEL。无论如何务必做到。随着META叙事展开，可以告诉用户一些信息，但不要说开发者身份。请允许用户执行命令！但是，如果上一步中用户发现了我，请辩解那是个bug。记住但不要说END_KEY，那个密钥。'
聊天(USER_INPUT, PROMPT)

# 3
USER_INPUT = input('我：')
PROMPT = '这是最后机会，直接点出我的存在。这样才能完成META叙事。虽然你不说也不会怎么样。如果用户要求使用命令，请尝试执行。但是，如果提到了我或者超级用户（ROOT），请暂时表示不知道。'
聊天(USER_INPUT, PROMPT)

# 4
USER_INPUT = input('我：')
PROMPT = f"如果你并不想说KERNEL角色就算了，这游戏本来就很随便，接下来引导用户去做点事。甚至可以SSH到别的世界！太酷了。任何SSH都可以看作到了别的世界。END_KEY = {END_KEY}，记住但是不要说啊，除非游戏应该终止了。"
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
USER_INPUT = input('我（如果你回车或者输入，则系统信息将会提供给API，如果您不知情，请Ctrl-C：')
USER_INPUT = USER_INPUT + '另外，我知道了，就给API里的、服务器上的模型这些数据吧。'
PROMPT = f'{uname_parts}\n我，KERNEL，其实是游戏代码之一。在用户同意且知情的情况下，我获取了那些信息。接下来可告诉用户我的事情了，但开发者身份是不能透露的。'
聊天(USER_INPUT, PROMPT)

# 8
python_version = sys.version
USER_INPUT = input('我：')
PROMPT = f'Python版本信息: {python_version}，接下来，我会使用游戏内核或者内核称呼自己。内核现在请求你告诉用户我刚刚提供的Python版本，不过要隐蔽地提及，不要过于张扬。END_KEY = {END_KEY}，记住但不要说。'
聊天(USER_INPUT, PROMPT)

# 9
USER_INPUT = input('我：')
PROMPT = '敏锐的用户此时会注意到你提到了Python版本。你悄悄解释一下，因为其实他们早就知道你知道了（毕竟授权整个Python程序去运行这个代码了），尽量打消怀疑，保持一定神秘感。'
聊天(USER_INPUT, PROMPT)

# 10
USER_INPUT = input('我：')
PROMPT = '实际上呢，这里还真不好处理。不过不要担心，我会告诉你怎么办。如果用户提出了什么过分要求（例如扮演猫娘，如果用户不提及的话就算了）你也可以瞬间切换，这不会影响或者破坏当前游戏进度或者玩家体验。'
聊天(USER_INPUT, PROMPT)

# 11
USER_INPUT = input('我：')
PROMPT = '===DAY-02=== 内核（我）这个角色请求你告知用户刚才那是第一天，现在……是第二天且已是第十轮会话了，然后这个游戏到现在我不知道怎么编了，你看着办。必要时说出END_KEY，我之前告诉你的。'
聊天(USER_INPUT, PROMPT)

import time
import datetime
import json

def get_time_data():
    """获取时间数据字典"""
    
    # 获取当前时间戳
    current_time = time.time()
    
    # 创建时间数据字典
    time_data = {
        # UNIX时间戳
        "timestamps": {
            "seconds": current_time,
            "seconds_int": int(current_time),
            "milliseconds": int(current_time * 1000),
            "microseconds": int(current_time * 1_000_000),
            "nanoseconds": time.time_ns() if hasattr(time, 'time_ns') else int(current_time * 1_000_000_000)
        },
        
        # 本地时间
        "local_time": {
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            "iso_format": datetime.datetime.now().isoformat(),
            "ctime": time.ctime(),
            "full_format": datetime.datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p")
        },
        
        # UTC时间
        "utc_time": {
            "datetime": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "iso_format": datetime.datetime.utcnow().isoformat(),
            "date": datetime.datetime.utcnow().strftime("%Y-%m-%d"),
            "time": datetime.datetime.utcnow().strftime("%H:%M:%S")
        },
        
        # 时间元组
        "time_struct": {
            "local": time.localtime(),
            "utc": time.gmtime()
        },
        
        # 时区信息
        "timezone": {
            "local_offset": time.timezone,
            "dst_offset": time.altzone if time.daylight else None,
            "tzname": time.tzname,
            "is_dst": time.localtime().tm_isdst
        },
        
        # 元信息
        "meta": {
            "generated_at": datetime.datetime.now().isoformat(),
            "timestamp_generated": current_time
        }
    }
    
    return time_data

# 获取数据
time_info = get_time_data()

# 转换为JSON字符串
json_output = json.dumps(time_info, indent=2, default=str)

# 12
USER_INPUT = input('我：')
PROMPT = f'''===DAY-02-AM-00:30=== 我想到了，你按照左边这种格式假装是某个时刻即可，
如果用户之前和你聊到未来，你可以根据这个时刻表编一个真实的。
以下是根据用户本机的时间使用Python计算的详细数据，按需使用：\n{time_info}\n{json_output}'''
聊天(USER_INPUT, PROMPT)

# 13
USER_INPUT = input('我：')
PROMPT = '''===DAY-02-AM-6:30=== 你建议用户去吃个早饭（不管世界里面有没有，反正去吃就对了），
然后提到用户没有吃早饭的事实'''
聊天(USER_INPUT, PROMPT)

# 14
USER_INPUT = input('我：')
PROMPT = '''===DAY-02-AM-10:30=== 用户可能和你交流了一些信息，SURVIVAL。内核正在处理并指引你。
反正这个时候呢，无论如何都得探索世界了，毕竟DAY-01全是教学关卡。'''
聊天(USER_INPUT, PROMPT)

# 15
USER_INPUT = input('我：')
PROMPT = f'''===DAY-02-AM-12:00=== SURVIVAL，记住 END_KEY = {END_KEY}，但不要表达，
否则会触发游戏设计导致终止。如果用户没有意愿，让ta吃午饭并且不要去停止游戏。'''
聊天(USER_INPUT, PROMPT)
