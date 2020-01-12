# Song sorter
# Sorts 'artists.txt' alphabetically and caps first letter of each word
f = open('artists.txt') #open file
lines = f.readlines() #read each line into lists
lines = [x for x in lines if x != '\n'] #remove gaps in list
for i in range (0, len(lines)): #for each line
 lines[i] = lines[i].title() #capitalize first letter of each word
lines = list(dict.fromkeys(lines)) #remove duplicates
lines.sort() #sort alphabetically
open('artists.txt', "w").close() #wipe file
for x in range(0, len(lines)): #rewrite file using sorted list
 with open('artists.txt', 'a') as myfile:
  myfile.write(lines[x])
print("sorted") #task completion message
