import os
import zipfile
import re
import random
import string

dir_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
files_dir = f"/tmp/temp{dir_name}"

if not os.path.exists(files_dir):
        os.makedirs(files_dir)

def create_book(filename):
    if re.search(r'[;|&.$(){}/]', filename):
        return "\nInvalid filename"
    filename = filename+'.txt'
    with open(os.path.join(files_dir, filename), "w") as f:
        f.write("")
    return f"\nBook '{filename}' created successfully in the '{files_dir}' directory"

def check_stock():
    book_files = os.listdir(files_dir)
    return f"\nStock information: Total {files_dir} in stock: {len(book_files)}"

def write_to_book(filename, content):
    if re.search(r'[;|&.$(){}/]', filename):
        return "\nInvalid filename"
    with open(os.path.join(files_dir, filename+'.txt'), "a") as f:
        f.write(content + "\n")
    return f"\nContent added to book '{filename}.txt'"

def read_book(filename):
    if re.search(r'[;|&.$(){}/]', filename):
        return "\nInvalid filename"
    try:
        with open(f"{files_dir}/{filename}.txt" ,"r") as f:
            content = f.read()
        return "\n"+content
    except FileNotFoundError:
        return f"\nBook '{filename}.txt' not found"

def archive_files(filename,dest):
    if re.search(r'[;|&$(){}]', filename):
        return "\nInvalid filename"
    os.system(f"zip -j {files_dir}/{dest}.zip {files_dir}/{filename}")
    return f"\nFiles archived successfully as {dest}.zip"

def unzip_archives(filename):
    if re.search(r'[;|&$(){}]', filename):
        return "\nInvalid filename"
    os.system(f"unzip {files_dir}/{filename}.zip -d {files_dir}/")
    return "\nFiles extracted successfully"

def list_files():
    books_directory = os.listdir(files_dir)
    return "\n".join(books_directory)

def main():
    while True:
        print("\n\nOptions:")
        print("1. Create a book")
        print("2. Check stock")
        print("3. Write to book")
        print("4. Read book")
        print("5. Archive files")
        print("6. Unzip archives")
        print("7. List files")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            filename = input("Enter filename for the book: ")
            response = create_book(filename)
        elif choice == '2':
            response = check_stock()
        elif choice == '3':
            filename = input("Enter filename to write to: ")
            content = input("Enter content to write to the book: ")
            response = write_to_book(filename, content)
        elif choice == '4':
            filename = input("Enter filename to read: ")
            response = read_book(filename)
        elif choice == '5':
            filename = input("Enter filename to archive: ")
            dest= input("Enter destination archive name: ")
            response = archive_files(filename,dest)
        elif choice == '6':
            filename = input("Enter filename to unzip: ")
            response = unzip_archives(filename)
        elif choice == '7':
            response = list_files()
        elif choice == '8':
            print("\nExiting the program.")
            break
        else:
            response = "\nInvalid choice"
        print(response)

if __name__ == "__main__":
    main()
