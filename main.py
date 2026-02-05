from datetime import datetime
from database import engine, metadata_obj
import models
from crud import create_task,get_task,delete_task,update_task,change_status
from database import get_connection


metadata_obj.create_all(engine)


def add_tasks():
    title = input("title: ")
    description = input("description: ")
    due_date_text = input("due_date: (yyyy-mm-dd | hh):  ")

    due_date =  datetime.strptime(due_date_text,"%Y-%m-%d | %H:%M")


    create_task(get_connection(),title,description=description,due_date=due_date)

def show_task():
    get_task(get_connection())
    
def remove_task():
    task_id = int(input("task_id: "))
    
    delete_task(get_connection(),task_id)
    
def get_update():
    task_id = int(input("Task id : "))
    
    update_task(get_connection(),task_id,title="kitob uqish",description="ertaga 1 soat")
    
def ststus():
    task_id = int(input("task_id: "))
    
    change_status(get_connection())
        
    
    
def main():
    
    while True:
        
        print("=" * 40)
        print("           Menu")
        print("=" * 40)
        print("1. Tasklarni Qo'shish")
        print("2. Tasklarni Ko'rish")
        print("3. Tasklarni O'chirish")
        print("4. Tasklarni Yangilash")
        print("5. Tasklarni status uzgartirish")
        print("0. Chiqish")
        print("=" * 40)
        
        choises = input("Menu tanlang: ")
        
        
        if choises == "1":
            add_tasks()
            
        elif choises == "2":
            show_task()
            
        elif choises == "3":
            remove_task()
            
        elif choises == "4":
            get_update()
            
        elif choises == "5":
            ststus()
            
        elif choises == "0":
            exit()
            
        else:
            print("Xato menu tanladiz:")
            
if __name__ == "__main__":
    main()