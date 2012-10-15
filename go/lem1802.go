package lem1802

import "hardware"

type LEM1802 struct {
	index uint
	screen []uint
}

//Returns a new LEM1802 object with initialized screen and port, and maps the video RAM.
func NewLEM1802(index uint) LEM1802 {
	lem := new(LEM1802) //Make a new LEM1802 object,
	lem.index = index //set the index,
	lem.screen = new([]uint, 384) //reserve video RAM,
	//hardware.MapLEM1802(index, *lem.screen) //map the screen,
	return lem //and return it.
}

//Writes to the screen of a given LEM1802 at the given screen index, using the given characters (including color codes.) If the write fails due to lack of screen length, it will return false. Otherwise, it will return true.
//func WriteToLEM1802(lem LEM1802, screenIndex uint, characters []uint) bool {
//	if screenIndex + len(characters) > 384 {
//		//If the screen isn't long enough,
//		return false //then return false.
//	}
//	copy(characters, lem.screen)
//}
