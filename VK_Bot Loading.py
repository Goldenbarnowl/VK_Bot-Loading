import vk_api
import time


token = input("Введите токен с доступом к сообщениям>> ")
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
print("Токен введен успешно, для запуска бота напишите /load в любой переписке!")
user_id = vk.users.get()
user_id = user_id[0]
user_id = user_id["id"]

def editor(peer_id, message, message_id):
    vk.messages.edit(peer_id = peer_id, message = message, message_id = message_id)
    print("Сообщение успешно изменено.")

def delet(message_ids, peer_id):
    vk.messages.delete(message_ids = message_ids, delete_for_all = 1, peer_id = peer_id)
    print("Сообщение успешно удалено.")

while(True):
    massive_message_info = vk.messages.search(q="/load",count = 1)
    massive_message_info = massive_message_info["items"]
    massive_message_info = massive_message_info[0]

    if (massive_message_info["text"] == "/load") and (massive_message_info["from_id"] == user_id):

        text = "Loading..."
        proc = 0
        load = ["▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒", "▒▒"]

        for y in range(10):
            loadtext = ""
            for x in range(10):
                loadtext += load[x]
            enter = text + str(proc) + "%\n" + loadtext
            proc += 10
            editor(massive_message_info["peer_id"], enter, massive_message_info["id"])
            time.sleep(1)
            load[y] = "██"

        delet(massive_message_info["id"],massive_message_info["peer_id"])