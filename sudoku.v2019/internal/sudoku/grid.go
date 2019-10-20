package sudoku

import (
	"github.com/jbmmhk/sudoku/internal/sudoku/cell"
	"github.com/jbmmhk/sudoku/internal/sudoku/group"
	log "github.com/sirupsen/logrus"
	"strconv"
	"strings"
)

func NewGrid(line string) *Grid {
	err := verifyPuzzle(line)
	if err != nil {
		log.Error(err)
		return nil
	}

	grid := &Grid{}
	rawGrid := []byte(line)
	for i, cv := range rawGrid {
		grid.Cells[i] = cell.NewCell(cv)
	}

	return grid
}

type Grid struct {
	Cells  [9 * 9]*cell.Cell
	Groups [3 * 9]*group.Group
}

func (g *Grid) Print() {
	var sb strings.Builder
	for i, cell := range g.Cells {
		sb.WriteString(strconv.Itoa(cell.Val()))
		sb.WriteRune(' ')

		x, y := GetGridCoords(i + 1)
		if x == 9 {
			if y > 1 && y%3 == 1 {
				log.Info("= = = | = = = | = = =")
			}

			log.Info(sb.String())
			sb.Reset()
		} else if x%3 == 0 {
			sb.WriteRune('|')
			sb.WriteRune(' ')
		}
	}
}
