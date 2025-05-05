# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MOHD NAQUI

*INTERN ID*: CT12VTA

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 8 WEEEKS

*MENTOR*: NEELA SANTOSH



*DESCRIPTION*:

            This tool is designed to ensure that files have not been tampered with by monitoring changes using cryptographic hash values.

The primary function of this tool is to calculate and compare SHA-256 hash values of files. A hash function takes the file's content and converts it into a unique fixed-size string (hash value). If even a single character in the file changes, the resulting hash value changes significantly. This makes it a powerful method to detect any form of file modification, whether it is accidental, malicious, or unintentional.

The Python script I developed includes the following core features:

Calculate SHA-256 hash of any file provided by the user.

Store the hash in a .hash file for future comparisons.

Load and compare the stored hash with the current hash of the file.

Warn the user if any changes are detected in the file.

Provide a simple and guided command-line interface to help users easily interact with the tool.


The script is structured using modular functions such as calculate_file_hash(), save_hash(), and load_saved_hash(). This modular approach makes the code clean, readable, and easy to maintain. It also helps in debugging and future improvements. The script reads the file in chunks of 4 KB, which ensures efficient memory usage, especially when dealing with large files. It also includes error-handling mechanisms to catch common issues like missing files or permission-related problems, thus ensuring a smooth user experience.




Libraries and Tools Used:

Python – The core language used to develop this tool.

hashlib – A standard built-in Python library that supports hashing using algorithms like SHA-256.

os – Another standard Python module that allows interaction with the operating system, such as checking whether a file exists.

Visual Studio Code (VS Code) – A powerful and lightweight code editor used for writing, editing, and running the Python script. 



Applications and Use Cases:

Such file integrity checking tools are widely used in various fields like cybersecurity, antivirus software, version control systems, backup verification, and auditing systems. For instance, system administrators can use these tools to regularly check whether critical system configuration files or logs have been altered. Similarly, software developers can use them to ensure that application files remain untouched and secure throughout deployment.

In the real world, many large-scale security systems rely on hashing algorithms to verify the authenticity and integrity of files.


     
