#file_integrity_checker
import hashlib
import os

def calculate_file_hash(filepath):
    """
    Calculate SHA-256 hash of a file.
    """
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_hash(filepath, hash_value):
    """
    Save the calculated hash into a .hash file.
    """
    with open(filepath + '.hash', 'w') as f:
        f.write(hash_value)

def load_saved_hash(filepath):
    """
    Load the previously saved hash from the .hash file.
    """
    try:
        with open(filepath + '.hash', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return None

def main():
    print("=== File Integrity Checker ===")
    filepath = input("Enter the full path of the file to check: ").strip()

    if not os.path.isfile(filepath):
        print("Error: The specified file does not exist.")
        return

    current_hash = calculate_file_hash(filepath)
    if current_hash is None:
        return

    saved_hash = load_saved_hash(filepath)

    if saved_hash is None:
        print("\nNo saved hash found for this file.")
        choice = input("Do you want to save the current hash? (y/n): ").strip().lower()
        if choice == 'y':
            save_hash(filepath, current_hash)
            print("Hash saved successfully. You can now monitor this file's integrity.")
        else:
            print("Hash not saved. Exiting.")
    else:
        if current_hash == saved_hash:
            print("\nResult: File is intact. No changes detected.")
        else:
            print("\nWarning: File has been modified!")

if __name__ == "__main__":
    main()
