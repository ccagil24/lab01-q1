def convert_temperature(temp,unit):
    if unit == "C":
        return round((9 * temp) / 5 + 32 , 2)
    elif unit == "F":
        return round ((temp - 32) * 5 / 9, 2)
    else:
        return None
    #convertion