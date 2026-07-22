"""
King's Library Management System
---------------------------------
A simple menu-driven program using basic Python:
lists, dictionaries, for loops, while loops, and if/else.

Features:
1. Display available books
2. Show borrowed books
3. Add new books
4. Keep records of students
5. Return reminder
6. Fine calculation for late submission
7. Charge calculation (total fine to pay)
8. Exit
"""
import os

books = []
students = []
borrow_records = []

FINE_PER_DAY = 100
DUE_PERIOD = 14
current_day = 0

book_id_counter = 1
student_id_counter = 1


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def _find(seq, key, value):
    return next((x for x in seq if x.get(key) == value), None)


def add_book():
    global book_id_counter
    print()
    title = input("Enter book title: ")
    books.append({"id": book_id_counter, "title": title, "available": True})
    print(f"Added '{title}' (ID {book_id_counter})")
    book_id_counter += 1
    input("\nPress Enter to continue...")


def display_available_books():
    print()
    print("=== AVAILABLE BOOKS ===")
    avail = [b for b in books if b["available"]]
    if not avail:
        print("No books available right now.")
    else:
        for b in avail:
            print(f"ID: {b['id']} | {b['title']}")


def display_borrowed_books():
    print()
    print("=== BORROWED BOOKS ===")
    recs = [r for r in borrow_records if not r["returned"]]
    if not recs:
        print("No books are currently borrowed.")
    else:
        for r in recs:
            b = _find(books, "id", r["book_id"]) or {"title": "Unknown"}
            print(f"{b['title']} | Student {r['student_id']} | Borrowed: {r['borrow_day']} | Due: {r['due_day']}")


def add_student():
    global student_id_counter
    print()
    name = input("Enter student name: ")
    students.append({"id": student_id_counter, "name": name})
    print(f"Added student '{name}' (ID {student_id_counter})")
    student_id_counter += 1
    input("\nPress Enter to continue...")


def display_students():
    print()
    print("=== STUDENT RECORDS ===")
    if not students:
        print("No students registered yet.")
    else:
        for s in students:
            print(f"ID: {s['id']} | {s['name']}")


def borrow_book():
    print()
    print("=== BORROW A BOOK ===")
    print()
    display_students()
    try:
        sid = int(input("Enter Student ID: "))
        display_available_books()
        bid = int(input("Enter Book ID to borrow: "))
        b = _find(books, "id", bid)
        if b and b["available"]:
            b["available"] = False
            borrow_records.append({
                "student_id": sid,
                "book_id": bid,
                "borrow_day": current_day,
                "due_day": current_day + DUE_PERIOD,
                "returned": False,
            })
            print("\n[SUCCESS] Book borrowed successfully!")
            print(f"  - Student ID: {sid}")
            print(f"  - Book ID: {bid}")
            print(f"  - Borrowed on: Day {current_day}")
            print(f"  - Due Date: Day {current_day + DUE_PERIOD}")
        else:
            print("\n[ERROR] Book not available or does not exist.")
    except ValueError:
        print("\n[ERROR] Please enter valid numbers!")
    input("\nPress Enter to continue...")


def return_book():
    print()
    print("=== RETURN A BOOK ===")
    print()
    display_borrowed_books()
    try:
        bid = int(input("Enter Book ID being returned: "))
        r = _find(borrow_records, "book_id", bid)
        if r and not r["returned"]:
            r["returned"] = True
            b = _find(books, "id", bid)
            if b:
                b["available"] = True
            late = current_day - r["due_day"]
            print("\n[SUCCESS] Book returned successfully!")
            if late > 0:
                fine = late * FINE_PER_DAY
                print(f"  [WARNING] Book was {late} day(s) late")
                print(f"  [FINE] ₹{fine} to pay")
            else:
                print("  [OK] Returned on time. No fine!")
        else:
            print("\n[ERROR] No matching borrowed record found.")
    except ValueError:
        print("\n[ERROR] Please enter a valid number!")
    input("\nPress Enter to continue...")


def return_reminder():
    print()
    print("=== RETURN REMINDERS ===")
    print(f"Current Day: {current_day}")
    print("-" * 50)
    recs = [r for r in borrow_records if not r["returned"]]
    msgs = []
    for r in recs:
        days_left = r["due_day"] - current_day
        b = _find(books, "id", r["book_id"]) or {"title": "Unknown"}
        if days_left <= 3:
            if days_left >= 0:
                msgs.append(f"[DUE SOON] '{b['title']}' (Student {r['student_id']}) - Due in {days_left} day(s)")
            else:
                msgs.append(f"[OVERDUE!] '{b['title']}' (Student {r['student_id']}) - {-days_left} day(s) LATE!")
    if not msgs:
        print("[OK] No reminders. All books on track!")
    else:
        print()
        print("\n".join(msgs))
    input("\nPress Enter to continue...")


def fine_calculation():
    print()
    print("=== FINE CALCULATION ===")
    print(f"Current Day: {current_day}")
    print("-" * 50)
    recs = [r for r in borrow_records if not r["returned"]]
    lines = []
    total_fines = 0
    for r in recs:
        late = current_day - r["due_day"]
        if late > 0:
            fine = late * FINE_PER_DAY
            lines.append(f"  Student {r['student_id']} | Book {r['book_id']} | Late {late} days | Fine: ₹{fine}")
            total_fines += fine
    if not lines:
        print("[OK] No fines at the moment.")
    else:
        print()
        print("\n".join(lines))
        print("-" * 50)
        print(f"[TOTAL FINES] ₹{total_fines}")
    input("\nPress Enter to continue...")


def charge_calculation():
    print()
    print("=== TOTAL CHARGE PER STUDENT ===")
    print(f"Current Day: {current_day}")
    print("-" * 50)
    totals = {}
    for r in borrow_records:
        if r["returned"]:
            continue
        late = current_day - r["due_day"]
        if late > 0:
            totals[r["student_id"]] = totals.get(r["student_id"], 0) + late * FINE_PER_DAY
    if not totals:
        print("[OK] No outstanding charges.")
    else:
        print()
        grand_total = 0
        for sid, amt in sorted(totals.items()):
            print(f"  Student ID {sid}: ₹{amt}")
            grand_total += amt
        print("-" * 50)
        print(f"[GRAND TOTAL] ₹{grand_total}")
    input("\nPress Enter to continue...")


def advance_day():
    global current_day
    print()
    print("=== ADVANCE TIME ===")
    print(f"Current day: {current_day}")
    print()
    try:
        days = int(input("How many days to move forward? "))
        if days > 0:
            old_day = current_day
            current_day += days
            print(f"\n[SUCCESS] Time advanced!")
            print(f"  - Previous day: {old_day}")
            print(f"  - Current day: {current_day}")
        elif days == 0:
            print("\n[INFO] No time passed.")
        else:
            print("\n[ERROR] Please enter a positive number!")
    except ValueError:
        print("\n[ERROR] Please enter a valid number!")
    input("\nPress Enter to continue...")


def main():
    print("Welcome to the King's Library Management System!")

    running = True
    while running:
        clear_screen()
        print("\n" + "="*50)
        print("MAIN MENU")
        print("="*50)
        print("\n[VIEW & RECORDS]")
        print("1. Display available books")
        print("2. Show borrowed books")
        print("3. Show student records")
        print("\n[ADD NEW]")
        print("4. Add new book")
        print("5. Add new student")
        print("\n[BORROW & RETURN]")
        print("6. Borrow a book")
        print("7. Return a book")
        print("\n[REPORTS & CALCULATIONS]")
        print("8. Return reminders")
        print("9. Fine calculation")
        print("10. Charge calculation (per student)")
        print("\n[SYSTEM]")
        print("11. Advance day (simulate time passing)")
        print("12. Exit")
        print("="*50)
        choice = input("\nEnter your choice (1-12): ")

        if choice == "1":
            display_available_books()
            input("\nPress Enter to continue...")
        elif choice == "2":
            display_borrowed_books()
            input("\nPress Enter to continue...")
        elif choice == "3":
            display_students()
            input("\nPress Enter to continue...")
        elif choice == "4":
            add_book()
        elif choice == "5":
            add_student()
        elif choice == "6":
            borrow_book()
        elif choice == "7":
            return_book()
        elif choice == "8":
            return_reminder()
        elif choice == "9":
            fine_calculation()
        elif choice == "10":
            charge_calculation()
        elif choice == "11":
            advance_day()
        elif choice == "12":
            print("Goodbye!")
            running = False
        else:
            print("\nInvalid choice, please try again.\n")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()