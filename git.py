import os, shutil
from time import sleep

log_folder_path = os.path.dirname(os.path.realpath(__file__)) + "\git_logs"
log_file_path = log_folder_path + "\git_log_" + "%s.txt"
project_path = os.path.dirname(os.path.realpath(__file__))


def save_commit_logs(path_list: list, author: str, callback) -> list:
	if os.path.exists(project_path + "\\git_logs"):
		shutil.rmtree(project_path + "\\git_logs")
	os.mkdir(project_path + "\\git_logs")
	# for path in paths:
	#     cmd = "cd " + path + " & git fetch "
	#     os.system(cmd)
	for value, path in enumerate(path_list):
		cmd = path[0:2] + " & cd " + path + \
		      " & git log --author=\"" + author + "\" --since=\"16hours\" --all > " + log_file_path % str(value + 1)
		print(cmd)
		os.popen(cmd)
	if callback is not None:
		sleep(5)
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
	paths = ['D:\\Development\\workspace_fandine\\fandine_new\\consumer-app-android',
	         'D:\\Development\\workspace_fandine\\fandine_new\\employee-app-android-v2']
	result = get_commit_logs(paths, 'flyn.yu')
	print(result)
