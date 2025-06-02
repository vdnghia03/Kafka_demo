from read_data import read_data

df = read_data()


approved = df.query("Beslut == 'Beviljad'")

number_approved = len(approved)
total_application = len(df)
approved_percentage = f"{number_approved / total_application * 100 :.1f}%"

print(number_approved)
print(total_application)
print(approved_percentage)