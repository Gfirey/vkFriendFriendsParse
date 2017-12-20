# vkFriendFriendsParse
Cкачивание из VK друзей и построение таблицы связей между ними

Для начала требуется установить библиотеку [vk_api](https://github.com/python273/vk_api): `pip install vk_api`


Для запуска скрипта: `python vk.py <LOGIN> <PASSWORD> <ID>`
  где `LOGIN` и `PASSWORD` - логин и пароль пользователя vk, `ID` - id человека чьи друзья будут анализироваться

API методы vk можно найти вот тут: [vk.com/dev/methods](https://vk.com/dev/methods)

На выходе получим 2 csv файла.
vkek.csv - таблица связей между друзьями
vkek_sex.csv - таблица всех друзей и их пола
