func tribonacci(n int) int {
	x := 0 
	y := 1
	z := 1

	for i := 0; i < n; i++ {
		x, y, z = y, z, x+y+z
	}

	return x
}