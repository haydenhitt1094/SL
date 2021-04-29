import subprocess

## Get run command
getDrives = subprocess.run('lsblk',capture_output=True)


## Parse returns

pre_parsed_drives = getDrives.stdout


print(pre_parsed_drives)