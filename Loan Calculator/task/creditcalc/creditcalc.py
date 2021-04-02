import math
import argparse
import sys


def calc_periods(principal, payment, interest):
    interest /= 100
    nom_interest = interest / 12
    periods = math.ceil(math.log(payment / (payment - (nom_interest * principal)), 1 + nom_interest))

    years = periods // 12
    months = periods % 12
    print('It will take', end=' ')
    if years:
        print(years, 'year' if years == 1 else 'years', end=' ')
    if months:
        print('and', months, 'month' if months == 1 else 'months', end=' ')
    print('to repay this loan!')
    print('Overpayment =', int(periods * payment - principal))


def calc_payment_amount(principal, periods, interest):
    interest /= 100
    nom_interest = interest / 12

    top = (nom_interest * pow(1 + nom_interest, periods))
    bottom = pow(1 + nom_interest, periods) - 1

    payment = int(math.ceil(principal * (top / bottom)))
    print(f'Your annuity payment = {payment}!')
    print('Overpayment =', int(periods * payment - principal))


def calc_principal(annuity_payment, periods, interest):
    interest /= 100
    nom_interest = interest / 12

    top = nom_interest * pow(1 + nom_interest, periods)
    bottom = pow(1 + nom_interest, periods) - 1
    full_bottom = top / bottom
    principal = int(annuity_payment / full_bottom)
    print(f'Your loan principal = {principal}!')
    print('Overpayment =', int(periods * annuity_payment - principal))


def calc_diff_payments(interest, periods, principal):
    interest /= 100
    nom_interest = interest / 12

    total_payment = 0
    for m in range(1, periods + 1):
        payment = math.ceil(principal / periods + nom_interest * (principal - (principal * (m - 1) / periods)))
        total_payment += payment
        print(f"Month {m}: payment is {int(payment)}")

    print('Overpayment =', int(total_payment - principal))


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
args = parser.parse_args()

all_positive = True
for i in range(1, len(sys.argv)):
    breakup = sys.argv[i].split('=')
    if breakup[0] != '--type':
        if float(breakup[1]) < 0:
            all_positive = False
            break

if (args.type != "annuity" and args.type != "diff") \
        or (args.type == "diff" and "--payment" in sys.argv) \
        or args.interest is None \
        or len(sys.argv) < 5 \
        or not all_positive:
    print("Incorrect parameters")
elif args.type == "diff":
    calc_diff_payments(float(args.interest), int(args.periods), float(args.principal))
elif args.periods is None:
    calc_periods(float(args.principal), float(args.payment), float(args.interest))
elif args.payment is None:
    calc_payment_amount(float(args.principal), int(args.periods), float(args.interest))
elif args.principal is None:
    calc_principal(float(args.payment), int(args.periods), float(args.interest))
