package main

import (
	"github.com/jbmmhk/sudoku/internal/sudoku"
	log "github.com/sirupsen/logrus"
)

func main() {
	log.SetFormatter(&log.TextFormatter{
		ForceColors: true,
	})
	grids := sudoku.LoadGridsFromFile("./puzzles/main.txt")
	for i := range grids {
		log.Info("Grid: ", i)
		grids[i].Print()
	}
}
