import datetime


def sparse(stringy):
    datey = datetime.strptime(stringy)
    match datey.month:
        case 1:
            return("You were born in January. Figure it out.")
        case 2:
            return("You were born in Febuary. Figure it out.")
        case 3:
            return("You were born in March. Figure it out.")
        case 4:
            return("You were born in April. Figure it out.")
        case 5:
            return("You were born in May. Figure it out.")
        case 6:
            return("You were born in June. Figure it out.")
        case 7:
            return("You were born in July. Figure it out.")
        case 8:
            return("You were born in August. Figure it out.")
        case 9:
            return("You were born in September. Figure it out.")
        case 10:
            return("You were born in October. Figure it out.")
        case 11:
            return("You were born in November. Figure it out.")
        case 12:
            return("You were born in December. Figure it out.")
