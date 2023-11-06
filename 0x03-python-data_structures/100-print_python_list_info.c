#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - is the main func
 * @p: is the pointer to the python object
 * Return: as specified
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
