
#deep copy
import copy
projects=[['job-posting','finance','banking'],['marketing','privacy','HR']]
tasks=copy.deepcopy(projects)
tasks[1][1]='cyber-security'
print(f'deep copy')
print("orginal projects",projects)
print("changed_tasks",tasks)


#shallow copy
import copy
projects=[['job-posting','finance','banking'],['marketing','privacy','HR']]
tasks=copy.copy(projects)
tasks[1][1]='cyber-security'
print("shallow copy")
print("orginal projects",projects)
print("changed_tasks",tasks)


import array
ar=array.array('i',[10,20,30])
ar.insert(4,370)
print(ar)