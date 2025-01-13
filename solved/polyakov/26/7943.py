
students_database_example = {
    601: {12, 43, 44, 45, 67}
}

students_database = {

}

with open('26-159.txt', 'r') as file:
    number = int(file.readline())
    for line in file.readlines():
        if line:
            student_id, task_id = map(int, line.split())
            if student_id not in students_database:
                students_database[student_id] = set()
            students_database[student_id].add(task_id)

max_in_row = 0
max_student_id = None
results = {}

for student_id, tasks in sorted(students_database.items(), key=lambda item: item[0], reverse=True):
    sorted_tasks = sorted(tasks)
    local_max_in_row = 0
    in_row = 1
    for i, task_id in enumerate(sorted_tasks):
        if i == 0:
            continue
        if task_id - sorted_tasks[i - 1] == 1:
            in_row += 1
        else:
            if in_row > local_max_in_row:
                local_max_in_row = in_row
            in_row = 1
    if in_row > local_max_in_row:
        local_max_in_row = in_row
    if local_max_in_row >= max_in_row:
        max_in_row = local_max_in_row
        max_student_id = student_id


print(max_student_id)
print(max_in_row)