# include <Python.h>
# include <random>




static PyMethodDef methods[] = {
    {"random", random, METH_VARARGS, "C/C++ random"},
    {NULL, NULL, 0, NULL} 
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "rand",
    "C/C++ random",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_rand(void) {
    return PyModule_Create(&module);
}