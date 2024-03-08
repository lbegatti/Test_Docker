##############################################################################
# ATM cap valuation under Vasicek short-rate framework.
##############################################################################
import numpy as np
from scipy import optimize
from scipy.stats import norm

# k = 0.86
# theta = 0.09
# sigma = 0.0148
# r_0 = 0.08
# delta = 0.25

while True:

    k = float(input('Input k: '))
    theta = float(input('Insert the value of theta: '))
    sigma = float(input('Insert the value of sigma: '))
    r_0 = float(input('Input the risk free rate at time 0: '))
    delta = float(input('Input timesteps delta: '))
    gamma = np.sqrt(k ** 2 + 2 * (sigma ** 2))

    periods = []

    for i in range(0, 120):
        periods.append((i + 1) / 4)

    # these are the A and B for the computation of the zcb price in VASICEK setting --> Riccati equations
    AA = []
    B = []

    for i in range(0, len(periods)):
        B.append((1 - np.exp(-k * periods[i])) / k)
        AA.append(
            (theta - ((sigma ** 2) / (2 * (k ** 2)))) * (B[i] - periods[i]) - (((sigma ** 2) * (B[i] ** 2)) / (4 * k)))

    # these are the discount factors
    P = []
    for i in range(0, len(periods)):
        P.append(np.exp(AA[i] - (B[i] * r_0)))

    # now we get the strike rates

    def atmswap(years):

        return (P[0] - P[years - 1]) / (delta * sum([P[i] for i in range(1, years)]))


    # strike rate
    strike_rate = atmswap(120)

    # caplet prices
    caplets = []


    def caplet(strike_caplet, period_index):

        return (1 + (delta * strike_caplet)) * max(((1 / (1 + (delta * strike_caplet))) - P[period_index]), 0)


    def cap(strike, years):

        return sum([caplet(strike, period_index) for period_index in range(1, years)])


    print(f'\nThe price of the cap is: {round(cap(strike=strike_rate, years=120), 2)}')

    continue_pricing = input('\nDo you to enter other values? (y/n)')

    if continue_pricing != 'y':
        break
