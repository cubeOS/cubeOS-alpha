package hardware

//Maps the LEM1802 from a given index (currently always 0) to the *[384]uint as video RAM.
func MapLEM1802(index uint, videoRAM *[]uint) {
	//if len(videoRAM) != 384 {
	//	return //if the videoRAM is not exactly 384 words long,
		//then return without doing anything
	//}
	calls := *((*([]*func(uint, *[]uint) )) (8))
	return calls[17](index, videoRAM)
}
