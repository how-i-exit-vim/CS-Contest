#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct virus virus;
struct virus {
    uint64_t size;
    virus * next;
};

typedef struct immune_system {
    virus * head;
    uint64_t len;
} immune_system;

virus * init_virus(uint64_t size) {
    virus * new_virus = (virus *)malloc(sizeof(virus));
    new_virus->size = size;
    new_virus->next = NULL;
    return new_virus;
}

immune_system * init_system() {
    immune_system * new_list = (immune_system *)malloc(sizeof(immune_system));
    new_list->head = NULL;
    new_list->len = 0;
    return new_list;
}

void analyze_system(immune_system * sys) {
    printf("immune_system[%lu] : { ", sys->len);
    virus * vp = sys->head;
    while (vp) {
        printf("%lu ", vp->size);
        vp = vp->next;
    }
    printf("}\n");
}

void virus_mutate(virus * vir, uint64_t new_size) {
    vir->size = new_size;
}

void inject_virus(immune_system * sys, uint64_t size) {
    if (sys->len == 0) {
        virus * vir = init_virus(size);
        sys->head = vir;
        sys->len++;
    } else {
        if (sys->head->size >= size) {
            virus * vir = init_virus(size);
            vir->next = sys->head;
            sys->head = vir;
            sys->len++;
        } else {
            virus * vp = sys->head;
            while ((vp->next) && (vp->next->size < size)) {
                vp = vp->next;
            }
            virus_mutate(vp, size);
        }
    }
}

int main() {

    // Initializing the immune_system
    immune_system * sys = init_system();

    // Inserting all virus
    uint64_t size;
    scanf("%lu", &size);
    while (size) {
        inject_virus(sys, size);
        scanf("%lu", &size);
    }

    // Getting the final result
    printf("%lu\n", sys->len);

    return 0;
}