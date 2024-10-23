
#### 📦 Local Deployment  
1. Clone the repository from GitHub by clicking the "Code" button and copying the URL.
2. Open your preferred IDE and open a terminal session in the directory you want to clone the repository to.
3. Type `git clone` followed by the URL you copied in step 1 and press enter.
4. Install the required dependencies by typing `pip install -r requirements.txt` in the terminal.
5. Note: The project is setup to use environment variables. You will need to set these up in your local environment. See [Environment Variables](#environment-variables) for more information.
6. Connect your database of choice and run the migrations by typing `python manage.py migrate` in the terminal.
7. Create a superuser by typing `python manage.py createsuperuser` in the terminal and following the prompts.
8. Optional: Fixtures for Flight, Airport and Aircraft models are included in the project in the `fixtures` directory. To add pre-populated data to the database, run `python manage.py loaddata fixtures/[fixture_name].json`.
9. Run the app by typing `python manage.py runserver` in the terminal and opening the URL in your browser.

#### 💜 Heroku Deployment
1. Login to the Heroku dashboard and create a new app.
2. Connect your GitHub repository to your Heroku app.
3. In the Settings tab, ensure that the Python Buildpack is added.
4. Set environment variables in the Config Vars section of the Settings tab.
5. In the Deploy tab, enable automatic deploys from your GitHub repository.
6. Click the "Deploy Branch" button to deploy the app.
7. Once the app has been deployed, click the "Open App" button to view the app.

### User Testing

User testing ensures that key user-facing features, such as authentication, profile management, and form submissions, work as expected. The following outlines the key areas to test and how to approach them:

#### 1. User Authentication

Test the following user actions to verify the authentication flow:

- **User Registration:**  
  Ensure that users can successfully register by submitting the registration form with valid credentials. After registration, users should be redirected to the appropriate page, and the new account should be created in the database.

- **User Login:**  
  Verify that users can log in using valid credentials. Upon successful login, users should be redirected to their dashboard or homepage, and their session should indicate they are authenticated.

- **User Logout:**  
  Test that users can log out successfully and are redirected to the appropriate page. After logging out, they should no longer have access to any authenticated areas.

#### 2. User Profiles and Dashboard

Test the ability for users to view and manage their profiles:

- **Profile Page Access:**  
  Confirm that authenticated users can access their profile page. The profile page should display user-specific information, and unauthorized users should not be able to access it.

- **Dashboard Access:**  
  Ensure that logged-in users can access their dashboard. Non-authenticated users should be redirected to the login page when attempting to access restricted areas like the dashboard.

#### 3. Form Submissions

Test forms to ensure users can successfully submit data:

- **Posting Comments or Creating Items:**  
  Verify that users can submit forms such as posting comments or creating content (e.g., blog posts, tasks). After submission, users should be redirected or shown a success message, and the new data should be stored and displayed correctly.

#### 4. Permissions and Access Control

Test that access to certain areas is restricted appropriately:

- **Authenticated-only Views:**  
  Ensure that pages like user dashboards, profile management, and other restricted content are only accessible to logged-in users. Non-authenticated users should be redirected to the login page if they attempt to access these pages.

- **Form Access:**  
  Confirm that only users with the correct permissions can access and submit certain forms, like admin or moderator-level actions.


## Credit

All credit goes to Dee MC and her follow along 'https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&index=1&ab_channel=DeeMc'
