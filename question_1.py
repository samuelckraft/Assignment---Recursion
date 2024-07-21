#Task 1

def schedule_tasks(task_hierarchy):
    tasks = []
    def traverse_tasks(task, tasks):
        tasks.append(task)

        for subtask in task.get('subtasks', []):
            traverse_tasks(subtask, tasks)

#Task 2
    def prioritize(tasks):
        tasks.sort(key=lambda x: (x.get('priority', float('inf')), x['name']))
        return tasks

    traverse_tasks(task_hierarchy, tasks)
    scheduled_tasks = prioritize(tasks)
    
    return scheduled_tasks

#Task 3
task_hierarchy = {
    'id': '1',
    'name': 'Main Project',
    'subtasks': [
        {
            'id': '1.1',
            'name': 'Schedule',
            'priority': 1,
            'subtasks': []
        },
        {
            'id': '1.2',
            'name': 'Delegate',
            'priority': 2,
            'subtasks': [
                {
                    'id': '1.2.1',
                    'name': 'Assign Roles',
                    'priority': 1,
                    'subtasks': []
                },
                {
                    'id': '1.2.2',
                    'name': 'Divide rooms',
                    'subtasks': []
                }
            ]
        },
        {
            'id': '1.3',
            'name': 'Status updates',
            'subtasks': []
        }
    ]
}

scheduled_tasks = schedule_tasks(task_hierarchy)

for task in scheduled_tasks:
    print(f"Task ID: {task['id']} - Name: {task['name']} - Priority: {task.get('priority', 'None')}\n")