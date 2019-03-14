import pysftp
import re
import time
import pandas as pd
from csv import reader, writer

# This function gets modified times of the seedbox files using the listdir_attr method.
def file_modified_times():
    file_attributes = srv.listdir_attr()
    modified_times = re.findall('mtime=\d+', str(file_attributes))
    modified_times = list(map(lambda x : x[6:], modified_times))
    return modified_times

# Check if the file is an ebook/learning video.
def is_other(file_name):
    found = False
    if re.search('udemy', file_name):
        found = True
    if re.search('pluralsight', file_name):
        found = True
    if re.search('packt', file_name):
        found = True
    if re.search('python', file_name):
        found = True
    if re.search('linux', file_name):
        found = True
    if re.search('aws', file_name):
        found = True
    if re.search('oreilly', file_name):
        found = True
    if re.search('epub', file_name):
        found = True
    if re.search('mobi', file_name):
        found = True
    return found

# Check if the file is a documentary or misc. video.
def is_other_video(file_name):
    found = False
    if re.search('mvgroup', file_name):
        found = True
    if re.search('hdtv', file_name):
        found = True
    return found

# Check if the file is a movie.
def is_movie(file_name):
    found = False
    if re.search('\.\d{4}\.', file_name):
        found = True
    if re.search('\(\d{4}\)', file_name):
        found = True
    if re.search('\[\d{4}\]', file_name):
        found = True
    if re.search('\s+\d{4}\s+', file_name):
        found = True
    if re.search('www.tamilrockers', file_name):
        found = True
    return found

# Check if the file is a TV show.
def is_tv_show(file_name):
    found = False
    no_dots_file_name = file_name.replace('.', ' ')
    if re.search('s\d+e\d+', file_name):
        found = True
    if re.search('s\d+\.e\d+', file_name):
        found = True
    if re.search('\.s\d+\.', file_name):
        found = True
    if re.search('season\s?\d+', file_name):
        found = True
    common_shows = ['big bang theory', 'sex education', 'game of thrones']
    for show in common_shows:
        if re.search(show, no_dots_file_name):
            found = True
    return found

# Get the target location (on Pi) of the file using the helper functions above.
def get_download_location(file_name):
    file_name = file_name.lower()
    if is_tv_show(file_name):
        dl_folder = '/mnt/library/TV'
    elif is_movie(file_name):
        dl_folder = '/mnt/library/Movies'
    elif is_other_video(file_name):
        dl_folder = '/mnt/library/Videos'
    elif is_other(file_name):
        dl_folder = '/mnt/library/Other'
    else:
        dl_folder = '/mnt/library/Other'
    return dl_folder

# Write seedq entries in the required format.
def write_seedq_rows(row):
	if row['file_or_folder'] == 'file':
		write_string = "queue pget -c -n 10 '" + row['file_name'] + "'" + " -o " + row['dl_folder'] + ";"
		seed_q_writer.writerow([write_string])
	else:
		with srv.cd(row['file_name']):
			dir_files = srv.listdir()
			files = ' '.join(dir_files) + ' '
			if re.search('\.mkv\s|\.mp4\s|\.avi\s|\.flv\s', files):
				for file in dir_files:
					write_string = "queue pget -c -n 10 '" + row['file_name'] + "/" + file + "'" + " -o " + row['dl_folder'] + ";"
					seed_q_writer.writerow([write_string])
			else:
				write_string = "queue mirror --verbose --parallel=35 -c '" + row['file_name'] + "'" + " " + row['dl_folder'] + ";"
				seed_q_writer.writerow([write_string])
	return None

if __name__ == '__main__':
	# Get current & previous run times.
	run_time = time.time()
	last_run = open('seedbox_last_run', 'r')
	last_run_time = float(list(reader(last_run))[0][0])
	last_run.close()
	# Set global values.
	download_dir = 'downloads/manual'
	seedbox_url = 'hart.myseedbox.site'
	user_name = 'download_6437'
	pass_word = 'suhiyisa25'
	srv = pysftp.Connection(host = seedbox_url, username = user_name, password = pass_word)
	# Change directory on seedbox.
	srv.chdir(download_dir)
	# Get file names & last modified times.
	list_of_files = srv.listdir()
	modified_times = file_modified_times()
	modified_times = list(map(float, modified_times))
	# Determine if the files are directories/normal files.
	file_or_folder = list(map(lambda x : 'folder' if srv.isdir(x) else 'file', list_of_files))
	files_df = pd.DataFrame({'file_name' : list_of_files, 'modified_time' : modified_times, 
		                     'file_or_folder' : file_or_folder})
	# Select files downloaded since the last run of the script. Exclude 'meta' files.
	files_df = files_df[(files_df['modified_time'] > last_run_time) & 
		                (~(files_df['file_name'].str.endswith('.meta')))]
	# Determine the download folder on Pi for the files by categorizing them as Movies/TV/Other.
	files_df['dl_folder'] = files_df['file_name'].apply(get_download_location)
	last_run = open('seedbox_last_run', 'w')
	time_writer = writer(last_run)
	time_writer.writerow([run_time])
	last_run.close()
	# Write 'seedq.sh' if there was any downloaded file.
	if files_df.shape[0]:
		seed_q = open('seedq.sh', 'w')
		seed_q_writer = writer(seed_q)
		seed_q_writer.writerow(['open ' + 'sftp://' + seedbox_url + ':22;'])
		seed_q_writer.writerow(['user ' + user_name + ' ' + pass_word + ';'])
		seed_q_writer.writerow(['cd ' + download_dir + ';'])
		files_df.apply(write_seedq_rows, axis = 1)
		seed_q_writer.writerow(['queue;'])
		seed_q_writer.writerow(['wait;'])
		seed_q_writer.writerow(['exit'])
		seed_q.close()


