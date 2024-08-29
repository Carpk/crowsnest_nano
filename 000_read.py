import os



dir_list = os.listdir()
formatted_list = []

# formatted_list = map(lambda x: "{ src: "+x+", srct: "+x+"},", dir_list)

path = "bear/"

for x in dir_list:
	formatted_list.append('{ src: "'+path+x+'", srct: "'+path+x+'"},')

print(formatted_list)