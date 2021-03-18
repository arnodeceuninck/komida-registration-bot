import requests

SESSION_COOKIE = 'hirepi8053%7C1617319326%7CdvowUVeELGr5sLzOIzYqe7OFd7tIfSfYOeNpk8bMh9V%7C77d935dd41afd36659cbf5472eb073402a14d0bafa0e9965fb5270f766daf567'

def register_tracking(user):
    cookies = {
        'pll_language': 'nl',
        'wordpress_logged_in_3fbacbcb0ab779434e30eaaaeb8d8449': SESSION_COOKIE,
        'complianceCookieROCLLNHC': 'on',
    }

    data = {
        "your-name": user.name,
        "tel-579": user.phone_number,
        "your-email": user.email,
        "acceptance-43": True
    }

    response = requests.post('https://nl-20202040ra.iziii.pro/wp-json/contact-form-7/v1/contact-forms/64009/feedback',
                             data=data, cookies=cookies)
    return response
