#!/usr/bin/env python3


from types import NoneType


def sendmail():
    import os
    from dotenv import load_dotenv, find_dotenv
    from lab_03 import EmailAddress, EmailDomain, EmailMessage, EmailServer

    load_dotenv(find_dotenv())

    mail_domain = os.environ.get("MAIL_DOMAIN")
    domain = os.environ.get("DOMAIN")
    mail_username = os.environ.get("MAIL_USERNAME")
    mail_password = os.environ.get("PASSWORD")
    user_name = os.environ.get("USER_NAME")
    user_domain = os.environ.get("USER_DOMAIN")

    mail_address = EmailAddress(
        user=mail_username or "",
        domain=EmailDomain(mail_domain or ""),
    )
    user_address = EmailAddress(
        user=user_name or "",
        domain=EmailDomain(user_domain or ""),
    )
    message = EmailMessage(from_addr=mail_address, to_addr=user_address)
    message.add_subject("The price has gone down!")

    server = EmailServer(
        email=mail_address,
        password=mail_password or "",
        email_domain=EmailDomain(domain or ""),
    )
    server.send_mail(user_email=user_address, message=message)


def data_scraping():
    import bs4, requests

    url = "https://www.emag.ro/telefon-mobil-motorola-g60-dual-sim-128gb-6gb-ram-6000-mah-dynamic-grey-panb0006pl/pd/DDMVQPMBM/?X-Search-Id=e80aa2c49153abba0b43&X-Product-Id=104307438&X-Search-Page=1&X-Search-Position=7&X-Section=search&X-MB=0&X-Search-Action=view"

    with requests.get(url) as req:
        soup = bs4.BeautifulSoup(req.text, "html.parser")

    price_element = soup.find("p", class_="product-new-price")
    if price_element is not None:
        price_str: str = price_element.text[:-4]
        import locale

        locale.setlocale(locale.LC_NUMERIC, "ro_RO.UTF-8")
        price: float = locale.atof(price_str)
    else:
        raise ValueError("Price could not be found!")

    if price < 1000:
        sendmail()
        print(f"The price has changed: {price}!")
    else:
        print(f"The price is the same: {price}.")

    # Honestly, I can't be bothered to complete this with the stuff in the
    # second picture (so sorry teacher for that), but you can see that it will
    # be the same thing, bar some refactoring on the email server's side.


def main():
    sendmail()
    data_scraping()


if __name__ == "__main__":
    main()
