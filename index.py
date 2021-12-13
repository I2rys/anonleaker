#Dependencies
from googlesearch import search
import sys

#Variables
args = sys.argv

#Main
if len(args) == 1:
    print("python index.py <keyword> <amount> <output>")
    sys.exit()
    
if len(args) == 2:
    print("Invalid amount.")
    sys.exit()
    
if len(args) == 3:
    print("Invalid output.")
    sys.exit()

if args[2].isnumeric() == False:
    print("amount is not a number.")
    sys.exit()
    
results = search(f"site:anonfiles.com {args[1]}", num_results=int(args[2]) - 1)

if len(results) == 0:
    print("No links found.")
    sys.exit()
    
for link in results:
    print(link)
    
print(f"{len(results)} links found.")
print("Saving the results, please wait.")
file = open(args[3], "w")
file.write("\n".join(results))
file.close()
print(f"Results has been saved to {args[3]}")
