# include <stdlib.h>
# include <Python.h>

static PyObject* random(PyObject* self, PyObject* args) {
    int range_max, range_min;

    if (!PyArg_ParseTuple(args, "ii", &range_min, &range_max)) {
        return NULL;
    }

    int result = ((double)rand() / RAND_MAX) * (range_max - range_min) + range_min;

    return Py_BuildValue("i", result);
}

static PyObject* _overclocking(PyObject* self, PyObject* args) {

    srand(time(NULL));

    return Py_None;
}


static PyMethodDef methods[] = {
    {"random", random, METH_VARARGS, "C/C++ random"},
    {"_overclocking", _overclocking, METH_VARARGS, "Overclocking"}
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