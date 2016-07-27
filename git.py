import os, shutil

log_folder_path = os.path.dirname(os.path.realpath(__file__)) + "\git_logs"
log_file_path = log_folder_path + "\git_log_" + "%s.txt"


def save_commit_logs(path_list: list, author: str, callback) -> list:
    if os.path.exists("git_logs"):
        shutil.rmtree("git_logs")
    os.mkdir("git_logs")
    # for path in paths:
    #     cmd = "cd " + path + " & git fetch "
    #     os.system(cmd)
    for value, path in enumerate(path_list):
        cmd = "cd " + path + \
              "& git log --author=\"" + author + "\" --since=\"24hours\" --all > " + log_file_path % str(value + 1)
        cmd_result = os.popen(cmd).readlines()
        print("CMD result%s" % cmd_result)
    if callback is not None:
        return callback()


def read_commit_logs() -> list:
    commit_logs = []
    for filename in os.listdir(log_folder_path):
        file = open(log_folder_path + '\\' + filename)
        lines = file.readlines()
        for line in lines:
            if filter_log(line) is False:
                continue
            elif line.startswith(" "):
                if line.endswith("\n"):
                    line = line[4:-1]
                commit_logs.append(line)
    return commit_logs


def filter_log(log_string) -> bool:
    if 'commit' in log_string and 'Author' in log_string and 'Date' in log_string:
        return False
    if 'Merge remote-tracking branch' in log_string:
        return False
    return True


def get_commit_logs(project_paths: list, author: str) -> list:
    git_logs = save_commit_logs(project_paths, author, read_commit_logs)
    return git_logs


if __name__ == '__main__':
    paths = [os.path.dirname(os.path.realpath(__file__))]
    result = get_commit_logs(paths, 'imflyn')
    print(result)
