#! python3

import sys
import os
import shutil
import send2trash #pip install send2trash

print('Welcome to the Python File Manager\n')

# Stores every drive connected on PC in a list.
drives = [chr(x) + ':' for x in range(65, 90) if os.path.exists(chr(x) + ':')]

# Lists each folder and file present in the current working directory
def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x)

while True:
    print("1.Open Files/Folders \n2.Rename \n3.Move and Paste \n4.Copy and Paste \n5.Delete\n")
    result = input("Choose one of the following: ")

    if result == '1':
        # Home Screen
        print('\nQuick Acess:\n1. Documents\n2. Videos\n3. Pictures\n4. Downloads\n')

        print('Drives: ')
        for x in range(len(drives)):
            print(str(5 + x) + '. ' + drives[x])

        while True:
            inp = input("\nEnter Your Choice: ")

            if inp == '1':
                path = 'C:\\Users\\$USERNAME\\Documents'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '2':
                path = 'C:\\Users\\$USERNAME\\Videos'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '3':
                path = 'C:\\Users\\$USERNAME\\Pictures'
                os.chdir(os.path.expandvars(path))
                break

            elif inp == '4':
                path = 'C:\\Users\\$USERNAME\\Downloads'
                os.chdir(os.path.expandvars(path))
                break

            elif inp in drives:
                os.chdir(inp + '\\')
                break

            else:
                print('Error\nEnter a correct input / drive name.\n')

        while True:

            listDirectories()

            print('\n\nType "exitManager" to Exit from File Manager.')
            print('Type "backManager" to go up one Directory.')
            res = input('\nChoose a File/Folder: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):
                    os.system('"' + res + '"')
                else:
                    os.chdir(res)

            elif res == 'exitManager':                          # Exit command to exit from loop
                sys.exit(0)

            elif res == 'backManager':                          # Back command to go up one directory
                os.chdir('..')

            else:
                print('No File/Folder Exist of this Name.')

    if result == '2':
        print("You Choose to Rename")
        print('Drives: ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])

        while True:
            inp = input("\nEnter Your Choice: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct Drive Name.\n')

        while True:

            listDirectories()

            print('\n\nType "exitManager" to exit from File Manager.')
            print('Type "backManager" to go up 0ne Directory.')
            print('Type "renameManager" to Rename This Directory')

            res = input('\nChoose a File to Rename: ')
            print('\n')

            if res in os.listdir(os.getcwd()):
                if os.path.isfile(res):

                    new_name = input("Enter a New Name: ")
                    ogDir = res
                    newDir = os.getcwd() + '\\' + new_name
                    shutil.move(ogDir, newDir)
                else:
                    os.chdir(res)

            elif res == 'exitManager':    # Exit command to exit from loop
                sys.exit(0)

            elif res == 'backManager':    # Back command to go up one directory
                os.chdir('..')

            elif res == 'renameManager':  # Rename command to delete one directory

                new_name = input("Enter a New Name: ")
                ogDir = os.getcwd()
                os.chdir('..')
                newDir = os.getcwd() + '\\' + new_name
                shutil.move(ogDir, newDir)

            else:
                print('No File/Folder exist of This Name.')

    if result == '3':
        print("You choose to Move")
        print('Drives: ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])

        while True:
            inp = input("\nEnter Your Choice: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a correct Drive Name.\n')

        while True:

            listDirectories()

            print('\n\nType "exitManager" to Exit from File Manager.')
            print('Type "backManager" to go up One Directory.')
            print('Type "cutManager" to move This Directory')

            res = input('\nChoose a File to Move: ')
            print('\n')

            if res in os.listdir(os.getcwd()):

                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("\nMove " + res + " to a Desired Location.")

                    while True:
                        for x in range(len(drives)):
                            print(str(1 + x) + '. ' + drives[x])

                        inp2 = input("\nEnter Your Choice: ")

                        if inp2 in drives:
                            os.chdir(inp2 + '\\')
                            break
                        else:
                            print('Error\nEnter a Correct Drive Name.\n')

                    while True:
                        listDirectories()

                        print('Type "pasteManager" to paste This File in Current Directory')

                        res2 = input('\nChoose a File to Move: ')
                        print('\n')

                        if res2 in os.listdir(os.getcwd()):
                            if os.path.isfile(res):
                                print("You can't choose a File.\nPlease choose a Folder.")
                            else:
                                os.chdir(res2)

                        elif res2 == 'pasteManager':
                            shutil.move(og_path, os.getcwd())
                            break

                else:
                    os.chdir(res)


            elif res == 'exitManager':                          # Exit command to exit from loop
                sys.exit(0)

            elif res == 'backManager':                          # Back command to go up one directory
                os.chdir('..')

            elif res == 'cutManager':
                og_path = os.getcwd()

                print("Moving the Current Directory")
                while True:
                    for x in range(len(drives)):
                        print(str(1 + x) + '. ' + drives[x])

                    inp2 = input("\nEnter Your Choice: ")

                    if inp2 in drives:
                        os.chdir(inp2 + '\\')
                        break
                    else:
                        print('Error\nEnter a Correct Drive Name.\n')

                while True:
                    listDirectories()

                    print('\nType "pasteManager" to paste This Folder in Current Directory')

                    res2 = input('\nChoose a Folder to Open: ')
                    print('\n')

                    if res2 in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            print("You can't choose a File.\nPlease choose a Folder.")
                        else:
                            os.chdir(res2)

                    elif res2 == 'pasteManager':
                        shutil.move(og_path, os.getcwd())
                        break

            else:
                print('No File/Folder Exist of This Name.')

    if result == '4':
        print("You choose to Copy")
        print('Drives: ')
        for x in range(len(drives)):
            print(str(1 + x) + '. ' + drives[x])

        while True:
            inp = input("\nEnter Your Choice: ")

            if inp in drives:
                os.chdir(inp + '\\')
                break
            else:
                print('Error\nEnter a Correct Drive Name.\n')

        while True:

            listDirectories()

            print('\n\nType "exitManager" to Exit from File Manager.')
            print('Type "backManager" to go up One Directory.')
            print('Type "copyManager" to copy This Directory')

            res = input('\nChoose a File to Copy: ')
            print('\n')

            if res in os.listdir(os.getcwd()):

                if os.path.isfile(res):
                    og_path = os.getcwd() + "\\" + res
                    print("Move " + res + " to a Desired Location.")

                    while True:
                        for x in range(len(drives)):
                            print(str(1 + x) + '. ' + drives[x])

                        inp2 = input("\nEnter Your Choice: ")

                        if inp2 in drives:
                            os.chdir(inp2 + '\\')
                            break
                        else:
                            print('Error\nEnter a Correct Drive Name.\n')

                    while True:
                        listDirectories()

                        print('Type "pasteManager" to copy This File in Current Directory')

                        res2 = input('\nChoose a File to Move: ')
                        print('\n')

                        if res2 in os.listdir(os.getcwd()):
                            if os.path.isfile(res):
                                print("You can't choose a File.\nPlease choose a Folder.")
                            else:
                                os.chdir(res2)

                        elif res2 == 'pasteManager':
                            shutil.copy(og_path, os.getcwd())
                            break

                else:
                    os.chdir(res)


            elif res == 'exitManager':  # Exit command to exit from loop
                sys.exit(0)

            elif res == 'backManager':  # Back command to go up one directory
                os.chdir('..')

            elif res == 'copyManager':
                og_path = os.getcwd()

                print("Copying the Current Directory")
                while True:
                    for x in range(len(drives)):
                        print(str(1 + x) + '. ' + drives[x])

                    inp2 = input("\nEnter Your Choice: ")

                    if inp2 in drives:
                        os.chdir(inp2 + '\\')
                        break
                    else:
                        print('Error\nEnter a Correct Drive Name.\n')

                while True:
                    listDirectories()

                    print('\nType "pasteManager" to copy This File in Current Directory')

                    res2 = input('\nChoose a Folder to Open: ')
                    print('\n')

                    if res2 in os.listdir(os.getcwd()):
                        if os.path.isfile(res):
                            print("You can't choose a File.\nPlease choose a Folder.")
                        else:
                            os.chdir(res2)

                    elif res2 == 'pasteManager':
                        print(og_path)
                        folder_name = og_path.split('\\')[-1]
                        folder_directory = os.getcwd() + '\\' + folder_name
                        shutil.copytree(og_path, folder_directory)
                        break

            else:
                print('No File/Folder Exist of This Name.')

    if result == '5':
        while True:

            # Options to delete files/folders to permanently or otherwise
            print('\n1. Permanently \n2. Recycle Bin')
            query = input('Would You like to Permanently Delete or Send to Recycle Bin?: ')

            if query == '1':
                print('You choose to Permanently Delete Files/Folders.\n')
                print('Drives: ')
                for x in range(len(drives)):
                    print(str(1 + x) + '. ' + drives[x])

                while True:
                    inp = input("\nEnter Your Choice: ")

                    if inp in drives:
                        os.chdir(inp + '\\')
                        break
                    else:
                        print('Error\nEnter a Correct Drive Name.\n')

                while True:

                    listDirectories()

                    print('\n\nType "exitManager" to Exit from File Manager.')
                    print('Type "backManager" to go up One Directory.')
                    print('Type "deleteManager" to Permanently Delete This Directory')

                    res = input('\nChoose a File to Delete: ')
                    print('\n')

                    if res in os.listdir(os.getcwd()):
                        if os.path.isfile(res):

                            # Warning to prevent unnecessary deletion
                            print('Are You sure You want to Permanently Delete This Folder? (YES/NO)')
                            ans = input('Yes or No: ')
                            if ans.lower() == 'yes' or 'y':
                                os.unlink(res)
                        else:
                            os.chdir(res)

                    elif res == 'exitManager':                      # Exit command to exit from loop
                        sys.exit(0)

                    elif res == 'backManager':                      # Back command to go up one directory
                        os.chdir('..')

                    elif res == 'deleteManager':                    # Delete command to delete one directory

                        # Warning to prevent unnecessary deletion
                        print('Are You sure You want to Permanently Delete This Folder? (YES/NO)')
                        ans = input('Yes or No: ')

                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            shutil.rmtree(path)

                    else:
                        print('No File/Folder Exist of This Name.')

            elif query == '2':
                print('You choose to temporarily Delete Files/Folders.')
                print('Drives: ')
                for x in range(len(drives)):
                    print(str(1 + x) + '. ' + drives[x])

                while True:
                    inp = input("\nEnter Your Choice: ")

                    if inp in drives:
                        os.chdir(inp + '\\')
                        break
                    else:
                        print('Error\nEnter a Correct Drive Name.\n')

                while True:

                    listDirectories()

                    print('\n\nType "exitManager" to Exit from File Manager.')
                    print('Type "backManager" to go up One Directory.')
                    print('Type "deleteManager" to Send This Directory to Recycle Bin')

                    res = input('\nChoose a File to Delete: ')
                    print('\n')

                    if res in os.listdir(os.getcwd()):
                        if os.path.isfile(res):

                            # Warning to prevent unnecessary deletion
                            print('Are You sure You want to Send This Folder to Recycle Bin? (YES/NO)')
                            ans = input('Yes or No: ')
                            if ans.lower() == 'yes' or 'y':
                                send2trash.send2trash(res)
                        else:
                            os.chdir(res)

                    elif res == 'exitManager':  # Exit command to exit from loop
                        sys.exit(0)

                    elif res == 'backManager':  # Back command to go up one directory
                        os.chdir('..')

                    elif res == 'deleteManager':  # Delete command to delete one directory

                        # Warning to prevent unnecessary deletion
                        print('Are You sure You want to Send This Folder to Recycle Bin? (YES/NO)')
                        ans = input('Yes or No: ')

                        if ans.lower() == 'yes' or 'y':
                            path = os.getcwd()
                            os.chdir('..')
                            send2trash.send2trash(path)

                    else:
                        print('No File/Folder Exist of This Name.')

        else:
            print('You Choose Wrong Number')
