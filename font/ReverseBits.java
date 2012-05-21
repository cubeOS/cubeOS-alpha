public class ReverseBits
{
	public static int reverse(int x)
	{
		int b = 0;
		while (x!=0){
			b<<=1;
			b|=( x &1);
			x>>=1;
		}
		return b;
	}
	
	public static void main(String[] args)
	{
		int n=256;
		int[] derp = new int[] {0x1286, 0xE38E, 0xB1CB, 0x51D0, 0x6722, 0x010E, 0x5E60, 0x72E5, 0xDB8B, 0xDBFF, 0xEFAB, 0xEFFF, 0xFFEF, 0xFFFF, 0xEFEF, 0xEFEF, 0xFF00, 0xFFFF, 0xFFE0, 0xEFEF, 0xEFE0, 0xFFFF, 0xEF0F, 0xFFFF, 0xFF0F, 0xEFEF, 0xFF00, 0xEFEF, 0xEFE0, 0xEFEF, 0xEF00, 0xFFFF, 0xEF0F, 0xEFEF, 0xEF00, 0xEFEF, 0x9933, 0x66CC, 0x6633, 0x99CC, 0x80E0, 0xF8FE, 0x0107, 0x1F7F, 0x7F1F, 0x0701, 0xFEF8, 0xE080, 0x55FF, 0xAAFF, 0x55AA, 0x55AA, 0x00AA, 0x0055, 0x0F0F, 0x0F0F, 0xF0F0, 0xF0F0, 0xFFFF, 0x0000, 0x0000, 0xFFFF, 0x0000, 0x0000, 0xFFFF, 0xFFFF, 0xFF05, 0xFFFF, 0x3FFF, 0x3FFF, 0x83D7, 0x83FF, 0x9B29, 0xB3FF, 0x79C7, 0x3DFF, 0x936B, 0x91F5, 0xFFBF, 0x7FFF, 0xC7BB, 0x7DFF, 0x7DBB, 0xC7FF, 0xD7EF, 0xD7FF, 0xEFC7, 0xEFFF, 0xFDFB, 0xFFFF, 0xEFEF, 0xEFFF, 0xFFFD, 0xFFFF, 0xF9C7, 0x3FFF, 0x836D, 0x83FF, 0xBD01, 0xFDFF, 0xB965, 0x9DFF, 0xBB6D, 0x93FF, 0x0FEF, 0x01FF, 0x1B5D, 0x63FF, 0x836D, 0xB3FF, 0x7967, 0x1FFF, 0x936D, 0x93FF, 0x9B6D, 0x83FF, 0xFFDB, 0xFFFF, 0xFDDB, 0xFFFF, 0xEFD7, 0xBB7D, 0xD7D7, 0xD7FF, 0x7DBB, 0xD7EF, 0xBF65, 0x9FFF, 0x8365, 0x85FF, 0x816F, 0x81FF, 0x016D, 0x93FF, 0x837D, 0xBBFF, 0x017D, 0x83FF, 0x016D, 0x7DFF, 0x016F, 0x7FFF, 0x837D, 0xA1FF, 0x01EF, 0x01FF, 0x7D01, 0x7DFF, 0xFBFD, 0x03FF, 0x01EF, 0x11FF, 0x01FD, 0xFDFF, 0x019F, 0x01FF, 0x017F, 0x81FF, 0x837D, 0x83FF, 0x016F, 0x9FFF, 0x837D, 0x82FF, 0x016F, 0x91FF, 0x9B6D, 0xB3FF, 0x7F01, 0x7FFF, 0x03FD, 0x03FF, 0x07F9, 0x07FF, 0x01F3, 0x01FF, 0x11EF, 0x11FF, 0x1FE1, 0x1FFF, 0x716D, 0x1DFF, 0xFF01, 0x7DFF, 0x3FC7, 0xF9FF, 0xFF7D, 0x01FF, 0xBF7F, 0xBFFF, 0xFEFE, 0xFEFF, 0xFF7F, 0xBFFF, 0xDBD5, 0xE1FF, 0x01DD, 0xE3FF, 0xE3DD, 0xEBFF, 0xE3DD, 0x01FF, 0xE3D5, 0xE5FF, 0xEF81, 0x6FFF, 0xEDD5, 0xC3FF, 0x01DF, 0xE1FF, 0xDD41, 0xFDFF, 0xFBFD, 0x43FF, 0x01F7, 0xC9FF, 0x7D01, 0xFDFF, 0xC1E7, 0xC1FF, 0xC1DF, 0xE1FF, 0xE3DD, 0xE3FF, 0xC1D7, 0xEFFF, 0xEFD7, 0xC1FF, 0xC1DF, 0xEFFF, 0xEDD5, 0xDBFF, 0xDF83, 0xDDFF, 0xC3FD, 0xC1FF, 0xC7F9, 0xC7FF, 0xC1F3, 0xC1FF, 0xC9F7, 0xC9FF, 0xCDF5, 0xC3FF, 0xD9D5, 0xCDFF, 0xEF93, 0x7DFF, 0xFF11, 0xFFFF, 0x7D93, 0xEFFF, 0xBF7F, 0xBF7F, 0xBF5F, 0xBFFF};
		int[] newVals = new int[n];
		
		for (int i=0;i<n;i+=2)
		{
			newVals[i+1] = reverse(derp[i]);
			newVals[i] = reverse(derp[i+1]);
			System.out.printf("0x%04X, 0x%04X, ",newVals[i],newVals[i+1]);
		}
	}
}
