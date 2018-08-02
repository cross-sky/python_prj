import os

#get file
rootdir = 'E:\da'
def get_files(rootdir):
	files = os.listdir(rootdir)
	for i in range(0, len(files)):
		file_path = os.path.join(rootdir, files[i])
		if os.path.isfile(file_path):
			print(file_path)
			replace_file(file_path)

def replace_file(file_path):
	with open(file_path, 'r', encoding='utf-8') as f1, open('%s.bak' % file_path, 'w', encoding='utf-8') as f2:
		while True:
			strs = f1.readline()
			if not strs:
				break
			strs = replace_line(strs)
			f2.write(strs+ '\n')
	os.remove(file_path)
	os.rename('%s.bak' % file_path, file_path)

def replace_line(strs):
	strs = strs.strip('\n')
	s_split = strs.split('//', 1)
	if len(s_split) == 1:
		return s_split[0]
	else:
		return s_split[0] + '/**' + s_split[1] + '**/'



if __name__ == '__main__':
	get_files(rootdir)