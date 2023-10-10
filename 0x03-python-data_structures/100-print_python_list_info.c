#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p:A Pyobject list
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject *object;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for(i = 0; i <sie; i++)
	{
		printf("Element %d: ", i);

		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}

}
