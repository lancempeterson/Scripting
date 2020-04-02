import shutil
import glob
import time
import os

print("File Mover 1.0 - Lance M. Peterson")

src = "C:/Users/Lance.Peterson/Desktop/Scripting/Folder1"
dst = "C:/Users/Lance.Peterson/Desktop/Scripting/Folder2"

EXTENSIONS = ('txt')

# Copy all files folders 
#shutil.copytree(src=src, dst=dst)

# Copy specific file
#shutil.copy(src=src + "/myLog.txt", dst=dst)

# Copy all files of specific extension
#for file in glob.glob('*.txt'):
#	print("Copying "+file+" --> "+ dst)
#	shutil.copy(src=src + "/"+file, dst=dst)
#	time.sleep( 1 )
	
# Copy all files of specific extension in root and all subdirectories
for root, dirs, files in os.walk(src):
	for file in files:
		if file.endswith('.txt'):
			print(os.path.join(root, file))
			shutil.copy(os.path.join(root, file), dst=dst)

	
input("Press Enter to continue...")