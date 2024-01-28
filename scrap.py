import requests
from bs4 import BeautifulSoup


def get_webpage_text(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract text from the parsed HTML
            page_text = soup.get_text()

            return page_text
        else:
            print(f"Error: Unable to fetch the webpage. Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


# Example: Get text from the OpenAI homepage
url = "https://www.flipkart.com/sandisk-e61-1050-mbs-window-mac-os-android-portable-type-c-enabled-5-y-warranty-usb-3-2-1-tb-wired-external-solid-state-drive-ssd/p/itm0c206e0687ae9?pid=ACCGYSPEYXV2EUPW&lid=LSTACCGYSPEYXV2EUPWDNUB4W&marketplace=FLIPKART&store=6bo%2Fjdy%2Fdus&srno=b_1_1&otracker=browse&fm=organic&iid=en_hv--xLG98wRcppW7UJiAjDPxCIVyCtoGRKLwFpoHqjCgWueKt2-ou-dVW7IQmzuzoMpLHbPBBwQlr9ATDGg5Ng%3D%3D&ppt=None&ppn=None&ssid=f64imx9b3k0000001706459295300"
webpage_text = get_webpage_text(url)

if webpage_text:
    print(webpage_text)
