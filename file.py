import os
import subprocess
import stat
import grp, pwd
import shutil
word = r"""
   _,---.   .=-.-.             ,----.           ,-,--.                  ,-,--.  ,--.--------.    ,----.         ___   
  .-`.' ,  \ /==/_ / _.-.     ,-.--` , \        ,-.'-  _\ ,--.-.  .-,--.,-.'-  _\/==/,  -   , -\,-.--` , \ .-._ .'=.'\  
 /==/_  _.-'|==|, |.-,.'|    |==|-  _.-`       /==/_ ,_.'/==/- / /=/_ //==/_ ,_.'\==\.-.  - ,-./==|-  _.-`/==/ \|==|  | 
/==/-  '..-.|==|  |==|, |    |==|   `.-.       \==\  \   \==\, \/=/. / \==\  \    `--`\==\- \  |==|   `.-.|==|,|  / - | 
|==|_ ,    /|==|- |==|- |   /==/_ ,    /        \==\ -\   \==\  \/ -/   \==\ -\        \==\_ \/==/_ ,    /|==|  \/  , | 
|==|   .--' |==| ,|==|, |   |==|    .-'         _\==\ ,\   |==|  ,_/    _\==\ ,\       |==|- ||==|    .-' |==|- ,   _ | 
|==|-  |    |==|- |==|- `-._|==|_  ,`-._       /==/\/ _ |  \==\-, /    /==/\/ _ |      |==|, ||==|_  ,`-._|==| _ /\   | 
/==/   \    /==/. /==/ - , ,/==/ ,     /       \==\ - , /  /==/._/     \==\ - , /      /==/ -//==/ ,     //==/  / / , / 
`--`---'    `--`-``--`-----'`--`-----``         `--`---'   `--`-`       `--`---'       `--`--``--`-----`` `--`./  `--` 
"""

print(word)


class FileSystemManager:

    def read_file(self):
        try:
            file_name = input("Enter the filename path (e.g: /home/user-directory/file_name)")
       
            with open(file_name, 'r') as f:
                content = f.read()
                print("File content:")
                print(content)
        except FileNotFoundError:
            print(f"{file_name} not Found")
        except PermissionError:
            print(f"{file_name} cannot have read permssion on this current user")
    def write_file(self):
        file_name = input("Enter the file name: ")
        if os.path.exists(file_name):
            with open(file_name, 'a') as f:
                data = input("Enter the data to write: ")
                f.write(data)
                print("Data written successfully.")
        else:
            print("File not found.")
        
    def create_and_write_to_file(self):
        file_name = input("Enter the filename Path (e.g. /home/user-directory/file_name): ")
        if os.path.exists(file_name):
            print("File already exists.")
        else:
            with open(file_name, 'w') as f:
                print(f"{file_name} created successfully.")
            with open(file_name, 'a') as f:
                file = input(f"Enter something in {file_name}: ")
                f.write(file)
                print(f"Data Written Successfully in {file_name}")
    

    def delete_file(self):
        file_name = input("Enter the filename (e.g: /home/user/file_name): ")
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_name} deleted successfully.")
        else:
            print(f"{file_name} not found.")

    def create_directory_create_file_and_write_to_file(self):
        
    
        dir_name = input("Enter the directory name: ")
        if os.path.exists(dir_name):
            print(f"{dir_name} already exists.")
        else:
            home_dir = os.path.expanduser("~")
            print(home_dir)
            os.mkdir(dir_name)
            file = input("Do you want to create a regular file in this directory? (Y/N) ")
            if(file.lower() == "y" ):
                while True:
                    try:
                        he = input("Enter the file_name: ")
                        path = f"{home_dir}/{dir_name}/{he}"
                        if os.path.exists(path):
                            print(f"{path} file exists")
                        else:
                            with open(path, "w") as h:
                                try:
                                    ho = input(f"Do you want insert some data in {he}? (Y/N) ")
                                    if ho.lower() == "y":
                                        with open (path, "a") as h:
                                            da = input("Then enter some data here: ")
                                            h.write(da)
                                            print(f"Data have been written in {he}")
                                            break
                                    elif ho.lower() == "n":
                                        print("exiting")
                                        exit()
                                    else:
                                        print("Invalid input ")
                                except KeyboardInterrupt:
                                    a = input("\nYou really wanna terminate (Y/N): ")
                                    if a.lower() == "y":
                                        print("Terminating...")
                                        exit()
                                    else:
                                        continue
                        
                    except KeyboardInterrupt:
                        a = input("\nYou really wanna terminate (Y/N): ")
                        if a.lower() == "y":
                            print("Terminating...")
                            exit()
                        else:
                            continue

               
       
    def copy_file(self):
        source_file = input("Enter the source file path: ")
        destination_file = input("Enter the destination file path: ")

        if os.path.exists(source_file):
            try:
                shutil.copy(source_file, destination_file)
                print(f"{source_file} copied to {destination_file} successfully.")
            except shutil.Error as e:
                print(f"Error while copying: {e}")
        else:
            print(f"{source_file} not found.")

    def rename_file(self):
        old_name = input("Enter the current file path: ")
        new_name = input("Enter the new file path: ")

        if os.path.exists(old_name):
            try:
                os.rename(old_name, new_name)
                print(f"{old_name} renamed to {new_name} successfully.")
            except OSError as e:
                print(f"Error while renaming: {e}")
        else:
            print(f"{old_name} not found.")

    def move_file(self):
        source_file = input("Enter the source file path: ")
        destination_file = input("Enter the destination file path: ")

        if os.path.exists(source_file):
            try:
                shutil.move(source_file, destination_file)
                print(f"{source_file} moved to {destination_file} successfully.")
            except shutil.Error as e:
                print(f"Error while moving: {e}")
        else:
            print(f"{source_file} not found.")


    def get_file_permissions(self):
        try:
            file_path = input("Enter the filename or path along with filename (e.g., /home/kali):> ")
            if os.path.exists(file_path):
                file_mode = os.stat(file_path).st_mode
                owner_uid = os.stat(file_path).st_uid
                group_gid = os.stat(file_path).st_gid

                owner_permissions = ''
                group_permissions = ''
                other_permissions = ''

                owner_permissions += 'r' if file_mode & 0o400 else '-'
                owner_permissions += 'w' if file_mode & 0o200 else '-'
                owner_permissions += 'x' if file_mode & 0o100 else '-'
                owner_permissions += 'S' if file_mode & 0o4000 else ''
                
                group_permissions += 'r' if file_mode & 0o40 else '-'
                group_permissions += 'w' if file_mode & 0o20 else '-'
                group_permissions += 'x' if file_mode & 0o10 else '-'
                group_permissions += 'S' if file_mode & 0o2000 else ''

                other_permissions += 'r' if file_mode & 0o4 else '-'
                other_permissions += 'w' if file_mode & 0o2 else '-'
                other_permissions += 'x' if file_mode & 0o1 else '-'
                other_permissions += 't' if file_mode & 0o1000 else '-'

                owner_name = pwd.getpwuid(owner_uid).pw_name
                group_name = grp.getgrgid(group_gid).gr_name

                print("\t INDEX:\n\tr = read\n\tw = write\n\tx = execute\n\tS = SUID(Owner) or SGID(Group)\n\tt = Sticky bits\n")
                print(f"\t  PERMISSIONS {file_path}  ")
                print("\t|=======================================|")
                print(f"\t| Owner =  ({owner_name}):   {owner_permissions}\t\t|")
                print(f"\t| Group  = ({group_name})  :   {group_permissions}\t\t|")
                print(f"\t| Other   \t   :   {other_permissions}\t\t\t|")
                print("\t|=======================================|")
            else:
                print(f"{file_path} not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

                
                    
    def get_file_type(self,file_path):
        if os.path.islink(file_path):
            return "Symbolic Link"
        if os.path.isfile(file_path):
            return "Regular File"
        elif os.path.isdir(file_path):
            return "Directory"
    
        elif stat.S_ISBLK(os.stat(file_path).st_mode):
            return "Block File"
        elif stat.S_ISCHR(os.stat(file_path).st_mode):
            return "Character File"
        elif stat.S_ISFIFO(os.stat(file_path).st_mode):
            return "FIFO (Named Pipe)"
        elif stat.S_ISSOCK(os.stat(file_path).st_mode):
            return "Socket"
    
        else:
            return "Unknown File Type"

    def search_file_in_directory(self):
        
       
        file_name = input("Enter the filename to search along path: ")
        if os.path.exists(file_name):
            op = self.get_file_type(file_name)
            print(f"\n\t{file_name} filetype:: {op}\n")
        else:
            print(f"{file_name} not found.")
   

    def delete_dir(self):
        dir_name = input("Enter the name of the directory:")
        if os.path.exists(dir_name):
            os.rmdir(dir_name)
            print(f"{dir_name} has been deleted successfully.")
        else:
            print(f"{dir_name} does not exist.")
    def list_files_with_permissions(self):
        dir_name = input("Enter the directory name: ")
        
        if os.path.exists(dir_name):
            try:
                print(f"Listing files in directory: {dir_name}\n")
                for item in os.listdir(dir_name):
                    item_path = os.path.join(dir_name, item)
                    if os.path.isfile(item_path):
                        permissions = oct(os.stat(item_path).st_mode)[-4:]
                        print(f"\t\t{item} - Permissions: {permissions}")
                        print("---------------------------------------------")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"{dir_name} not found.")


    def change_file_permissions(self, file_path, mode):
        try:
            subprocess.run(['chmod', str(mode), file_path])
            print("File permissions changed successfully.")
        except subprocess.CalledProcessError as e:
            print("Error while changing file permissions:", str(e))

    def change_perm(self):
        file_path = input("Enter the file path (eg: /home/user-directory/file_name): ")
        if os.path.exists(file_path):
            mode_input = input("Enter the new file permissions (e.g., '755', '644'): ")
            try:
                mode = int(mode_input, 8)  # Convert octal string to integer
                self.change_file_permissions(file_path, mode)
            except ValueError:
                print("Invalid octal format. Please enter a valid octal number.")
        else:
            print(f"{file_path} not found.")

    def show_menu(self):
        print("File System Menu:")
        print('**************************************************************************************\n/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\n**************************************************************************************')
        print("\t1. Create File")
        print("\t2. Read File")
        print("\t3. Write File ")
        print("\t4. Create Directory")
        print("\t5. Checking permission of file")
        print("\t6. Search File type")
        print("\t7. Delete Directory")
        print("\t8. Delete File")
        print("\t9. Change permission")
        print("\t10. Copy File")
        print("\t11. Rename File")
        print("\t12. Move File")
        print("\t13: List all file in directory")
        print("\t14. Exit")

    def run(self):
        while True:
            try:
                self.show_menu()
                print("=============================================================================================")
                options = input("Select options(1 -- 10): ")
                if options == '1':
                    self.create_and_write_to_file()
                elif options == '2':
                    self.read_file()
                elif options == '3':
                    self.write_file()
                elif options == '4':
                    self.create_directory_create_file_and_write_to_file()
                elif options == '5':
                    self.get_file_permissions()
                elif options == '6':
                    self.search_file_in_directory()
                elif options == '7':
                    self.delete_dir()
                elif options == '8':
                    self.delete_file()
                elif options == '9':
                    self.change_perm()
                elif options == '14':
                    print("Exiting.")
                    break
                elif options == '10':
                    self.copy_file()
                elif options == '11':
                    self.rename_file()
                elif options == '12':
                    self.move_file()
                elif options == '13':
                    self.list_files_with_permissions()
                elif options == "KeyboardInterrupt":
                    print("hello")
                else:
                    print("Invalid options. Please enter a valid option.")
            except KeyboardInterrupt:
                a = input("\nYou really wanna terminate (Y/N): ")
                if a.lower() == "y":
                    print("Terminating...")
                    break
                else:
                    continue
if __name__ == "__main__":
    manager = FileSystemManager()
    manager.run()

