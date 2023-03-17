def water_state(temperature):
    if int(temperature) >= 212:
        return "Gas"
    elif int(temperature) > 32:
        return "Liquid"
    else:
        return "Solid"
