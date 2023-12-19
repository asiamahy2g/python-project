import csv

def List_jobs(jenkins_url, jenkins_user, jenkins_pass):

    import jenkins

    jen_server = jenkins.Jenkins(jenkins_url, username= jenkins_user, password= jenkins_pass)

    user = jen_server.get_whoami()
    jobs = jen_server.get_jobs()
    #print(dir(jen_server))

    Job_stats=[]
    for job in jobs:
        Job_name= job['name'] ,
        Job_url = job['url'] 
        Job_status = job['color']
        Job_stats.append([Job_name, Job_url, Job_status])

    return Job_stats

# with open("example.txt" , 'a') as f:
#     content = "adding data into file\n"
#     f.write(content)

# with open("example.txt" , 'r') as file:
#     cont = file.read()
#     print(cont)

data=List_jobs("http://ec2-44-204-17-137.compute-1.amazonaws.com:8080/", "devmanny", "devops")
with open("jenkins_object.csv" , 'w') as j:
    write_row = csv.writer(j)
    write_row.writerow(['JOB_NAME', 'JOB_URL', 'JOB_STATUS'])
    for item in data:
        write_row.writerow(item)




