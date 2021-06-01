from utils import Portfolio
from config import config
import numpy as np



def linear_solver():
    portfolio = Portfolio(config)
    portfolio.init_linear_solver()
    portfolio.optimize()

def eval_LP():
    rand = 0
    lp = 0
    for i in range(100):
        portfolio = Portfolio(config)

        # random solution
        h = np.random.rand(10)
        h = h / float(sum(h))
        rand += portfolio.evaluate_construction(h)/float(100)

        portfolio.init_linear_solver()
        lp += portfolio.optimize()/100.

    print("Average Returns\n")
    print("Random Policy: ", round(rand, 3), "%")
    print("LP Policy: ", round(lp,3), "%" )



def test():
    portfolio = Portfolio(config)

    print("Alpha")
    print(portfolio.alpha)

    h = np.random.rand(10)
    h = h / float(sum(h)) # normalize h

    print("Eval objective and bounds")
    print(portfolio.evaluate_construction(h))
    print(portfolio.evaluate_lb(h))
    print(portfolio.evaluate_ub(h))

    val = 0
    for i in range(100):
        h = np.random.rand(10)
        h = h / float(sum(h))
        val += portfolio.evaluate_construction(h)/float(100)
    print("Trials", val)


if __name__ == "__main__":
    print("Testing Library")
    # test()
    # linear_solver()
    eval_LP()
