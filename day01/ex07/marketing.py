import sys


def init():

    clients = [
        'andrew@gmail.com', 
        'jessica@gmail.com',
        'ted@mosby.com',
        'john@snow.is',
        'bill_gates@live.com',
        'mark@facebook.com',
        'elon@paypal.com',
        'jessica@gmail.com'
        ]

    participants = [
        'walter@heisenberg.com',
        'vasily@mail.ru',
        'pinkman@yo.org',
        'jessica@gmail.com',
        'elon@paypal.com',
        'pinkman@yo.org',
        'mr@robot.gov',
        'eleven@yahoo.com'
        ]

    recipients = [
        'andrew@gmail.com',
        'jessica@gmail.com',
        'john@snow.is'
        ]

    return clients, participants, recipients


def call_center(clients, participants, recipients):
    return set(clients) - set(recipients)


def potential_clients(participants, clients):
    return set(participants) - set(clients)


def loyalty_program(clients, participants):
    return set(clients) - set(participants)


def marketing():
    clients, participants, recipients = init()
    if len(sys.argv) == 2:
        match sys.argv[1]:
            case "call_center":
                print(*call_center(clients, participants, recipients), sep="\n")
            case "potential_clients":
                print(*potential_clients(participants, clients), sep="\n")
            case "loyalty_program":
                print(*loyalty_program(clients, participants), sep="\n")
            case _:
                raise NameError(f'name {sys.argv[1]} is not defined')


if __name__ == '__main__':
    marketing()