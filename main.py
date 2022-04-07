import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-tp", "--type")
parser.add_argument("-pcp", "--principal")
parser.add_argument("-prd", "--periods")
parser.add_argument("-int", "--interest")
parser.add_argument("-pay", "--payment")

args = parser.parse_args()
arguments = [args.type, args.principal, args.periods, args.interest, args.payment]

S = 0

if args.type == "diff":
    if args.payment is not None or float(arguments[1]) < 0 or float(arguments[2]) < 0 or float(arguments[3]) < 0 \
            or args.principal is None or args.periods is None or args.interest is None:
        print("Incorrect parameters")

    else:
        for i in range(1, int(args.periods) + 1, 1):

            inter = float(args.interest) / (12 * 100)
            D = (float(args.principal) / float(args.periods)) + inter * (
                    float(args.principal) - (float(args.principal) * (i - 1) / float(args.periods)))
            print("Month {}: payment is {}".format(i, math.ceil(D)))
            S += math.ceil(D)
        overpay = math.ceil(S - int(args.principal))
        print("Overpayment = {}".format(overpay))

elif args.type == "annuity":
    if args.principal and args.periods and args.interest is not None or args.principal \
            and args.interest and args.payment is not None or args.principal and args.periods \
            and args.payment is not None or args.periods and args.interest and args.payment is not None:

        if args.principal is None and float(arguments[2]) > 0 and float(arguments[3]) > 0 and float(arguments[4]) > 0:

            inter = float(args.interest) / (12 * 100)
            principal = math.floor(float(args.payment) / ((inter * math.pow(1 + inter, int(args.periods)))
                                                          / (math.pow(1 + inter, int(args.periods)) - 1)))
            overpay = int(int(args.periods) * float(args.payment) - principal)
            print("Your loan principal = {}!".format(principal))
            print("Overpayment = {}".format(overpay))

        elif args.payment is None and float(arguments[1]) > 0 and float(arguments[2]) > 0 and float(arguments[3]) > 0:

            inter = float(args.interest) / (12 * 100)
            annuity = math.ceil(float(args.principal) * ((inter * math.pow(1 + inter, int(args.periods)))
                                                         / (math.pow(1 + inter, int(args.periods)) - 1)))
            overpay = int(annuity * int(args.periods) - float(args.principal))
            print("our annuity payment = {}!".format(annuity))
            print("Overpayment = {}".format(overpay))

        elif args.periods is None and float(arguments[1]) > 0 and float(arguments[3]) > 0 and float(arguments[4]) > 0:

            inter = float(args.interest) / (12 * 100)
            cycles = math.ceil(math.log(float(args.payment) /
                                        (float(args.payment) - inter * float(args.principal)), 1 + inter))
            years = math.floor(cycles / 12)
            months = cycles - years * 12
            overpay = int(cycles * float(args.payment) - float(args.principal))

            if years != 0:
                if months != 0:
                    print("It will take {} years and {} months to repay this loan!".format(int(years), int(months)))
                    print("Overpayment = {}".format(overpay))
                else:
                    print("It will take {} years to repay this loan!".format(int(years)))
                    print("Overpayment = {}".format(overpay))
            else:
                print("It will take {} months to repay this loan!".format(int(months)))
                print("Overpayment = {}".format(overpay))
    else:
        print("Incorrect parameters")
else:
    print("Incorrect parameters")
