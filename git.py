import os, shutil


def save_commit_logs(paths: list, author: str):
    if os.path.exists("git_logs"):
        shutil.rmtree("git_logs")
    os.mkdir("git_logs")
    # for path in paths:
    #     cmd = "cd " + path + " & git fetch "
    #     os.system(cmd)
    script_path = os.path.dirname(os.path.realpath(__file__))
    for value, path in enumerate(paths):
        cmd = "cd " + path + \
              "& git log --author=\"" + author + "\" --since=\"24hours\" --all > " + script_path + "\git_logs\git_log_" + str(value + 1) + ".txt"
        os.system(cmd)


if __name__ == '__main__':
    paths = []
    save_commit_logs(paths, 'flyn.yu')
