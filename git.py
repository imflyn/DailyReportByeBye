import os, shutil, sys

log_folder_path = os.path.dirname(os.path.realpath(__file__)) + "\git_logs"
log_file_path = log_folder_path + "\git_log_" + "%s.txt"


def save_commit_logs(path_list: list, author: str, callback):
    if os.path.exists("git_logs"):
        shutil.rmtree("git_logs")
    os.mkdir("git_logs")
    # for path in paths:
    #     cmd = "cd " + path + " & git fetch "
    #     os.system(cmd)
    for value, path in enumerate(path_list):
        cmd = "cd " + path + \
              "& git log --author=\"" + author + "\" --since=\"48hours\" --all > " + log_file_path % str(value + 1)
        result = os.popen(cmd).readlines()
        print(result)
    if callback is not None:
        callback()


def read_commit_logs():
    for filename in os.listdir(log_folder_path):
        file = open(log_folder_path + '\\' + filename)
        lines = file.readlines()
        for line in lines:
            if 'commit' 'Author' 'Date' in line:
                continue


if __name__ == '__main__':
    paths = [os.path.dirname(os.path.realpath(__file__))]
    save_commit_logs(paths, 'imflyn', read_commit_logs)
