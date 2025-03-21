import sys
import os
import subprocess
import shlex

def main():
    while True:
        command_dict = {}
        sys.stdout.write("$ ")

        command = input()
        split_command = shlex.split(command)
        command_list = ['echo', 'exit', 'type', 'pwd', 'cd']

        if command == 'exit 0':
            break

        elif split_command[0] not in command_list:
            path = os.environ['PATH'].split(":")
            for p in path:
                binary_path = os.path.join(p, split_command[0])
                if os.path.exists(binary_path):
                    try:
                        subprocess.run([split_command[0]] + split_command[1:], executable=binary_path, check=True)
                    except subprocess.CalledProcessError as e:
                        sys.stdout.write(f"Command '{command}' failed with error: {e}\n")
                    break
            else:
                sys.stdout.write(f"{split_command[0]}: not found\n")

        elif split_command[0] == "pwd":
            sys.stdout.write(f"{os.getcwd()}\n")

        elif split_command[0] == "cd":
            if len(split_command) > 1:
                if split_command[1] == "~":
                    os.chdir(os.path.expanduser("~"))
                else:
                    try:
                        os.chdir(split_command[1])
                    except FileNotFoundError:
                        sys.stdout.write(f"{split_command[1]}: No such file or directory\n")
            else:
                sys.stdout.write("cd: Missing argument\n")

        elif split_command[0] == 'echo':
            
            echo_command = " ".join(split_command[1:])
            sys.stdout.write(f"{echo_command}\n")

        elif split_command[0] == 'type':
            env = os.environ
            if split_command[1] in command_list:
                sys.stdout.write(f"{split_command[1]} is a shell builtin\n")
            else:
                path = env['PATH'].split(":")
                for p in path:
                    binary_path = os.path.join(p, split_command[1])
                    if os.path.exists(binary_path):
                        sys.stdout.write(f"{split_command[1]} is {binary_path}\n")
                        break
                else:
                    sys.stdout.write(f"{split_command[1]}: not found\n")

        else:
            sys.stdout.write(f"{command}: command not found\n")

if __name__ == "__main__":
    main()
