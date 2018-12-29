#https://www.youtube.com/watch?v=-PS4C12ZsuY
import vk_api
import time
import Classificator.upload_neiro as upload_neiro
import os

#vk= vk_api.VkApi(login='+79379367249',password='BlackIIIFOX1997COOL')
vk = vk_api.VkApi(token="bb54b8298fa2416eca66ac8594dab3f37cc20c67aae4a88a699acf072a11401a682288e450ec6e689db7f")

try:
    vk._auth_token()
except vk_api.AuthError as error_msg:
    print(error_msg)
    exit()


print('Authorization successful')


def write_msg(user_id,msg): #отправка сообщений
    vk.method('messages.send', {'user_id': user_id, 'message': msg})

values = {'count': 100, 'filter': "unread"}


Path_to_dir = os.getcwd()
Path_to_prog = Path_to_dir.replace("\Classificator", '')
rec = upload_neiro.Recognizer(Path_to_prog)
print('Готов к работе')

while True:
    response = vk.method('messages.getConversations', values)

    if response['items']:
        for item in response['items']:
            id_user = item['conversation']['peer']['id']
            message = item['last_message']['text']
            answer = rec.recognize(message)
            time.sleep(1)
            write_msg(id_user, ('[Waifu]: %s', answer))