# Create a new class of residents and print out two of the residents data in the console
class Resident:
    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day, status, cpr, diagnosis):
        self._first_name    = first_name
        self._last_name     = last_name
        self._birth_year    = birth_year
        self._birth_month   = birth_month
        self._birth_day     = birth_day
        self._status        = status
        self._cpr           = cpr
        self._diagnosis     = diagnosis

    def __str__(self):
        return (f"{self._first_name} {self._last_name} \n"
                f"- Status: {self._status}\n"
                f"- Diagnosis: {self._diagnosis}")

    def dischargeResident(self):
        self._status = "discharged"

# create a new resident named 'Jane Done', who was born on March 3, 1980, status of 'current_resident' and 'CPR' status
resident1 = Resident("Jane", "Doe",
                    1980, 3, 25,
                    "current_resident", "CPR", "High blood pressure")

# create a new resident named 'Julius Caesar', who was born on July 12, 100 BC, status of 'discharged'  and 'DNR' status
resident2 = Resident("Julius", "Caesar",
                    100, 7, 12,
                    "discharged", "DNR", "Very afraid of knives")

# create list of all residents
residents = [resident1, resident2]

### Print list of all residents
print("##############################")
print("All Residents")
print("")
for resident in residents:
    print(resident)
    print("")

### Printing individual residents manually
print("")
print("##############################")
print("Printing Residents Manually")
print("")

# Print Jane Doe's data
print(resident1)
print("")

# Print Julius Caesar's data
print(resident2)

#### Discharge the first resident
print("")
print("##############################")
print("Discharging resident1...")
residents[0].dischargeResident()
print("Finished...")

### Print list of all residents
print("")
print("##############################")
print("All Residents")
print("")
for resident in residents:
    print(resident)
    print("")

### Output ###
#
#
# Jane Doe
# - Diagnosis: High blood pressure
#
# Julius Caesar
# - Diagnosis: Very afraid of knives
#