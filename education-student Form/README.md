
# education-student Form
A Java-based application that allows users to manage classes and student information. It provides functionality to add, remove, change, show, save, and read class and student data.
Getting Started
To run the project, follow these steps:
Clone the repository to your local machine.
Open the project in your preferred Java IDE.
Compile and run the KH3.java file.
## Usage
Upon running the application, you will be presented with a menu to choose between education and student information. Enter the corresponding number to select your choice.

### Education Information
If you choose education information, you will have the following options:
- Add: Add a new education entry by providing the name, code, and phone number.
- Remove: Remove an education entry by specifying the index.
- Change: Modify an existing education entry by specifying the index and providing updated information.
- Show: Display all education entries.
- Save: Save the education data to a file.
- Read: Read education data from a file.
- Exit: Exit the education information menu.

### Student Information
If you choose student information, you will have the following options:
- Add: Add a new student entry by providing the name, student ID, and score.
- Remove: Remove a student entry by specifying the index.
- Change: Modify an existing student entry by specifying the index and providing the updated information.
- Show: Display all student entries.
- Save: Save the student data to a file.
- Read: Read student data from a file.
- Exit: Exit the student information menu.

## File Storage
The application uses text files to store education and student data. The education data is stored in the `Edu.txt` file, and the student data is stored in the `Stu.txt` file. When you choose the "Save" option, the corresponding data will be written to the respective file. Similarly, when you choose the "Read" option, the data will be read from the file and loaded into the application.
