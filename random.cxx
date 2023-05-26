# include <stdlib.h>

# ifdef __cplusplus
	extern "C" {
# endif

__declspec(dllexport) int random(int from, int before) {
	int randomInt = rand() % before;
	while (randomInt < from) {
		randomInt = rand() % before;
	}
	return randomInt;
}

__declspec(dllexport) int srandom() {
	return rand();
}

# ifdef __cplusplus
	}
# endif