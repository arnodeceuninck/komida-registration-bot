# komida-registration-bot
Just send `-register` to the bot, and you get automatically added to the Komida table tracking, without having to enter your info manually every time (only the first time).
## Installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
In `bot.py`, update the token to your discord bot token. In `request.py`, update the session cookie to your cookie when logged in. This is currently the session of an account created with a temp mail. The session cookie expires every two weeks, it's still a TODO to fix this. 
## Running
```shell
python3 bot.py
```
## Development
### Getting the request
In Chrome, use inspect element, go to the Network tab, hit the submit button of the form.
You can see your request in the network tab (mine had the name `feedback`), right click it and copy as curl.
Then you can use https://curl.trillworks.com/ to convert your curl request to python code.

This is a sample curl request (with code from an incognito window):

```shell
curl 'https://nl-20202040ra.iziii.pro/wp-json/contact-form-7/v1/contact-forms/64009/feedback' \
  -H 'authority: nl-20202040ra.iziii.pro' \
  -H 'sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"' \
  -H 'accept: application/json, text/javascript, */*; q=0.01' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundaryBtlMZAndhOEFjkde' \
  -H 'origin: https://nl-20202040ra.iziii.pro' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://nl-20202040ra.iziii.pro/nl/tracking-komida-cmi/' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cookie: pll_language=nl; PHPSESSID=er15rvvocrepbj6tfu77v3q82l' \
  --data-raw $'------WebKitFormBoundaryBtlMZAndhOEFjkde\r\nContent-Disposition: form-data; name="_wpcf7"\r\n\r\n64009\r\n------WebKitFormBoundaryBtlMZAndhOEFjkde\r\nContent-Disposition: form-data; name="_wpcf7_version"\r\n\r\n5.1.7\r\n------WebKitFormBoundaryBtlMZAndhOEFjkde\r\nContent-Disposition: form-data; name="_wpcf7_locale"\r\n\r\nfr_FR\r\n------WebKitFormBoundaryBtlMZAndhOEFjkde\r\nContent-Disposition: form-data; name="_wpcf7_unit_tag"\r\n\r\nwpcf7-f64009-p63988-o1\r\n------WebKitFormBoundaryBtlMZAndhOEFjkde\r\nContent-Disposition: form-data; name="_wpcf7_container_post"\r\n\r\n63988\r\n------WebKitFormBoundaryBtlMZAndhOEFjkde\r\nContent-Disposition: form-data; name="your-name"\r\n\r\nJohn Doe\r\n------WebKitFormBoundaryBtlMZAndhOEFjkde\r\nContent-Disposition: form-data; name="tel-579"\r\n\r\n0444444444\r\n------WebKitFormBoundaryBtlMZAndhOEFjkde\r\nContent-Disposition: form-data; name="your-email"\r\n\r\nhirepi8053@leonvero.com\r\n------WebKitFormBoundaryBtlMZAndhOEFjkde\r\nContent-Disposition: form-data; name="acceptance-43"\r\n\r\n1\r\n------WebKitFormBoundaryBtlMZAndhOEFjkde\r\nContent-Disposition: form-data; name="submission_id-77"\r\n\r\n1132\r\n------WebKitFormBoundaryBtlMZAndhOEFjkde--\r\n' \
  --compressed
```
In the converted python code, it's recommended to change the raw data to a more readable python dict. 