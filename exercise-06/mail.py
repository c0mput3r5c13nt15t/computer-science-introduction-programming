class MailAddress:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain


class Mail:
    def __init__(self, sender: MailAddress, receiver: MailAddress, subject: str, body: str):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body


class MailAccount:
    def __init__(self, name: str, inbox: list[Mail], outbox: list[Mail]):
        self.name = name
        self.inbox = inbox
        self.outbox = outbox


class MailServer:
    def __init__(self, domain: str, accounts: list[MailAccount]):
        self.domain = domain
        self.accounts = accounts


def show_mail_address(mail_address: MailAddress) -> str:
    return f"{mail_address.name}@{mail_address.domain}"


def show_mail(mail: Mail) -> str:
    return f"From: {show_mail_address(mail.sender)}\nTo: {show_mail_address(mail.receiver)}\nSubject: {mail.subject}\n{mail.body}"


def show_mail_account(mail_account: MailAccount) -> str:
    return_string = f"Name: {mail_account.name}\nInbox: {len(mail_account.inbox)}\n"
    for mail in mail_account.inbox:
        return_string += show_mail(mail) + "\n"
    return_string += f"Outbox: {len(mail_account.outbox)}\n"
    for mail in mail_account.outbox:
        return_string += show_mail(mail) + "\n"
    return return_string


def show_mail_server(mail_server: MailServer) -> str:
    return_string = f"Server: {mail_server.domain}\nAccounts: {len(mail_server.accounts)}\n"
    for account in mail_server.accounts:
        return_string += "\n" + show_mail_account(account)
    return return_string


def find_server(servers: list[MailServer], domain: str) -> MailServer | None:
    for server in servers:
        if server.domain == domain:
            return server
    return None


def deliver_mail(mail: Mail, servers: list[MailServer]) -> bool:
    server = find_server(servers, mail.receiver.domain)
    if server is None:
        return False
    for account in server.accounts:
        if account.name == mail.receiver.name:
            account.inbox.append(mail)
            return True
    return False


def deliver_all_mail(servers: list[MailServer]) -> None:
    for server in servers:
        for account in server.accounts:
            for mail in account.outbox:
                if mail.sender.name == account.name and mail.sender.domain == server.domain:
                    if deliver_mail(mail, servers):
                        account.outbox.remove(mail)
