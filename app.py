from cars import Car, Truck


if __name__ == "__main__":
    car = Car("Honda", 200, "yellow", "2020")
    car.get_color()
    car.get_company()
    car.get_speed()
    car.get_year()

    truck = Truck("Yamaha", 240, "Green", "2018")
    print("Speed of truct is:")
    truck.get_speed()