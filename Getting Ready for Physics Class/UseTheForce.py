train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# force calculation
def get_force(mass, acceleration):
    force = mass * acceleration
    print("A GE train supplies " + f'{force:,}' + " Newtons(N) of force.")
    return force

get_force(train_mass, train_acceleration)

# energy equivalence calculation
def get_energy(mass):
    c = 2.99792458*10**8
    energy = mass * c**2
    print("A " + str(bomb_mass) +"kg bomb creates " + f'{energy:,}' + " Joules.")
    return energy

get_energy(bomb_mass)

# work-force calculation
def get_work(mass, acceleration, distance):
    work = get_force(mass, acceleration) * distance
    print("The GE train does " + f'{work:,}' + " Joules of work over " + str(distance) + " meters.")
    return work

get_work(train_mass, train_acceleration, train_distance)