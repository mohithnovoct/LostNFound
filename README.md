<center><h1>University Lost and Found App<br></h1></center>
<hr/>
<h4>The University Lost and Found App is a web application designed to help university students and staff report and find lost or found items on campus. Built with Django, this app provides a user-friendly interface for posting items, browsing listings, and contacting users who have posted items.
Features</h4>

<b>Post Lost/Found Items</b>: Authenticated users can post items they’ve lost or found, including a title, description, location, category, and optional image.<br>
<b>Browse Items</b>: View all items or filter by category (Lost or Found).<br>
<b>User-Specific Posts</b>: Users can view their own posted items under "My Posts".<br>
<b>Contact Information</b>: Item listings include the contact number of the user who posted the item (if provided).<br>
<b>Responsive Design</b>: The app is styled with Bootstrap 4 for a modern, mobile-friendly UI.<br>
<b>Admin Panel</b>: Administrators can manage items and user profiles via Django’s admin interface.<br>
<h2>Technologies Used</h2>

<b>Backend</b>: Django 5.2.1, Python 3.12.9<br>
<b>Frontend</b>: Bootstrap 4, Custom CSS<br>
<b>Database</b>: SQLite (default for development)<br>
<b>Form Rendering</b>: django-crispy-forms with crispy-bootstrap4<br>
<b>Static Files</b>: Django’s static file handling<br>

<b>Prerequisites
Before running the project, ensure you have the following installed:

Python 3.12.9 or higher
pip (Python package manager)
virtualenv (optional but recommended for creating isolated environments)
Git (to clone the repository)

Setup Instructions
Follow these steps to set up the project locally on your machine.
1. Clone the Repository
Clone the repository from GitHub to your local machine:
git clone https://github.com/<your-username>/lostnfound-app.git
cd lostnfound-app

2. Create and Activate a Virtual Environment
It’s recommended to use a virtual environment to manage dependencies.
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
Install the required Python packages using pip. The project dependencies are listed below (you may need to create a requirements.txt file if not already present).
pip install django==5.2.1 django-crispy-forms crispy-bootstrap4 pillow

Alternatively, if a requirements.txt file is provided in the repository, you can install all dependencies at once:
pip install -r requirements.txt

4. Apply Migrations
Set up the database by running migrations. This will create the necessary tables in SQLite.
python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (Optional)
Create a superuser account to access the Django admin panel.
python manage.py createsuperuser

Follow the prompts to set up a username, email, and password.
Running the Project
Once the setup is complete, you can run the development server.
1. Start the Development Server
Run the following command to start the Django development server:
python manage.py runserver

2. Access the App
Open your browser and navigate to:
http://127.0.0.1:8000/

3. Access the Admin Panel (Optional)
If you created a superuser, you can access the admin panel at:
http://127.0.0.1:8000/admin/

Log in with your superuser credentials to manage items and user profiles.
Usage

Home Page: Browse all lost and found items or filter by category (Lost or Found).
Register/Login: Create an account or log in to post items.
Post an Item: Navigate to "Post Item" to add a new lost or found item.
View Details: Click on an item to see more details, including the poster’s contact number (if provided).
My Posts: View all items you’ve posted under "My Posts".
Contact: Use the contact page to send a message (currently logs to the console).

Contributing
Contributions are welcome! To contribute:<br>

<b>Fork the repository.<br>
Create a new branch (git checkout -b feature/your-feature).<br>
Make your changes and commit them (git commit -m "Add your feature").<br>
Push to your branch (git push origin feature/your-feature).<br>
Open a pull request.<br>

This project is licensed under the MIT License. See the LICENSE file for details.</b>
