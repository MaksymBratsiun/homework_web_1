from functions import commands_dict,commands_dict_ua, interface, users, hello, hello_ua
import addressbook
import console


the_end = False


def main():
    try:
        lang = input("Change language to Ukrainian? Enter 'Yes' to change")
        if lang.strip().lower() == 'yes':
            print(hello_ua())
            command = commands_dict_ua
        else:
            print(hello())
            command = commands_dict

        while not the_end:
            user_input = input(">>>: ").lower()
#           user_input = console.get_input("Enter please: ").lower()
            if user_input in ["good_bye", "close", "exit", "удачі", "вихід", "закрити"]:
                print(commands_dict.get("exit")())
                break
            else:
                print(interface.handler(command, user_input))
    finally:
        users.save_file()


if __name__ == '__main__':
    main()
