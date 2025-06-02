from behave import given, when, then
from app import app

@given('the user enters the username "{username}" and password "{password}"')
def enter_credentials(context, username, password):
    context.client = app.test_client()
    context.response = context.client.post('/login', data={'username': username, 'password': password}, follow_redirects=True)

@when('they click the login button')
def click_login(context):
    pass #had to click the button in the last call

@then('they should be redirected to the dashboard')
def redirect_dashboard(context):
    #test that the dashboard page was reached
    assert b'dashboard' in context.response.data.lower()

@then('they should see an error message')
def error_login(context):
    #test there were invalid credentials
    # print("The response is ", context.response.data.lower())
    assert b"invalid credentials" in context.response.data.lower()