# include <stdlib.h>

# ifdef __cplusplus
	extern "C" {
# endif

__declspec(dllexport) int random(int range_min, int range_max) {
    return ((double)rand() / RAND_MAX) * (range_max - range_min) + range_min;
}

# ifdef __cplusplus
	}
# endif