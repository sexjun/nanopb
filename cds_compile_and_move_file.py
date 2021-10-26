import os
from shutil import copyfile
import subprocess
import shlex

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("{} does not exist".format(filename))

def copy_file(src_path, dest_path):
    if(os.path.exists(dest_path)):
        del_file(dest_path)
    
    if(os.path.exists(src_path)):
        try:
            copyfile(src_path, dest_path)
        except IOError as e:
            print("Error copying")
            exit(1)
        except:
            print("unknown error")
            exit(-1)

def move_file(src_path, dest_path):
    copyfile(src_path, dest)
    os.remove(src_path)

def get_cmd_str(cmd):
    command = {
        "run": "python -V",
        "dir": "ls",
        "generate_pb": r"python ./generator/nanopb_generator.py ./cds_nanopb/cds_nanopb_info.proto"
    }
    try:
        cmd_str = command[cmd]
    except KeyError:
        print("Command {} not found".format(cmd))
        exit(1)
    return cmd_str

def run_cmd(cmd, is_nedd_output=False, run_in_shell=True, check_result=True):
    cmd_str = shlex.split(get_cmd_str(cmd))
    subprocess.Popen(cmd_str)

def main():
    run_cmd("generate_pb")
    base_dir = "./cds_nanopb"
    filename_c = "cds_nanopb_info.pb.c"
    filename_h = "cds_nanopb_info.pb.h"
    copy_file(os.path.join(base_dir, filename_c), filename_c)
    copy_file(os.path.join(base_dir, filename_h), filename_h)

if __name__ == '__main__':
    main()
    

