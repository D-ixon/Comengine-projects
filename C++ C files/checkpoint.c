#include <stdio.h>
#include <string.h>

#define MAX_TASKS 10
#define TASK_LEN 100

void showMenu() {
    printf("\n--- QUICK TASK MANAGER ---\n");
    printf("1. View Tasks\n");
    printf("2. Add a Task\n");
    printf("3. Exit\n");
    printf("Choose an option: ");
}

int main() {
    char tasks[MAX_TASKS][TASK_LEN];
    int taskCount = 0;
    int choice;

    while (1) {
        showMenu();
        scanf("%d", &choice);
        getchar();

        if (choice == 1) {
            printf("\nYOUR TASKS:\n");
            if (taskCount == 0) {
                printf("No tasks yet. Go relax!\n");
            } else {
                for (int i = 0; i < taskCount; i++) {
                    printf("%d. %s\n", i + 1, tasks[i]);
                }
            }
        } 
        else if (choice == 2) {
            if (taskCount < MAX_TASKS) {
                printf("Enter task description: ");
                fgets(tasks[taskCount], TASK_LEN, stdin);
                tasks[taskCount][strcspn(tasks[taskCount], "\n")] = 0;
                taskCount++;
                printf("Task added!\n");
            } else {
                printf("List full! Finish something first.\n");
            }
        } 
        else if (choice == 3) {
            printf("Goodbye!\n");
            break;
        } 
        else {
            printf("Invalid choice. Try again.\n");
        }
    }

    return 0;
}