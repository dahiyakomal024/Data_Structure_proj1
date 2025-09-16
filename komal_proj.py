# Weather ADT (procedural)
def make_record(date, city, temperature):
    return {"date": date, "city": city, "temperature": float(temperature)}

# Storage setup and helpers
def create_storage(years, cities):
    rows = len(years)
    cols = len(cities)
    array = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(None)
        array.append(row)
    records = []
    return {"years": list(years),
             "cities": list(cities),
             "array": array,
             "records": records
            }

def index_of(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1

# Insert record
def insert(storage, record):
    storage["records"].append(record)
    r = index_of(storage["years"], record["date"])
    c = index_of(storage["cities"], record["city"])
    if r != -1 and c != -1:
        storage["array"][r][c] = record["temperature"]

# Delete record by city and date (first match)
def delete(storage, city, date):
    found_index = -1
    for i in range(len(storage["records"])):
        rec = storage["records"][i]
        if rec["city"] == city and rec["date"] == date:
            found_index = i
            break
    if found_index != -1:
        storage["records"].pop(found_index)
        r = index_of(storage["years"], date)
        c = index_of(storage["cities"], city)
        if r != -1 and c != -1:
            storage["array"][r][c] = None
        return True
    return False

# Retrieve temperatures for a city in a year
def retrieve(storage, city, year):
    result = []
    for rec in storage["records"]:
        if rec["city"] == city and rec["date"] == year:
            result.append(rec["temperature"])
    return result

# Populate 2D array from records (useful if records were added/changed externally)
def populate_array(storage):
    rows = len(storage["years"])
    cols = len(storage["cities"])
    # reset
    for i in range(rows):
        for j in range(cols):
            storage["array"][i][j] = None
    # populate
    for rec in storage["records"]:
        r = index_of(storage["years"], rec["date"])
        c = index_of(storage["cities"], rec["city"])
        if r != -1 and c != -1:
            storage["array"][r][c] = rec["temperature"]

# Row-major access
def row_major_access(storage):
    values = []
    for i in range(len(storage["array"])):
        for j in range(len(storage["array"][i])):
            values.append(storage["array"][i][j])
    return values

# Column-major access
def column_major_access(storage):
    values = []
    if len(storage["array"]) == 0:
        return values
    rows = len(storage["array"])
    cols = len(storage["array"][0])
    for j in range(cols):
        for i in range(rows):
            values.append(storage["array"][i][j])
    return values

# Handle sparse data -> return dict of (year_index, city_index) -> temp
def handle_sparse_data(storage):
    sparse = {}
    for i in range(len(storage["array"])):
        for j in range(len(storage["array"][i])):
            val = storage["array"][i][j]
            if val is not None:
                sparse[(i, j)] = val
    return sparse

# Complexity analysis
def analyze_complexity():
    return {
        "insert": "O(1) amortized (append to list + O(1) array write)",
        "delete": "O(n) (search through records list)",
        "retrieve": "O(n) (scan records list for matches)",
        "row_major_access": "O(rows * cols)",
        "column_major_access": "O(rows * cols)",
        "space": "O(rows * cols) for array + O(r) for records"
    }

def print_table(storage):
    years = storage["years"]
    cities = storage["cities"]
    array = storage["array"]

    # Print header
    header = "Year/City".ljust(10)
    for city in cities:
        header += city.ljust(10)
    print(header)

    # Print rows
    for i in range(len(years)):
        row = years[i].ljust(10)
        for j in range(len(cities)):
            val = array[i][j]
            if val is None:
                row += "None".ljust(10)
            else:
                row += str(val).ljust(10)
        print(row)


def main():
    years_input = input("Enter years (comma separated, e.g. 2023,2024): ")
    cities_input = input("Enter cities (comma separated, e.g. Delhi,Mumbai): ")

    years = [y.strip() for y in years_input.split(",") if y.strip() != ""]
    cities = [c.strip() for c in cities_input.split(",") if c.strip() != ""]

    storage = create_storage(years, cities)

    while True:
        print("\n1. Insert records")
        print("2. Delete record")
        print("3. Retrieve records")
        print("4. Populate array from records")
        print("5. Row-major flatten")
        print("6. Column-major flatten")
        print("7. Sparse representation")
        print("8. Print table")
        print("9. Complexity info")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            n = int(input("How many records? "))
            for _ in range(n):
                d = input("Year/date: ")
                c = input("City: ")
                t = float(input("Temperature: "))
                rec = make_record(d, c, t)
                insert(storage, rec)

        elif choice == '2':
            c = input("City to delete: ")
            d = input("Year/date to delete: ")
            if delete(storage, c, d):
                print("Record deleted.")
            else:
                print("No match found.")

        elif choice == '3':
            c = input("City: ")
            d = input("Year/date: ")
            print("Temperatures:", retrieve(storage, c, d))

        elif choice == '4':
            populate_array(storage)
            print("Array repopulated.")

        elif choice == '5':
            print("Row-major:", row_major_access(storage))

        elif choice == '6':
            print("Column-major:", column_major_access(storage))

        elif choice == '7':
            sparse = handle_sparse_data(storage)
            print("Sparse data:", sparse)

        elif choice == '8':
            print_table(storage)

        elif choice == '9':
            comp = analyze_complexity()
            for k, v in comp.items():
                print(k, ":", v)

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()