import numpy as np


# ===== Trade Costs ======

def transaction_cost(h):
    pass # TODO: bid ask spread

# porportional trade cost
def per_trd_cost(h_delta, c_trd, z=None):

    cost = 0
    if z is not None:
        for z_i in z:
            cost += c_trd * z_i
    else:
        for i in range(len(h_delta)):
            cost += c_trd * (h_delta[i] != 0)
    return cost
    # return sum(h > 0) * c_trd


def min_trd_sz(h, u_min):
    return sum(h[h > 0] <= u_min) * float("inf")

def tax_liability(h, L):
    pass


# ===== Hold Costs ======

def pre_security_holding_costs(h, c_hld, z=None):
    cost = 0
    if z is not None:
        for z_i in z:
            cost += c_hld*z_i
    else:
        for i in h:
            cost += c_hld * (i != 0)
    return cost

def position_limits(h):
    pass

# given min holding values and a holding cost
# returns associate holding cost

# hold cost porportional
def min_hld_sz(h, h_min, c_hld, z=None):
    pass
    # cost = 0
    # max = -1
    # for i in range(len(h)):
    #     if h[i] > max:
    #
    # for i in range(len(h)):
    #     # if h[i] != 0 and h[i] < h_min[i]:
    #     #     cost += c_hld
    #     cost += c_hld * h[i]


    return cost

def int_share_constr(h):
    pass
