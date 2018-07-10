XSize = 1024;
XName = "X";
YSize = 1024;
YName = "Y";
HasClass = 1;
CName = "Type";

newImage("Mask", "16-bit black", XSize, YSize, 1);
for(i=0;i<nResults;i++)
{
	XPos = getResult(XName,i);
	YPos = getResult(YName,i);
	if(HasClass==0)setPixel(XPos,YPos,65535);	
	else
	{
		Class = parseInt(getResult(CName,i));
		setPixel(XPos,YPos,Class);
	}
}