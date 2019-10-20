package sudoku

import (
	"bufio"
	"fmt"
	log "github.com/sirupsen/logrus"
	"os"
	"regexp"
)

// Double escape the `.` because...?
var puzzlePattern = regexp.MustCompile(`^[\.1-9]{81}$`)
var whitespacePattern = regexp.MustCompile(`\s`)

func verifyPuzzle(puzzle string) error {
	if !puzzlePattern.MatchString(puzzle) {
		return fmt.Errorf("puzzle does not match pattern %v", puzzlePattern)
	}

	return nil
}

func LoadGridsFromFile(path string) []*Grid {
	fp, err := os.Open(path)
	if err != nil {
		log.Error(err)
	}
	defer fp.Close()

	s := bufio.NewScanner(fp)
	var out []*Grid
	for s.Scan() {
		line := whitespacePattern.ReplaceAllString(s.Text(), "")
		if g := NewGrid(line); g != nil {
			out = append(out, g)
		}
		break
	}

	return out
}

func GetGridIndex(x int, y int) int {
	if !(x >= 1 && x <= 9 && y >= 1 && y <= 9) {
		panic("invalid coords")
	}
	return (y * 9) + x
}

func GetGridCoords(i int) (int, int) {
	if !(i >= 1 && i <= 81) {
		panic("invalid index")
	}
	return ((i - 1) % 9) + 1, ((i - 1) / 9) + 1
}
