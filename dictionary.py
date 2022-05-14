# Dictionary is like a key value pairs
# Jan -> January
# Feb -> February

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    1: "January"
}

print(monthConversions["Apr"])
print(monthConversions.get("Aug"))
print(monthConversions.get(1))

