"""
To-Do List Application
A simple command-line task management system

Author: Created for Python practice
Date: November 24, 2025
"""

# Global list to store all tasks
tasks = []


def display_welcome():
    """Display welcome message when the application starts"""
    print("\n" + "="*50)
    print("         WELCOME TO TO-DO LIST APPLICATION")
    print("="*50)
    print("Organize your tasks efficiently!\n")


def display_menu():
    """Display the main menu options to the user"""
    print("\n" + "-"*50)
    print("MAIN MENU")
    print("-"*50)
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Quit")
    print("-"*50)


def add_task():
    """
    Add a new task to the task list
    Handles empty input validation
    """
    try:
        print("\n--- ADD A NEW TASK ---")
        task = input("Enter the task description: ").strip()
        
        if not task:
            print("! Error: Task description cannot be empty!")
            return
        
        tasks.append(task)
        print(f"[+] Success! Task '{task}' has been added.")
        
    except Exception as e:
        print(f"! An unexpected error occurred: {e}")
    finally:
        print("--- Returning to main menu ---")


def view_tasks():
    """
    Display all tasks in the list
    Alerts user if the list is empty
    """
    try:
        print("\n--- YOUR TASKS ---")
        
        if not tasks:
            print("! No tasks available. Your task list is empty!")
            return
        
        print(f"You have {len(tasks)} task(s):\n")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
            
    except Exception as e:
        print(f"! An unexpected error occurred: {e}")
    finally:
        print("--- End of task list ---")


def delete_task():
    """
    Delete a task from the list by its number
    Handles invalid input and non-existent task numbers
    """
    try:
        print("\n--- DELETE A TASK ---")
        
        # Check if there are any tasks to delete
        if not tasks:
            print("! No tasks available to delete. Your task list is empty!")
            return
        
        # Display tasks first
        print("Current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        
        # Get user input
        task_number = input("\nEnter the task number to delete: ").strip()
        
        # Validate that input is a number
        if not task_number.isdigit():
            print("! Error: Please enter a valid number!")
            return
        
        task_index = int(task_number) - 1
        
        # Check if the task number exists
        if task_index < 0 or task_index >= len(tasks):
            print(f"! Error: Task number {task_number} doesn't exist!")
            return
        
        # Delete the task
        deleted_task = tasks.pop(task_index)
        print(f"[-] Success! Task '{deleted_task}' has been deleted.")
        
    except ValueError:
        print("! Error: Invalid input. Please enter a number!")
    except Exception as e:
        print(f"! An unexpected error occurred: {e}")
    finally:
        print("--- Returning to main menu ---")


def get_user_choice():
    """
    Get and validate user's menu choice
    Returns: User's choice as a string
    """
    try:
        choice = input("\nEnter your choice (1-4): ").strip()
        return choice
    except Exception as e:
        print(f"! Error reading input: {e}")
        return None


def main():
    """
    Main function to run the To-Do List application
    Controls the program flow and menu navigation
    """
    display_welcome()
    
    while True:
        try:
            display_menu()
            choice = get_user_choice()
            
            # Handle invalid input
            if choice is None:
                continue
            
            # Process user's choice
            if choice == "1":
                add_task()
                
            elif choice == "2":
                view_tasks()
                
            elif choice == "3":
                delete_task()
                
            elif choice == "4":
                print("\n" + "="*50)
                print("Thank you for using the To-Do List Application!")
                print("Goodbye!")
                print("="*50 + "\n")
                break
                
            else:
                print(f"! Error: '{choice}' is not a valid option!")
                print("Please choose a number between 1 and 4.")
        
        except KeyboardInterrupt:
            print("\n\n! Program interrupted by user.")
            print("Goodbye!\n")
            break
            
        except Exception as e:
            print(f"! An unexpected error occurred in main program: {e}")
        
        finally:
            # Small pause for better user experience
            if choice != "4":
                input("\nPress Enter to continue...")


# Entry point of the program
if __name__ == "__main__":
    main()
