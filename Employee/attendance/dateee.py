total_days = 31
total_days_list = {}

for i in range(1, total_days+1):
  if i==2:
    total_days_list[i] = "date_row_2"
  else:
    total_days_list[i] = "date"
print(total_days_list)