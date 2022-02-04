# This opens the file and returns a file object
log_file = open("um-server-01.txt")

# This is a function that loops through the file objects
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

# # This calls the function to get the data requested from its body
# sales_reports(log_file)

def sold_report(log_file):
    for line in log_file:
        line=line.split()
        if int(line[2]) > 10:
            print(line)


sold_report(log_file)    
