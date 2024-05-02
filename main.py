from termcolor import cprint
from function_runner import FunctionRunner


with open("SHA-3/user/input.md", "r") as file:
    user_message = file.readline()


while True:
    cprint("sha3_224 || sha3_256 || sha3_384 || sha3_512 || shake128 || shake256", "cyan" , None)
    user_function = input().lower()
    runner = FunctionRunner(user_function)

    if user_function in ("shake128", "shake256"):
        cprint("Введите параметр d:", "cyan", None)
        user_d = int(input())
        user_result = runner.run(user_message, user_d).upper()
        cprint(f"Полученный хеш - {user_result}", "green", None)
    else:
        user_result = runner.run(user_message).upper()
        cprint(f"Полученный хеш - {user_result}", "green", None)

    with open("SHA-3/user/output.md", "w") as file:
          file.write(f"{user_result} <!-- The result of the {user_function} function -->")
