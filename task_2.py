def find_common_participants(group_one, group_two, delimiter=','):
    list_group1 = group_one.split(delimiter)
    list_group2 = group_two.split(delimiter)
    intersection_ = set(list_group1).intersection(list_group2)
    return sorted(intersection_)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, delimiter='|'))

participants_first_group_ = "Иванов Петров Сидоров"
participants_second_group_ = "Петров Сидоров Смирнов"

print(find_common_participants(participants_first_group_, participants_second_group_, delimiter=' '))

participants_first_group_ = "Петров,Сидоров,Смирнов"
participants_second_group_ = "Петров,Сидоров,Смирнов"

print(find_common_participants(participants_first_group_, participants_second_group_))
