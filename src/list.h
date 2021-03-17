#ifndef LIST_H
#define LIST_H

/*
为了解析网络配置参数，DarkNet 中定义了三个关键的数据结构类型。
list类型变量保存所有的网络参数, 
section类型变量保存的是网络中每一层的网络类型和参数, 其中的参数又是使用list类型来表示。
kvp键值对类型用来保存解析后的参数变量和参数值。
*/

// 链表上的节点
typedef struct node{
    void *val;
    struct node *next;
    struct node *prev;
} node;

//双向链表
typedef struct list{
    int size;//list的所有节点个数
    node *front;//list的首节点
    node *back;//list的普通节点
} list;

#ifdef __cplusplus
extern "C" {
#endif
list *make_list();
int list_find(list *l, void *val);

void list_insert(list *, void *);

void **list_to_array(list *l);

void free_list_val(list *l);
void free_list(list *l);
void free_list_contents(list *l);
void free_list_contents_kvp(list *l);

#ifdef __cplusplus
}
#endif
#endif
