f = open('input.txt', 'r')

def ret_data(code):
    return code[:7], code[7:].strip()

def ret_row(row_data):
    no = row_data.replace('F', '0').replace('B', '1')
    return int(no, 2)

def ret_col(col_data):
    no = col_data.replace('L', '0').replace('R', '1')
    return int(no, 2)

highest = 0
d = {i:[] for i in range(0,128)}
for i in f:
    # Get the column and row data
    row, col = ret_data(i)
    
    # Convert the column and row to integers
    row_no = ret_row(row)
    col_no = ret_col(col)
    
    # Calculate the ID
    tid = (row_no * 8) + col_no
    
    # Get the highest ID!
    if tid > highest: highest = tid
    
    # Print the stuff!
    print('for seat {} -> col: {}, row: {}, ID: {}'.format(i.strip(), col_no, row_no, tid))
    d[row_no].append(col_no)

print(highest)

# Part 2
# For all the keys, find the one that doesn't have a full row.
for k,v in d.items():
    if len(v) != 8 and len(v) !=0:
        print('{} -> {}'.format(k, v))