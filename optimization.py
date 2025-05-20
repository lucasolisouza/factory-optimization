"""
Production Optimization using Linear Programming

Author: [Lucas Barbosa]
GitHub: [https://github.com/lucasolisouza]
Last Modified: [2025-05-07]

This script implements a production optimization model using Linear Programming
to maximize profit given resource constraints.
"""

from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value

def optimize_production(profit_a, profit_b, machine_time, raw_material):
    """
    Optimizes production quantities for two products using Linear Programming.
    
    Args:
        profit_a (float): Profit per unit of Product A
        profit_b (float): Profit per unit of Product B
        machine_time (float): Total available machine hours
        raw_material (float): Total available raw material in kg
        
    Returns:
        dict: Optimization results containing:
            - status: Solution status
            - product_a: Optimal quantity of Product A
            - product_b: Optimal quantity of Product B
            - max_profit: Maximum achievable profit
    """
    
    # Initialize the optimization problem
    prob = LpProblem("Production_Optimization", LpMaximize)
    
    # Define decision variables (must be non-negative integers)
    product_a = LpVariable('Product_A', lowBound=0, cat='Integer')
    product_b = LpVariable('Product_B', lowBound=0, cat='Integer')
    
    # Set objective function: Maximize total profit
    prob += profit_a * product_a + profit_b * product_b, "Total_Profit"
    
    # Add constraints
    # Machine time constraint: 2h per Product A + 1h per Product B
    prob += 2 * product_a + 1 * product_b <= machine_time, "Machine_Time_Constraint"
    
    # Raw material constraint: 3kg per Product A + 2kg per Product B
    prob += 3 * product_a + 2 * product_b <= raw_material, "Raw_Material_Constraint"
    
    # Solve the optimization problem
    prob.solve()
    
    # Return results in a structured dictionary
    return {
        "status": LpStatus[prob.status],
        "product_a": product_a.varValue,
        "product_b": product_b.varValue,
        "max_profit": value(prob.objective)
    }


# Example usage:
if __name__ == "__main__":
    results = optimize_production(
        profit_a=40,
        profit_b=30,
        machine_time=100,
        raw_material=120
    )
    print("Optimization Results:")
    print(f"Status: {results['status']}")
    print(f"Product A: {results['product_a']} units")
    print(f"Product B: {results['product_b']} units")
    print(f"Maximum Profit: R$ {results['max_profit']}")