for i in 2 3 4
do
	ffmpeg -r 30 -f image2 -s 512x512 -i samples/brainimaging_256/111${i}/interpZY0%d.png -vcodec libx264 -crf 15 -pix_fmt yuv420p brainimaging${i}.mp4
done