**PyFloraApp by Ivan Logožar**
PyFloraApp is a Python 3.10.10 demonstration app developed as the final project for the Python Developer Course at Algebra University.

Overview:
The PyFloraApp showcases a range of functionalities, including login and sign-up features, basic CRUD operations, database management, and Tkinter-based GUI. Additionally, it employs graph plotting capabilities using Pandas and Matplotlib.

Getting Started:
To access the PyFloraApp, follow these instructions:
**1.Navigate to the root folder:**
`cd absolute_path_to_root_folder`
_Alternatively, you can open the root folder in an integrated terminal using the right-click option._

**2.Install the required dependencies:**
`pip install -r requirements.txt`

**3.Run the app:**
Click on run_app.py to execute the PyFloraApp, or use the following command:
`python3 run_app.py`

**Functionality:**
- User Management
The app provides a secure login and sign-up functionality for users. New profiles can be created instantly via the Register option. For accessing already created users, use the following credentials:
- Username: Algebra
- Password: Algebra123

**Databases:**
The PyFloraApp consists of four databases for different purposes:
- Users: Stores user data for login functionality.
- Plants: Keeps records of various plant details.
- Pots: Manages pots created from plants, along with their associated data.
- Data: Holds data required for plotting graphs and creating pots.

**My Profile:**
Signed-up users can modify their information through the My Profile menu after logging in.

**My Pots:**
The My Pots menu displays the user's active pots along with their respective sensor readings. Sensor readings are automatically saved when loading the My Pots menu or clicking on the Sync Data button. Users have the option to edit their pots.

_Disclaimer: Please note that sensor readings are currently simulated via a script, while temperature data is fetched through an API. The graphs are plotted using 10 results from the sensor readings inside the database. However, there might be some inconsistencies due to inaccuracies in the mock data._