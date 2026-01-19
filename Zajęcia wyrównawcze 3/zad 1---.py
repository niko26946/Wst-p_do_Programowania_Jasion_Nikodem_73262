#zad11
from task_utilis import show_tasks
#zad12
import task_utilis as tu


tasks = ["pranie", "projekt", "zakupy", "siłownia"]

tu.add_tasks(tasks, "ride!")
show_tasks(tasks)

#zad13
def add_many_tasks(list_of_tasks, new_tasks):
    for new_task in new_tasks:
        tu.add_tasks(list_of_tasks, new_task)


add_many_tasks(tasks, ["study", "rower", "daily-quest"])
show_tasks(tasks)