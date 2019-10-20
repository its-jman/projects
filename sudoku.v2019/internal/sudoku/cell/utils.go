package cell

func ValidInt(val int) bool {
	return val >= 1 && val <= 9
}

func ValidByte(val byte) bool {
	return ValidInt(int(val - '0'))
}

func BtoI(val byte) int {
	if ValidByte(val) {
		return int(val - '0')
	} else {
		return -1
	}
}
