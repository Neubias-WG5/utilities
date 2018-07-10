XSize = 256;
XName = "X";
YSize = 256;
YName = "Y";
ZSize = 100;
ZName = "Z";
HasClass = 0;
CName = "C3";

newImage("Mask", "16-bit black", XSize, YSize, ZSize);
for(i=0;i<nResults;i++)
{
	XPos = getResult(XName,i);
	YPos = getResult(YName,i);
	if(ZSize > 1)
	{
		ZPos = getResult(ZName,i);
		setZCoordinate(ZPos-1);
	}
	if(HasClass==0)setPixel(XPos,YPos,65535);	
	else
	{
		Class = parseInt(getResult(CName,i));
		setPixel(XPos,YPos,Class);
	}
}