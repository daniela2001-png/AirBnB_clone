#!/usr/bin/python3
import sys

__import__('sys').path.append('.')


def main():
    import uuid
    from models import storage
    from models.review import Review

    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new User --")
    my_user = Review()
    my_user.text = "Betty"
    my_user.save()
    print(my_user)

    print("-- Create a new User 2 --")
    my_user2 = Review()
    my_user2.text = "daniela"
    my_user2
    my_user2.save()
    print(my_user2)


main()
