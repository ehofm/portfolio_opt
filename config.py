import numpy as np

# problem set up
n = 10
h_init = np.zeros(n)# init portfolio holdings (should prob be randomized)
alpha = np.array([1 * i for i in range(n)]) #*0.1 # expected returns of each asset (mean) [0.1 reps S&P]

# weights of portfolio cost
gamma_risk = 0.5
gamma_trade = 0.5
gamma_hold = 0.5

# costs
c_hld = 0.01
c_trd = 0.01 # per trade cost

# constraint bounds
eta_lb = 0#.1
eta_ub = 1#.9

h_min = np.zeros(n)

config = {
    "n": n,
    "h_init": h_init,
    "alpha": alpha,
    "gamma_risk": gamma_risk,
    "gamma_trade": gamma_trade,
    "gamma_hold": gamma_hold,
    "eta_lb": eta_lb,
    "eta_ub": eta_ub,
    "c_hld": c_hld,
    "c_trd": c_trd,
    "h_min": h_min
}
