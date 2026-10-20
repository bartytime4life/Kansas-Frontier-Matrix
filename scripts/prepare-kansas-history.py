"""Render sourced Kansas history as silent, 1080p cartographic short films.

Requires Pillow and FFmpeg. Pass the FFmpeg executable as argv[1]. Archive
plates remain intact; animation belongs to the map locator and event timeline.
Connections are schematic, never asserted to be exact routes or troop positions.
"""
import json
import math
import pathlib
import subprocess
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = pathlib.Path(__file__).resolve().parents[1]
FF = sys.argv[1]
OUT = ROOT / 'public/welcome/motion'
CHAPTERS = json.loads((ROOT / 'app/living-welcome/kansas-history.json').read_text())
W, H, FPS, SECONDS = 1920, 1080, 30, 8
NAVY, INK, GOLD, TEAL, WHITE = '#092532', '#04151e', '#f0c979', '#78c6c6', '#eaf1ed'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SERIF = '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'

def font(size, bold=False, serif=False):
    return ImageFont.truetype(SERIF if serif else BOLD if bold else FONT, size)

def geo(lon, lat):
    # Local equirectangular locator. Longitude scale follows the parallel at
    # 38.5 N so the Kansas outline retains its geographic aspect ratio.
    return (round(100 + (lon + 102.2) * 110 * math.cos(math.radians(38.5))),
            round(730 - (lat - 37) * 110))

# Simplified geographic outline, including the Missouri River boundary.
STATE = [(-102.052,37),(-94.618,37),(-94.618,38.99),(-94.6,39.12),
         (-94.76,39.2),(-94.89,39.27),(-94.98,39.37),(-95.06,39.49),
         (-95.1,39.57),(-95.2,39.61),(-95.18,39.76),(-95.31,39.86),
         (-95.31,40),(-102.052,40)]

def make_background(chapter, index):
    im = Image.new('RGB', (W, H), INK)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((36,36,1884,1044),radius=28,fill=NAVY,outline='#41616b',width=2)
    d.text((90,78),'KANSAS  /  STORIES THROUGH TIME',font=font(22,True),fill=TEAL)
    d.text((90,133),chapter['heading'],font=font(51,False,True),fill=WHITE)
    d.text((92,211),chapter['place'],font=font(24),fill='#aac6cc')
    d.line((90,268,1830,268),fill='#36535f',width=2)
    # Cartographic field. Longitude/latitude grid, not invented county borders.
    for lon in range(-102,-94):
        a,b=geo(lon,37),geo(lon,40.6);d.line((a,b),fill='#183d49',width=1)
    for lat in [37,38,39,40]:
        a,b=geo(-102.2,lat),geo(-94.2,lat);d.line((a,b),fill='#183d49',width=1)
    pts=[geo(*p) for p in STATE]
    d.polygon(pts,fill='#173c46');d.line(pts+[pts[0]],fill='#779a98',width=3)
    d.text((185,466),'K A N S A S',font=font(37,True),fill='#40626a')
    d.text((120,316),chapter['era'],font=font(48,False,True),fill=GOLD)
    d.text((96,758),'SCHEMATIC LOCATORS · APPROXIMATE PLACES',font=font(16),fill='#a7bfc1')
    # An archival plate is evidence, not a simulated camera view of the event.
    plate=Image.open(ROOT/'scripts/welcome-history/source-images'/f"{chapter['asset']}.jpg").convert('RGB')
    plate=ImageOps.contain(plate,(790,434),Image.Resampling.LANCZOS)
    px,py=1050+(790-plate.width)//2,315+(434-plate.height)//2
    d.rounded_rectangle((1030,295,1860,770),radius=9,fill='#071c25',outline='#4b646b',width=2)
    im.paste(plate,(px,py))
    d.text((1051,793),chapter['imageLabel'],font=font(20),fill='#c6d7d5')
    # Leave room for the animated timeline, using comfortable reading sizes.
    for n,line in enumerate(textwrap.wrap(chapter['summary'],width=100)):
        d.text((92,855+n*31),line,font=font(24),fill=WHITE)
    d.text((92,1005),f"{index+1:02} / 06    ARCHIVAL IMAGE + ANIMATED EVENT MAP",font=font(16),fill='#9dbac0')
    return im

for index, chapter in enumerate(CHAPTERS):
    if len(sys.argv) > 2 and chapter['asset'] not in sys.argv[2:]:
        continue
    background=make_background(chapter,index)
    dest=OUT/f"{chapter['asset']}-hd.webm"
    process=subprocess.Popen([FF,'-y','-hide_banner','-loglevel','error','-f','rawvideo','-vcodec','rawvideo',
        '-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','pipe:0','-an','-c:v','libvpx-vp9',
        '-crf','27','-b:v','0','-deadline','good','-cpu-used','5','-row-mt','1','-threads','2',str(dest)],stdin=subprocess.PIPE)
    places=chapter['places']
    for frame in range(FPS*SECONDS):
        t=frame/FPS;phase=min(2,int(t/2.5));im=background.copy();d=ImageDraw.Draw(im)
        # Follow the selected place in a repeating locator orbit. The graphic
        # points to actual Kansas places; it does not fabricate historical motion.
        for n,(label,lon,lat) in enumerate(places):
            x,y=geo(lon,lat);active=n==phase%len(places)
            if active:
                radius=19+8*math.sin(t*1.4)**2
                d.ellipse((x-radius,y-radius,x+radius,y+radius),outline=TEAL,width=2)
                a=t*1.4;cx,cy=x+radius*math.cos(a),y+radius*math.sin(a)
                d.ellipse((cx-4,cy-4,cx+4,cy+4),fill=GOLD)
            d.ellipse((x-5,y-5,x+5,y+5),fill=GOLD if active else TEAL)
            # Offset nearby labels to avoid collisions in eastern Kansas.
            if chapter['asset']=='kansas-territory':
                dx,dy=[(-155,-55),(-120,28),(-125,43)][n]
                lx,ly=x+dx,y+dy
                d.line((x,y,lx+70,ly+14),fill='#577983',width=1)
            else:
                ly=y-35 if n%2==0 else y+13
                lx=x-15 if x<700 else x-145
            box=d.textbbox((lx,ly),label,font=font(22,True));d.rounded_rectangle((box[0]-6,box[1]-3,box[2]+6,box[3]+3),radius=4,fill=INK)
            d.text((lx,ly),label,font=font(22,True),fill=WHITE)
        # A chronological reveal is the action, rather than distorting an image.
        for step in range(3):
            x=96+step*584;y=960;done=step<=phase
            d.line((x,y,x+530,y),fill='#42626a',width=3)
            local=max(0,min(1,(t-step*2.5)/2.5))
            if done:d.line((x,y,x+530*local,y),fill=GOLD,width=4)
            d.ellipse((x-5,y-5,x+5,y+5),fill=GOLD if done else '#42626a')
            d.text((x,922),chapter['steps'][step],font=font(21,step==phase),fill=WHITE if step==phase else '#8ca9af')
        if frame==45:im.save(OUT/f"{chapter['asset']}.jpg",quality=92)
        process.stdin.write(im.tobytes())
    process.stdin.close()
    if process.wait():raise RuntimeError(f"Encoding failed: {chapter['asset']}")
    subprocess.run([FF,'-y','-hide_banner','-loglevel','error','-i',str(dest),'-vf','scale=480:270',
        '-an','-c:v','libvpx-vp9','-crf','32','-b:v','0','-deadline','good','-cpu-used','5',
        '-threads','2',str(OUT/f"{chapter['asset']}-preview.webm")],check=True)
    print('Prepared',chapter['asset'],dest.stat().st_size,flush=True)
