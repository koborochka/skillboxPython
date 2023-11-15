import random


class KillError(Exception):
	pass

class DrunkError(Exception):
	pass

class CarCrashError(Exception):
	pass

class GluttonyError(Exception):
	pass

class DepressionError(Exception):
	pass


def one_day():
	karma = random.randint(1, 7)
	if random.randint(1, 10) == 1:
		raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
	return karma


with open("karma.log", "w") as file:
	karma_sum = 0
	while karma_sum < 500:
		try:
			karma = one_day()
			karma_sum += karma
		except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
			file.write(f"Exception: {e.__class__.__name__}\n")

