#include <Python.h>

void print_python_list(PyObject *p)
{
    long int size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (int i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %i: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}

void print_python_bytes(PyObject *p)
{
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    long int size = PyBytes_Size(p);
    char *str = PyBytes_AsString(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes:", size < 10 ? size + 1 : 10);
    for (int i = 0; i < size && i < 10; i++) {
        printf(" %02hhx", str[i]);
    }
    printf("\n");
}

