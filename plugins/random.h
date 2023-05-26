# include <stdlib>

# ifdef __cplusplus
	extern "C" {
# endif

int random(int from, int before) {
	int randomInt = rand() % before;
	while (randomInt < from) {
		randomInt = rand() % before;
	}
	return randomInt;
}

# ifdef __cplusplus
	}
# endif