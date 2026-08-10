bs_months = ["Baisakh", "Jestha", "Ashadh", "Shrawan", "Bhadra", "Ashwin",
             "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]
 
ad_months = ["January", "February", "March", "April", "May", "June",
             "July", "August", "September", "October", "November", "December"]
 
 
def ordinal(day):
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    return f"{day}{suffix}"
 
 
def convert_date(date_str, from_cal, to_cal, style="iso"):
    year, month, day = (int(x) for x in date_str.split("-"))
 
    if from_cal != to_cal:
        year += 56 if from_cal == "AD" else -56
 
    if style == "iso":
        return f"{year:04d}-{month:02d}-{day:02d} {to_cal}"
 
    months = bs_months if to_cal == "BS" else ad_months
    return f"{ordinal(day)} {months[month - 1]}, {year} {to_cal}"
 
 
customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"},
]
 
print()
print("=" * 50)
print("Question 3 - Date Converter for Nepal Bank System (BS <-> AD)")
print("=" * 50)
for c in customers:
    converted = convert_date(c["date"], c["cal"], c["need"], c["style"])
    print(f"{c['name']:14}| Original: {c['date']} {c['cal']} | Converted: {converted}")