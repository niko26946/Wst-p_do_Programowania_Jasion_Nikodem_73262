tasks = ["pranie", "projekt", "zakupy", "siłownia"]
#zad1
def show_tasks(list_of_tasks):
    for task in list_of_tasks:
        print(task)
#zad2

def add_tasks(list_of_tasks, new_task):
    list_of_tasks.append(new_task)

add_tasks(tasks, "coś")

#zad3

def remove_tasks(list_of_tasks, del_task):
    list_of_tasks.remove(del_task)
remove_tasks(tasks, "projekt")

#zad4
#dlugośc listy


#zad5

#def has_tasks(list_of_tasks, task):
#    if (task in list_of_tasks):

 #       return True
 #   else: return False

  #  return task in list_of_tasks

#print(has_tasks(tasks, "projekt"))





#zad6

#def reset_tasks(list_of_tasks):
#    list_of_tasks.clear()

#reset_tasks(tasks)
#show_tasks(tasks)

#zad7

add_tasks(tasks, "projekt!")

def get_urgent_tasks(list_of_tasks):
    urgent_tasks = []
    for task in list_of_tasks:
        if  '!' in task: urgent_tasks.append(task)
    return urgent_tasks
#show_tasks(get_urgent_tasks(tasks))

#zad8

def mark_done(list_of_tasks, task):
    remove_tasks(list_of_tasks, task)



#zad9

def archive_tasks(list_of_tasks):
    return list_of_tasks
archiwum = archive_tasks(tasks)
show_tasks(archiwum)
