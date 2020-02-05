year = eval(input("Enter the number of years:"))
time = year * 365 * 24 *60 * 60
current_population = 3120324986
change_of_population_per_second = 1/7 - 1/13 + 1 /45
change_of_population_in_five_year = time * change_of_population_per_second
finalpopulation = current_population + change_of_population_in_five_year

print("""
美国当前人口为{}，
每秒人口变化为{},
五年内人口变化为{},
五年后人口为{}
""".format(current_population,change_of_population_per_second,change_of_population_in_five_year,finalpopulation))
