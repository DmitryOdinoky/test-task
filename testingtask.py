import os
import glob
import importlib.util

def main():
    tasks_dir = "tasks"
    if not os.path.exists(tasks_dir):
        print(f"Error: '{tasks_dir}' directory not found.")
        return
    
    # Get all Python files in the 'tasks' directory excluding __init__.py
    task_files = sorted([f for f in glob.glob(os.path.join(tasks_dir, "*.py")) if not os.path.basename(f).startswith("__")])
    
    if not task_files:
        print(f"No Python files found in '{tasks_dir}' directory.")
        return
    
    for task_file in task_files:
        task_name = os.path.splitext(os.path.basename(task_file))[0]
        
        try:
            # Dynamically load the module
            spec = importlib.util.spec_from_file_location(task_name, task_file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # Execute the module
            if hasattr(module, "main") and callable(module.main):
                print(f"Launching task '{task_name}'...")
                module.main()
            else:
                print(f"Module '{task_name}' does not have a callable 'main()' function.")
        
        except Exception as e:
            print(f"Error launching task '{task_name}': {e}")

if __name__ == "__main__":
    main()
