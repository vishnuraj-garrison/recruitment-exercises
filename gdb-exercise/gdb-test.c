#include <stdio.h>
#include <stdlib.h>

typedef struct _Node {
    int data;
    struct _Node* next;
} Node;


void add_node(Node** head, int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->next = *head;
    *head = new_node;
    printf("Node with data %d added.\n", data);
}

void populate_list(Node** head, int size) {
    int it = 0;

    for (it = 0; it < size; it++) {
        add_node(head, it + 1);
    }
}

void print_list(Node* head) {
    Node* current = head;

    printf("List contents: ");
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

void delete_list(Node* head) {
    Node* current = head;
    Node* next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
    printf("List deleted.\n");
}

void update_list(Node* head) {
    Node* current = head;
    Node* next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }

    printf("List updated.\n");
}

void process_list(Node* head) {
    Node* current = head;
    while (current != NULL) {
        current->data += 1;
        current = current->next;
    }
    printf("List processed.\n");

    update_list(head);
}


int main() {
    Node* head = NULL;
    populate_list(&head, 5);

    print_list(head);
    
    process_list(head);
    
    print_list(head);
    
    delete_list(head);
    
    printf("Program finished.\n");
    return 0;
}