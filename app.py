def main():
    gravitational_constant = 0.000000000066743
    mass_of_sun_kg = 1988470000000000000000000000000.0
    distance_between_earth_and_sun_m = 151480000000.0

    delta_t = 1
    time = 0
    distance_from_sun = distance_between_earth_and_sun_m
    velocity = 0.0

    while distance_from_sun > 0.0:
        acceleration = -1.0 * (gravitational_constant * mass_of_sun_kg) / (distance_from_sun * distance_from_sun)
        delta_v = acceleration * delta_t
        velocity += delta_v
        delta_s = velocity * delta_t
        distance_from_sun += delta_s

        print(f"Time: {time}s,"
              f"acceleration: {acceleration}ms^-2,"
              f"velocity: {velocity}ms^-1,"
              f"distance: {distance_from_sun}m")

        time += delta_t


if __name__ == '__main__':
    main()
