# Exercise was to fix file with a bug causing this error
# Traceback (most recent call last):
#  File "sears.py", line 10, in <module>
#    day = days + 1
# NameError: name 'days' is not defined

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
days            = 1

while num_bills * bill_thickness < sears_height:
    print(days, num_bills, num_bills * bill_thickness)
    days = days + 1
    num_bills = num_bills * 2

print('Number of days', days)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)

# Fixed by adding an 's' to day to ensure the variable name was consistent
