pkg_weight = 0.0
ship_method = "none chosen"
ship_method_cheapest = "undecided"
lb_price = 0.0
ship_cost_premium = 125.00
ship_cost_drone = 0.0
ship_cost_ground = 0.0

# Ship-by-Ground
def ship_ground(pkg_weight, flat_charge = 20.00):
  global lb_price
  global ship_cost_ground
  if pkg_weight > 10:
    lb_price = 4.75
  elif pkg_weight > 6 and pkg_weight <= 10:
    lb_price = 4.00
  elif pkg_weight > 2 and pkg_weight <= 6:
    lb_price = 3.00
  elif pkg_weight <= 2:
    lb_price = 1.50

  ship_cost_ground = (pkg_weight * lb_price) + flat_charge
  print("Ground Shipping cost: $" + f'{ship_cost_ground:.2f}')
  return ship_cost_ground 

# ship_ground(pkg_weight)

# Ship-by-Drone
def ship_drone(pkg_weight, flat_charge = 0.00):
  global lb_price
  global ship_cost_drone
  if pkg_weight > 10:
    lb_price = 14.25
  elif pkg_weight > 6 and pkg_weight <= 10:
    lb_price = 12.00
  elif pkg_weight > 2 and pkg_weight <= 6:
    lb_price = 9.00
  elif pkg_weight <= 2:
    lb_price = 4.50

  ship_cost_drone = (pkg_weight * lb_price) + flat_charge
  print("Drone Shipping cost: $" + f'{ship_cost_drone:.2f}')
  return ship_cost_drone
  
# ship_drone(pkg_weight)

# determine cheapest shipping method
def ship_it_cheaper(ship_cost_drone, ship_cost_ground, ship_cost_premium):
  if ship_cost_drone < ship_cost_ground and ship_cost_drone < ship_cost_premium:
    ship_cost = ship_cost_drone
    print("At $" + f'{ship_cost_drone:.2f}' + " Drone Shipping is cheaper!")
  if ship_cost_ground < ship_cost_drone and ship_cost_ground < ship_cost_premium:
    ship_cost = ship_cost_ground
    print("At $" + f'{ship_cost_ground:.2f}' + " Ground Shipping is cheaper!")
  if ship_cost_premium < ship_cost_drone and ship_cost_premium < ship_cost_ground:
    ship_cost = ship_cost_ground
    print("At $" + f'{ship_cost_premium:.2f}' + " Premium Shipping is cheaper!")

# ship_it_cheaper(ship_cost_drone, ship_cost_ground, ship_cost_premium)

# # User Inputs
def ask_user():
  print("How heavy is your package?")
  weight = input("Please enter your weight in pounds: ")
  pkg_weight = float(weight)
  print("\n")

  ship_ground(pkg_weight)
  ship_drone(pkg_weight)
  ship_it_cheaper(ship_cost_drone, ship_cost_ground, ship_cost_premium)

ask_user()
