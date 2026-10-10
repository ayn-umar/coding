# Daily Routine Flowchart Simulator (Pure Python - No installation needed)

print("┌─────────────────────────┐")
print("│       START: Wake Up    │")
print("└────────────┬────────────┘")
print("             │")
print("             ▼")
print("┌─────────────────────────┐")
print("│ Brush Teeth & Breakfast │")
print("└────────────┬────────────┘")
print("             │")
print("             ▼")

# Decision variable: Change this to False if it's the weekend!
is_weekday = True 

print("┌─────────────────────────┐")
print("│    Is it a Weekday?     │")
print("└────────────┬────────────┘")

# Decision logic (equivalent to the diamond shape in a flowchart)
if is_weekday:
    print("             │ [YES]")
    print("             ▼")
    print("┌─────────────────────────┐")
    print("│   Go to School / Work   │")
    print("└────────────┬────────────┘")
else:
    print("             │ [NO]")
    print("             ▼")
    print("┌─────────────────────────┐")
    print("│   Relax & Enjoy Hobbies │")
    print("└────────────┬────────────┘")

print("             │")
print("             ▼")
print("┌─────────────────────────┐")
print("│    END: Ready for Day   │")
print("└─────────────────────────┘")