
#dictionar key:value pair
d={"jack":78,"jerry":89,"sam":78} #key cannot
print(d)
print(d["jack"])
#add a pair to dict
d["Sam"]="sas"
print(d)
student={"jerry":{"sid":1,
                   "address":"perth",
                   "marks":78},
        "Max":{"sid":2,"address":"Sydney","marks":89},
        "Jack":{"sid":3,"address":"Tasmania","marks":45}
        }

print(student)
print(student["jerry"]["sid"])
print(student["Max"]["marks"])
print(student["jerry"]["address"])