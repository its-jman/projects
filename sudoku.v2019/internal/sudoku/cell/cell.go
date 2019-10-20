package cell

func NewCell(val byte) *Cell {
	c := &Cell{}
	c.SetValue(BtoI(val))

	return c
}

type Cell struct {
	val int
}

func (c *Cell) SetValue(val int) {
	if ValidInt(val) {
		c.val = val
	} else {
		c.val = -1
	}
}

func (c *Cell) Val() int {
	return c.val
}
