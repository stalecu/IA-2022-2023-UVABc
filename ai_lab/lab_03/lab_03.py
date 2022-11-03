#!/usr/bin/env python3

import os
from pyisemail import is_email
from pyisemail.diagnosis import ValidDiagnosis
import re
import warnings
import dns, dns.resolver
import smtplib
from enum import Enum


class Port(Enum):
    SMTP = 465
    SMTP_ALT = 26
    IMAP = 933
    POP3 = 995


class EmailDomain:
    def __init__(self, domain: str):
        if re.match("^.+\\..+$", domain, re.I) is None:
            msg = "Not a valid domain: '{}'".format(domain)
            raise ValueError(msg)
        record_types = ("MX", "AAAA", "A")
        record_count = 0
        for record_type in record_types:
            try:
                if len(dns.resolver.query(domain, record_type)):
                    record_count += 1
                    self.domain = domain
            except:
                continue

        if record_count == 0:
            msg = "No DNS records of types {} found for {}".format(record_types, domain)
            warnings.warn(msg)


class EmailAddress:
    def __init__(self, user: str, domain: EmailDomain) -> None:
        """
        Create an email address of the form user@domain.
        """
        diagnosis = is_email(f"{user}@{domain.domain}", diagnose=True)
        if (
            diagnosis
            and isinstance(diagnosis, bool)
            or isinstance(diagnosis, ValidDiagnosis)
        ):
            self.user = user
            self.domain = domain

        if not isinstance(diagnosis, bool) and not isinstance(
            diagnosis, ValidDiagnosis
        ):
            raise ValueError(diagnosis.message)

    def __str__(self) -> str:
        """
        Return "user@domain" as a string.
        """
        return f"{self.user}@{self.domain}"


class EmailMessage:
    def __init__(self, from_addr: EmailAddress, to_addr: EmailAddress) -> None:
        """
        Create an email message.
        """
        self.from_addr = from_addr
        self.to_addr = to_addr

    def add_subject(self, subject: str) -> None:
        """
        Add a subject to the existing email message
        """
        self.subject = subject


class EmailServer:
    def __init__(
        self, email: EmailAddress, password: str, email_domain: EmailDomain
    ) -> None:
        self.email = email
        self.password = password
        self.email_domain = email_domain

    def send_mail(self, user_email: EmailAddress, message: EmailMessage) -> None:
        server = smtplib.SMTP(self.email_domain.domain, Port.SMTP_ALT.value)
        server.starttls()
        server.login(str(self.email), self.password)
        try:
            server.sendmail(
                str(self.email), str(user_email), f"Subject: {message.subject}"
            )
        finally:
            server.quit()
