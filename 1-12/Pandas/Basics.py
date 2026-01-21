# Pandas reads input in 2 ways series(1D) and dataframe(2D) used for data analysis ,manipulation ,updation etc
# series
import pandas as pd
s = pd.Series([1,2,3,4,5,6])
print(s)

# Dataframe
data = {
    "names" : ["Ayush","Diksha","Akku"],
    "ages" : [20,30,40],
    "marks" : [99,98,97],
    "city" :["Kashi","Jsr","kochi"]
}
df = pd.DataFrame(data)
print(df)

# to csv and to read from csv
df.to_csv("data.csv", index=False)
print("Csv file created")
df1=pd.read_csv("data.csv")

print(df1)
print("csv file read successfully")


#operations
print(df.head(2))
print(df.tail(2))
print(df.describe())
print(df.info())
print(df.shape)
print(df.columns)

#printing only specific columns
print(df["names"])
print(df[["ages","marks"]])

#filters
good_scorers = df[(df["marks"]>98)]
print(good_scorers)

aged = df[(df["ages"]>10) & (df["marks"]>98)]
print(aged)

#adding column
df["Result"]=df["marks"].apply(lambda x: "Pass" if x>98  else "Fail")
print(df)

#sorting
print(df.sort_values(by="marks",ascending=False))

#filling missing values
df2 = df.copy()
df2.loc[1,"city"]=None
print(df2)
print(df2.isnull().sum())

df2_filled=df2.fillna("Unknown")
print(df2_filled)

#group by
city_marks=df2.groupby("city")["marks"].count()
print(city_marks)

avg_age = df2.groupby("city")["ages"].mean()
print(avg_age)





