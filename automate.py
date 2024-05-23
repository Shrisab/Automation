import requests
from bs4 import BeautifulSoup

# Function to log in to the site
def login(memberID, memberDob):
    # URL of the login page
    login_url = 'https://taradev.deerhold.com/login'  # Update this URL

    # Start a session
    session = requests.Session()

    # Load the login page to get any necessary hidden form inputs
    login_page = session.get(login_url)
    soup = BeautifulSoup(login_page.text, 'html.parser')

    # Find the form action URL
    form_action_url = login_url  # Adjust if different from the login URL

    # Prepare the login data
    login_data = {
        'member_id_field_name': memberID,  # Update with the actual field name
        'dob_field_name': memberDob,  # Update with the actual field name
        # Include any other hidden inputs required by the form
    }

    # Perform the login
    response = session.post(form_action_url, data=login_data)

    # Check if login was successful
    if response.url == login_url:
        print('Login failed. Check your member ID and DOB.')
    else:
        print('Login successful!')
        # Now you can use the session to access other pages
        # For example, fetching the dashboard page
        dashboard_url = 'https://taradev.deerhold.com/dashboard'  # Update this URL
        dashboard_page = session.get(dashboard_url)
        print(dashboard_page.text)  # Print or process the dashboard page content

if __name__ == '__main__':
    memberID = input('Enter Member ID: ')
    memberDob = input('Enter Member DOB (YYYY-MM-DD): ')
    login(memberID, memberDob)
