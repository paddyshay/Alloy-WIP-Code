while True:
    First_Name = input("First Name: " )
    if First_Name:
        None
        break
    else:
        print("Please enter First Name.")

while True:
    Last_Name = input("Last Name: ")
    if Last_Name:
        None
        break
    else:
        print("Please enter Last Name.")

while True:
    Street_Address = input("Street Address: " )
    if Street_Address:
        None
        break
    else:
        print("Please enter Street Address.")

while True:
    City_Address = input("City Address: " )
    if City_Address:
        None
        break
    else:
        print("Please enter City.")

Allowed_States = {
    "AL": "",
    "AK": "",
    "AZ": "",
    "AR": "",
    "CA": "",
    "CO": "",
    "CT": "",
    "DE": "",
    "DC": "",
    "FL": "",
    "GA": "",
    "GU": "",
    "HI": "",
    "ID": "",
    "IL": "",
    "IN": "",
    "IA": "",
    "KS": "",
    "KY": "",
    "LA": "",
    "ME": "",
    "MD": "",
    "MA": "",
    "MI": "",
    "MN": "",
    "MS": "",
    "MO": "",
    "MT": "",
    "NE": "",
    "NV": "",
    "NH": "",
    "NJ": "",
    "NM": "",
    "NY": "",
    "NC": "",
    "ND": "",
    "OH": "",
    "OK": "",
    "OR": "",
    "PA": "",
    "RI": "",
    "SC": "",
    "SD": "",
    "TN": "",
    "TX": "",
    "UT": "",
    "VT": "",
    "VA": "",
    "WA": "",
    "WV": "",
    "WI": "",
    "WY": "",
}

while True:
    State_Address = input("State (Abbreviated): ")

    if State_Address in Allowed_States.keys():
        print(Allowed_States[State_Address])
        break

    print("Please input a valid State in abbreviated format.")

def get_int():
    Zip_Address = input("Zip Code: ")
    if Zip_Address == 'q':
        return None
    try:
        user_num = int(Zip_Address)
        return user_num
    except ValueError:
        print("Please input valid US Zip Code.")
        return(get_int())

user_number = get_int()

Allowed_Countries = {
    "US": "",
}

while True:
    Country_Address = input("Country: ")

    if Country_Address in Allowed_Countries.keys():
        print(Allowed_Countries[Country_Address])
        break

    print("Please input a valid country code.")

def get_int():
    SocSecNum = input("Social Security Number: ")
    if SocSecNum == 'q':
        return None
    try:
        user_num = int(SocSecNum)
        return user_num
    except ValueError:
        print("Value input must be 9 digits and numeric only.")
        return(get_int())

user_number = get_int()

while True:
    Email_Address = input("Email Address: " )
    if Email_Address:
        None
        break
    else:
        print("Please enter Email Address.")

DOB = input("Date of Birth YYYY-MM-DD: " )