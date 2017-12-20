import vk_api
import csv
import sys


def main(_, login, password, id):
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    friends = vk.friends.get(user_id=id, fields='sex')

    friend_ids = [x['id'] for x in friends['items']]

    data = {x['id']: {'sex': x['sex']} for x in friends['items']}
    for friend in friend_ids:
        try:
            friend_data = vk.friends.get(user_id=friend)
            if 'deactivated' not in friend_data:
                data[friend]['friends'] = friend_data['items']
        except Exception:
            pass
    to_csv(parser(friend_ids, data), 'vkek')
    to_csv(parser_sex(friend_ids, data), 'vkek_sex')


def parser(friend_ids, data):
    matrix = [[] for i in range(len(friend_ids) + 1)]
    matrix[0].append('vkek')
    i = 1
    for x in friend_ids:
        matrix[0].append(x)
        row = matrix[i]
        col = matrix[0][i]
        row.append(x)
        i += 1
        for friend in friend_ids:
            relationship = ''
            if 'friends' in data[friend]:
                relationship = 1 if col in data[friend]['friends'] else 0
            row.append(relationship)
    return matrix


def parser_sex(friend_ids, data):
    result = [[] for i in range(len(friend_ids) + 1)]
    result[0].append('id')
    result[0].append('sex')
    i = 1
    for friend in friend_ids:
        result[i].append(friend)
        result[i].append(data[friend]['sex'])
        i += 1

    return result


def to_csv(formatted_data, file_name):
    myFile = open(file_name + '.csv', 'w')
    with myFile:
        writer = csv.writer(myFile, dialect='excel', lineterminator='\n')
        writer.writerows(formatted_data)


if __name__ == '__main__':
    main(*sys.argv)
