# include <Python.h>
# include <random>
using namespace std;

class Rander {
public:
    Rander() {
        random_device rd;

        this->gen(rd());
    }

    int rand(int range_min, int range_max) {
        uniform_int_distibution<> dis(range_min, range_max);
    
        return dis(this->gen);
    }
private:
    mt19937 gen;
}


typedef struct {
    PyObject_HEAD,
    Rander* obj;
} RanderObj;


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