def create_seating_chart(rows, columns):
    seating_chart = []
    
    for row in range(1, rows + 1):
        if row in (5, 6, 13, 14):
            continue
        row_data = []
        for col in columns:
            if row <= 4:
                if col == 'B':
                    row_data.append(' ')
                else:
                    row_data.append(col)
            else:
                row_data.append(col)
        seating_chart.append(row_data)
    
    return seating_chart

def print_seating_chart(seating_chart):
    for row_num, row in enumerate(seating_chart, 1):
        if row_num in (5, 6, 13, 14):
            continue
        print(f"{row_num:2}", end=" ")
        for seat in row:
            print(seat, end="  ")
        print()

def main():
    rows = 29
    columns = ['A', 'B', 'C', 'D']
    
    seating_chart = create_seating_chart(rows, columns)
    print_seating_chart(seating_chart)

if __name__ == "__main__":
    main()
