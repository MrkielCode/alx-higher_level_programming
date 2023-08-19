#include <Python.h>
/**
 * print_python_list_info - to print python some info
 * @p: python object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size, get_alloc, counter = 0;
	PyObject *obj;

	size = Py_SIZE(p);
	get_alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", get_alloc);

	while (counter < size)
	{
		printf("Element %d: ", counter);
		obj = PyList_GetItem(p, counter);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		counter++;
	}
}
