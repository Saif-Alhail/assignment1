# Python / Django Work List Application

# Work List Application 
This is a Python, Django based worklist application. The application is intended to be used as a Work List /  To-Do tasks that can be updated and changed frequently to suit the user. The user can add tasks by entering the name and the date, which are required fields, and then clicking add. This will be saved onto the database sqlite3. The database base is then constantly used, and the homepage is refreshed accordingly to display the new database containing the tasks. There is a functionality to tag a task as pending, which indicates that the task is overdue; afterwards, clicking completed will remove the task. There is an edit function to change the name of the task. There is also a delete functionality for the task to be removed. There are sorting methods that the user can use; sorting by Date, Ascending alphabetically based on the task, descending alphabetically based on the task and by the pending status of the task.

# Start by cloning the project:
"""
git init
git clone https://github.com/Saif-Alhail/assignment1.git
"""
# Change to the main directory of assignment1
cd/assignment1

# Access the virtual environment (after creating one)
python -m venv ./{virutal environment name} 

# Install requirements by running the following command;
"""
pip install -r requirements.txt
"""
# Requirements
•	Python 3 +
•	Asgiref == 3.4.1
•	Django == 3.2.7
•	Pytz == 2021.1
•	Sqlparse == 0.4.2

# Make Migrations for Django
python manage.py makemigrations
python manage.py migrate

# Starting the application
cd/assignment
start the application by running the following command;
"""
python manage.py runserver
"""
# This application runs as a website, so the server has to be run first, then accessed through the URL: http://127.0.0.1:8000/
# To start the application next:
Access URL through: http://127.0.0.1:8000/

# Functionality 
The application works by refreshing the homepage to display the results appropriately; both task name and date are required inputs; when a task is added, that task is then identified by an ID that Django uses, and that task is added to the current database in the working directory. The homepage is automatically refreshed, and the new list of tasks within the database is called to the homepage displaying the new tasks. The function add within the views.py file is responsible for this operation. When the request method is a POST method, there is a new task to be added; the function checks whether the field is empty, and if it is, it will display a message and request input. When the requested form is valid and inserted, it shows the message that the task has been successfully added. Then at the end of the function, the return redirect(‘home’) is responsible for refreshing the homepage to display the updated tasks list. The edit function within the views.py file works by identifying which task is requested by the ID of that task, and checking whether that task is available or not, by checking by the ID within the database; when the task is identified, and the name of that task is changed, it overwrites the old task with the new one and refreshes the page.
The sorting method works by calling the home function, which displays the homepage, which initially has a default sorting method by date. When the appropriate sorting method is selected, such as Pending, the function within views.py {sort_pending} is called, which calls the home function and provides an input of -completed which indicates that the sorting method should be starting from the pending ones first. Then the homepage is refreshed with that sorting method. From the HTML side, once a sorting method is chosen, the appropriate sorting method is called in home.html from lines 34-37. If Ascending is selected, the sort_ascending function will be called from views.py, which refreshes the homepage with the new alphabetically sorted list.

# Testing
Adding a task requires both name and date inputs to be correctly identified within the database; a method to test this is to try and add a task by selecting the date and without adding a name. This results in a message that says, “You need to write something”, which means that the if statement within the function; add works correctly since the field was empty, and the if statements checks if the input field is empty. Another testing method is to add a task by name without any date, which results in the message “Please fill in all fields”. This indicates that the function add else statement works correctly since the if statement firsts check if the form is valid, which means that all fields are added; the name and date. If not, the program will go to the else statement, print out the message, and redirect to the homepage. 
Another testing method is to use the sorting method with duplicates. When the task date is the same, and the sort by date method is used, the sorting of the dates is correct since the task is saved correctly to the nearest second; when the tasks are sorted by the date, the program behaves correctly by sorting the tasks with the same date by the intended order where the latest task added is appropriately shown as the last task.  
