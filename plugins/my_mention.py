import MeCab
#from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
#from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

@listen_to(r'^!mecab\s+\S.*')
def listen_func(message):
    text = message.body['text'] # メッセージを取り出す

    l = text.split()
    l.pop(0) # 先頭は `!mecab` なので除外
    content = l.pop() # 末尾は解析対象の文字列として扱う
    print(content)

    option = ' '.join(l)
    mecab = MeCab.Tagger(option)
    m = "```" + mecab.parse(content) + "```"
    print(m)

    message.send(m)
