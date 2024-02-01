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
    modal_content = page.get_modal_content()

    assert 'Thanks for submitting the form' in modal_content
    assert form_data.get('firstName') in modal_content
    assert form_data.get('lastName') in modal_content
    assert form_data.get('email') in modal_content
    assert form_data.get('phone') in modal_content
    assert form_data.get('gender') in modal_content

    assert ', '.join(form_data.get('subjects')) in modal_content

    birth_day, birth_month, birth_year = form_data.get('birthday').values()
    expected_birthday = f"{birth_day} {birth_month},{birth_year}"
    assert expected_birthday in modal_content

    assert form_data.get('picture') in modal_content
    assert form_data.get('address') in modal_content
    assert form_data.get('state') in modal_content
    assert form_data.get('city') in modal_content
