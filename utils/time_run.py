import time

def log_time(fn):
	def inner(*args, **kwargs):
		tnow = time.time()
		out = fn(*args, **kwargs)
		te = time.time()
		took = round(te - tnow, 2)
		
		if took <= .000_001:
			print(f"{fn.__name__} ran in {took*1_000_000_000:.4f} ns")
		elif took <= .001:
			print(f"{fn.__name__} ran in {took*1_000_000:.4f} μs")
		elif took <= 1:
			print(f"{fn.__name__} ran in {took*1_000:.4f} ms")
		elif took <= 60:
			print(f"{fn.__name__} ran in {took:.2f} s")
		elif took <= 3600:
			print(f"{fn.__name__} ran in {(took)/60:.2f} m")		
		else:
			print(f"{fn.__name__} ran in {(took)/3600:.2f} h")
		return out
	return inner