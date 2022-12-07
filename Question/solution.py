# How would you merge datasets like these?

# District | KPI_1
# Kathmandu | .8
# Dhanusa | .85
# Kavre palanchowk | .75

# District | KPI_2
# Kathmandu | .35
# Kavrepalanchowk | .65
# Dhanusha | .6
data1 = {"Kathmandu": .8, "Dhanusa": .85, "Kavre palanchowk": .75}

data2 = {"Kathmandu": .35, "Kavrepalanchowk": .65, "Dhanusha": .6}

merged_data = {}

for district, kpi1 in data1.items():
    merged_data[district] = {"KPI_1": kpi1}

for district, kpi2 in data2.items():
    if district in merged_data:
        merged_data[district]["KPI_2"] = kpi2
    else:
        merged_data[district] = {"KPI_2": kpi2}

print(merged_data)

