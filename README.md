# Weather ADT Project

This project implements a **Weather Abstract Data Type (ADT)** in Python using procedural programming techniques. It provides functionalities to store, manage, and analyze temperature records for different cities across multiple years. The data can be accessed and manipulated using various operations through a simple console menu interface.

## Features

- **Add new temperature records** for cities and years.
- **Delete records** by city and year/date.
- **Retrieve temperatures** for a specific city and year/date.
- **Populate a 2D array** (year × city) from stored records.
- **Row-major and column-major flattening** of the data array.
- **Sparse data representation** for efficient storage and access.
- **Complexity analysis** for major operations.
- **Tabular display** of records for easy viewing.

## How It Works

- **Data Storage:**  
  The program uses a dictionary to store years, cities, a 2D array for temperatures, and the list of all records.
- **Menu-Driven Interface:**  
  Users interact with the program via numbered menu options in the console.
- **Operations:**  
  - Insert, delete, and retrieve records
  - Repopulate the 2D array from the records list
  - View the data as a flattened list (row- or column-major order)
  - View a sparse representation (only non-empty entries)
  - Print the data in a table format
  - Check the time/space complexity of each operation

## Getting Started

1. **Run the program:**
    ```bash
    python komal_proj.py
    ```
2. **Initialize storage:**
    - Enter years (comma separated), e.g. `2023,2024`
    - Enter cities (comma separated), e.g. `Delhi,Mumbai`
3. **Use the menu options:**  
    Enter the number corresponding to the desired operation.

## Example

```
Enter years (comma separated, e.g. 2023,2024): 2023,2024
Enter cities (comma separated, e.g. Delhi,Mumbai): Delhi,Mumbai

1. Insert records
2. Delete record
3. Retrieve records
...
Enter your choice: 1
How many records? 2
Year/date: 2023
City: Delhi
Temperature: 35
Year/date: 2024
City: Mumbai
Temperature: 30
```

## Code Structure

- `make_record(date, city, temperature)` — Create a record dictionary
- `create_storage(years, cities)` — Initialize the storage structure
- `insert(storage, record)` — Add a record
- `delete(storage, city, date)` — Remove a record
- `retrieve(storage, city, year)` — Get temperatures for a city/year
- `populate_array(storage)` — Rebuild the array from records
- `row_major_access(storage)` — Flatten data row-wise
- `column_major_access(storage)` — Flatten data column-wise
- `handle_sparse_data(storage)` — Sparse dictionary rep
- `analyze_complexity()` — Time/space complexity info
- `print_table(storage)` — Print records as a table
- `main()` — Menu and input handling

## Complexity Analysis

The program displays complexity for key operations. Example:
- **Insert:** O(1) amortized
- **Delete:** O(n)
- **Retrieve:** O(n)
- **Row/Column-major access:** O(rows × cols)
- **Space:** O(rows × cols) + O(records)

## Notes

- Supports arbitrary numbers of years and cities.
- Handles missing data gracefully (`None`).
- Console-based; no external dependencies.

---

**Author:** Komal Dahiya  
**Repository:** [dahiyakomal024/data_structure](https://github.com/dahiyakomal024/data_structure)
