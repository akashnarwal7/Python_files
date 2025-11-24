import os

import stat



'''

Command : os.getced()


          . To Get Working Directory where your programm is running not where your programme is located.

          . current working directory means you have a pointer which points and only can see that directory.
          but there is no need that python script should exist in that working directory.

          . cwd means pyhton script or programme points to that folder.



          Any programme can run on any folder or location irrespective of its file or script location.

          so cwd is where your python programme is running not where your python programme is located.

          
'''
def currPath():
    print(" Current Working Directory : ",os.getcwd())


currPath()

'''
       command : os.chdir()

                . we can change the curr working directory any desired directory using os.chdir()
       

'''


currWd=os.chdir("../")

currPath()

currWd=os.chdir("D:\Python_revision_files")

currPath()
'''
       command : os.listdir()
       gives all files and folders list in present directory.
 
'''

print("All Directories List ", os.listdir())

currPath()



'''
 mkdir : creates a new directory with

 ./ means current working directory

 this means when using mkdir use cwd as parent directory.
 


os.mkdir("./NewDir",0o666)
print("Created a new Directory inside our cwd only.")


mkdirs

here to create a directory there are two things that exist

1. Directory
2. Parent Directory for that new Directory

parent / new directory

mkdir() will thro error if parent directory doesn't exist.

mkdirs() will also create parent directory if they doesn't exist. 


directory = "c"
parent_dir = "D:/Pycharm projects/GeeksforGeeks/a/b"
mode = 0o666
path = os.path.join(parent_dir, directory)
os.makedirs(path, mode)
print("Directory '% s' created" % directory)

'''

'''
   command: chmod


   There are three types of users

   1. owner

   2. group (other users )

   3. other than group and owners

   to change the permissions for a file or direcrory


   there are three types of permissions.

   1. Read(R)

   2. Write(w)

   3. Execute(x)


   we can use use numbers to give permissions for differnet users

   ex: owner read write read

       GRP read write

       other read write

       number will represent the abive thing < type of user  permission1 permission2 permission3>

       numbers like 0O666

       we can also use stat module

       using stat constants we can define the permission for each type of user

       for example :

       STAT CONSTANTS

stat.S_IRWXU: Owner Read, Write, Execute

stat.S_IRUSR: Owner Read

stat.S_IWUSR: Owner Write

stat.S_IXUSR: Owner Execute

(…GRP): Constants for Group read (e.g., stat.S_IRGRP)


(…OTH): Constants for Others read (e.g., stat.S_IROTH)


'''

mode=stat.S_IRUSR|stat.S_IRGRP|stat.S_IROTH

os.chmod("D:\Python_revision_files\OSModules\OsModules.py",mode)


# i try to write in file

with open ("D:\Python_revision_files\OSModules\OsModules.py",'r+') as f:
    r=f.read()
    print(r)
    f.write("")




'''
   command : chown

   to change the owner or a group for a file or directory.
'''


'''
  command: chstat()

  To get metadata of file or directory.
'''

