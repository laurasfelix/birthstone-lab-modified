from datetime import datetime
import holidays


def sparse(stringy):
    datey = datetime.strptime(stringy,"%m/%d/%Y")
    match datey.month:
        case 1:
            return("coal", "You were born in January. Figure it out.")
        case 2:
            return("coal", "You were born in Febuary. Figure it out.")
        case 3:
            return("coal", "You were born in March. Figure it out.")
        case 4:
            return("coal", "You were born in April. Figure it out.")
        case 5:
            return("coal", "You were born in May. Figure it out.")
        case 6:
            return("coal", "You were born in June. Figure it out.")
        case 7:
            return("ruby", "You were born in July. Yours is a Ruby.")
        case 8:
            return("coal", "You were born in August. Figure it out.")
        case 9:
            return("coal", "You were born in September. Figure it out.")
        case 10:
            return("coal", "You were born in October. Figure it out.")
        case 11:
            return("coal", "You were born in November. Figure it out.")
        case 12:
            if datey.day== 16:
                return("emerald", "You're my girlfriend.")
            return("coal", "You were born in December. Figure it out.")
        

def holy(country, stringy):
    match country:
        case "Japan":
            return holidays.Japan.get(stringy)
        case "United Kingdom":
            return holidays.UnitedKingdom.get(stringy)
        case "United States":
            return holidays.UnitedStates.get(stringy)
        case "Canada":
            return holidays.Canada.get(stringy)
        case "France":
            return holidays.France.get(stringy)
        case "Spain":
            return holidays.Spain.get(stringy)
        case "Mexico":
            return holidays.Mexico.get(stringy)
        case "Italy":
            return holidays.Italy.get(stringy)
        
