# There are 100 cars
cars = 100

# A car holds 4 people
space_in_a_car = 4

# There are 30 drivers
drivers = 30

# There are 90 passengers
passengers = 90

# The number of "cars not driven" is calculated by subtracting the number of 
# drivers from cars
cars_not_driven = cars - drivers

# The number of cars driven equals the number of drivers
cars_driven = drivers

# The "carpool capacity" is calculated by multiplying the number of cars driven
# and the amount of space in a car
carpool_capacity = cars_driven * space_in_a_car

# The average number of passengers per car is calculated by dividing the number
# of passengers by the number of cars driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."