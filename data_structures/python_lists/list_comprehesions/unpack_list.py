profile = ["amjad", 27, "ai_engineer", "berlin"]
#i can generate variables like
name, age, job, city = profile
print(name)
#for example job and city are irrelavant for me 
profile = ["amjad", 27, "ai_engineer", "berlin"]
name, age , *other_details = profile
print(other_details)
print(name)
#under asteric we have stored all other values.
#what if i dnt want to store values , i just wanna skip them
profile = ["amjad", 27, "ai_engineer", "berlin"]
name, age , *_ = profile
print(_)
print(name)