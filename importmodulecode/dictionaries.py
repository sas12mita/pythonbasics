workshop={
    "Sasmita":
    {
        "fav_color":"red",
        "fav_nul":"WindowsError",
        "destination":"Pokhara",

    },
    "Bikash":
    {
        "fav_color":"blue",
        "fav_nul":"WindowsError",
        "destination":"Pokhara",

    }
}
print(workshop)
print(workshop["Sasmita"])
print(workshop["Bikash"]["destination"])


#update dictionary
workshop["Sasmita"]["fav_nul"]="one",
print(workshop["Sasmita"])

d={

}
d[1]=5
print(d)

#update 
d.update({
    2: 10,
    3: 15
})

print(d)