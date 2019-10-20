package group

func createGroupMap(def bool) map[int]bool {
	out := map[int]bool{}
	for i := 1; i <= 9; i++ {
		out[i] = def
	}
	return out
}
