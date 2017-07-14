#!user/bin/env python
# -*- coding:utf-8 -*-

def media(a, b):
	m, n = len(a), len(b)
	if m > n:
		m, n, a, b = n, m, b, a
	if n == 0:
		raise ValueError
	imin, imax, half_len = 0, m, (m + n) / 2
	while imin <= imax:
		i = (imin + imax) / 2
		j = half_len - i
		if i < m and b[j - 1] > a[i]:
			imin = i + 1
		elif i > 0 and a[i - 1] > b[j]:
			imax = i - 1
		else:
			if i == 0: max_of_left = b[j - 1]
			elif j == 0: max_of_left = a[i - 1]
			else:
				max_of_left = max(a[i - 1], b[j - 1])
				if (m + n) % 2 == 1:
					return max_of_left
				if i == m: min_of_right = b[j]
				elif j == n: min_of_right = a[i]
				else: min_of_right = min(a[i], b[j])
				return (max_of_left + min_of_right) / 2.0
		
