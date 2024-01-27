from pages.practice_form_page import PracticeFormPage


def test_form_success_submission(driver):
    form_data = {
        'firstName': 'Alice',
        'lastName': 'Ivanova',
        'email':    'name@example.com',
        'phone':    '8999888776',
        'gender':   'Female',
        'subjects': ['Computer Science', 'Maths'],
        'birthday': {'day': '23', 'month': 'June', 'year': '1993'},
        'picture':  'picture.png',
        'address':  'Welcome st. 37-15',
        'state':    'Uttar Pradesh',
        'city':     'Agra'
    }

    page = PracticeFormPage(driver)
    page.open_page()
    page.fill_form(form_data)

    page.submit_form()
    page.check_form_submission(form_data)
