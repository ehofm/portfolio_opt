
import numpy as np
from cost_functions import *
import gurobipy as gp
from gurobipy import Model, quicksum, LinExpr, GRB
from copy import deepcopy
class Portfolio:

    def __init__(self, config):
        self.n = config["n"]
        self.alpha = config["alpha"]
        self.gamma_risk = config["gamma_risk"]
        self.gamma_trade = config["gamma_trade"]
        self.gamma_hold = config["gamma_hold"]
        self.eta_lb = config["eta_lb"]
        self.eta_ub = config["eta_ub"]
        self.h_init = config["h_init"]

        self.c_hld = config["c_hld"]
        self.c_trd = config["c_trd"]
        self.h_min = config["h_min"]

        self.V = self.init_V(self.n)
        self.z_trd = None
        self.z_hld = None
        self.h_var = None


    def init_V(self, n):
        return np.zeros((n,n))

    def asset_return(self, h):

        ret = 0
        for i in range(self.n):
            if self.h_var is not None:
                ret += self.h_var[i] * self.alpha[i]
            else:
                ret += h[i] * self.alpha[i]
        return ret

    # defines the
    def evaluate_construction(self, h):
        check = len(h)
        assert(check == self.n)

        asset_ret = self.asset_return(h)
        risk_cost = 0 #self.gamma_risk *  np.outer(h, h) # took off float

        delta = []
        for i in range(self.n):
            delta.append( self.h_init[i] - h[i])
        trd_cost = self.gamma_trade * self.trade_cost(delta)
        hld_cost = self.gamma_hold * self.hold_cost(h)

        total_cost = asset_ret - risk_cost - trd_cost - hld_cost

        return  total_cost

    def init_linear_solver(self):
        self.lin_m = Model()
        self.lin_m.setParam('OutputFlag', False)
        self.h_var = self.lin_m.addVars(self.n)
        self.z_trd = self.lin_m.addVars(self.n)
        self.z_hld = self.lin_m.addVars(self.n)

        for i in range(self.n):
            self.lin_m.addGenConstrIndicator(self.z_trd[i], False, (self.h_init[i] - self.h_var[i]) == 0)
            self.lin_m.addGenConstrIndicator(self.z_hld[i], False, self.h_var[i] == 0)

        self.lin_m.addConstr(self.h_var.sum() <= self.eta_ub)
        self.lin_m.addConstr(self.eta_lb <= self.h_var.sum())

        # self.lin_m.addConstr(self.h_var[0] + self.h_var[1] <= 1)
        self.lin_m.addConstr(self.h_var.sum() <= self.eta_ub)


        self.lin_m.setObjective(self.evaluate_construction(self.h_var), GRB.MAXIMIZE)

    def optimize(self):
        self.lin_m.optimize()
        # print("found", self.h_var[0].x)
        # print("FOUND")
        # for i in range(self.n):
        #     print(i, " : ", self.h_var[i].x)
        # print('Obj: %g' % self.lin_m.objVal)
        return self.lin_m.objVal
    def evaluate_lb(self, h):
        check = len(h)
        assert(check == self.n)

        return (self.eta_lb <= sum(h))

    def evaluate_ub(self, h):
        check = len(h)
        assert(check == self.n)
        return (sum(h) <= self.eta_ub)

    def trade_cost(self, h, type="default"):
        check = len(h)
        assert(check == self.n)

        if type == "default":
            return per_trd_cost(h, self.c_trd, self.z_trd)


    def hold_cost(self, h, type="default"):
        check = len(h)
        assert(check == self.n)

        if type == "default":
            return pre_security_holding_costs(h, self.c_hld, self.z_hld)
