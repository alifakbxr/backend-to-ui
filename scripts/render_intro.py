#!/usr/bin/env python3
"""Render product-ui's original motion intro as one deterministic 30fps MP4.

Input: no external images, no network, no proprietary assets.
Output: media/intro.mp4, cover.png. The GIF is encoded from the same MP4.
Uses Pillow + ffmpeg; Inter or DejaVu fonts from the runner.
"""
from __future__ import annotations

import argparse
import functools
import math
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import wave
import struct

from PIL import Image, ImageDraw, ImageFont

W, H, FPS, DURATION = 1280, 720, 30, 17.0
BG = (246, 246, 242)
INK = (26, 31, 30)
MUTED = (105, 113, 108)
LINE = (218, 221, 216)
DEEP = (31, 52, 47)
ACCENT = (73, 114, 102)
LIME = (227, 239, 183)
WHITE = (255, 255, 252)
DARKLINE = (59, 79, 70)
EASE = lambda t: t*t*(3-2*t)


def clamp(x, a=0.0, b=1.0): return min(b, max(a, x))
def tween(t, a, b): return EASE(clamp((t-a)/(b-a)))
def lerp(a, b, u): return a+(b-a)*u

def _find_font(bold=False):
    candidates = (
        ['/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf', '/usr/share/fonts/truetype/inter/Inter-Bold.otf']
        if bold else
        ['/usr/share/fonts/opentype/inter/InterDisplay-Regular.otf', '/usr/share/fonts/truetype/inter/Inter-Regular.otf']
    )
    for name in candidates:
        if os.path.isfile(name): return name
    fc = shutil.which('fc-match')
    if fc:
        family = 'Inter:style=Bold' if bold else 'Inter:style=Regular'
        path = subprocess.check_output([fc, '-f', '%{file}', family], text=True).strip()
        if os.path.isfile(path): return path
    return '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

@functools.lru_cache(maxsize=100)
def font(size, bold=False): return ImageFont.truetype(_find_font(bold), size)


def text(draw, xy, s, sz, color=INK, bold=False, anchor=None):
    draw.text((round(xy[0]), round(xy[1])), s, font=font(sz, bold), fill=color, anchor=anchor, stroke_width=0)

def rr(d, xy, r, fill, outline=None, width=1):
    d.rounded_rectangle(tuple(round(q) for q in xy), radius=r, fill=fill, outline=outline, width=width)

def label(d, xy, s, color=MUTED, size=16):
    text(d, xy, s, size, color, True)

def header(d, step):
    d.ellipse((78, 40, 103, 65), fill=DEEP)
    d.rounded_rectangle((84, 47, 97, 58), radius=2, fill=LIME)
    text(d, (116, 42), 'product-ui', 23, INK, True)
    text(d, (1201, 45), step, 13, MUTED, True, anchor='ra')
    d.line((78, 92, 1202, 92), fill=LINE, width=2)

def footer(d, line):
    d.line((78, 664, 1202, 664), fill=LINE, width=2)
    text(d,(79,680),'AN AGENT SKILL FOR REAL PRODUCTS',12,MUTED,True)
    text(d,(1201,681),line,12,MUTED,anchor='ra')


def mini_icon(d,x,y,k=0):
    col=ACCENT
    if k==0:
        d.line((x,y,x+13,y+13),fill=col,width=3);d.line((x+13,y,x,y+13),fill=col,width=3)
    elif k==1:
        d.ellipse((x,y,x+12,y+12),outline=col,width=2)
    elif k==2:
        d.rectangle((x,y+3,x+12,y+11),outline=col,width=2)
    else:
        d.line((x,y+6,x+12,y+6),fill=col,width=2)


def draw_bad_ui():
    im=Image.new('RGBA',(984,500),(250,251,251,255)); d=ImageDraw.Draw(im)
    # Generic before state deliberately illustrative, not a functioning product.
    rr(d,(1,1,982,498),20,(255,255,255),outline=(210,215,214),width=2)
    rr(d,(1,1,982,92),20,(21,35,44));d.rectangle((1,70,982,93),fill=(21,35,44))
    text(d,(29,23),'Dashboard',27,WHITE,True)
    text(d,(839,35),'Overview   Settings',13,(182,190,192))
    text(d,(31,115),'Welcome back.',33,INK,True)
    text(d,(31,159),'Here is an overview of your operations.',15,MUTED)
    for n,(ttl,val) in enumerate([('Active','24'),('Completed','18'),('Pending','6')]):
        x=30+n*311
        rr(d,(x,208,x+294,320),17,(250,251,251),outline=(229,232,232),width=2)
        text(d,(x+20,226),ttl,15,(135,141,147),True)
        text(d,(x+20,256),val,38,(53,65,74),True)
    text(d,(31,363),'Recent activity',20,(53,65,74),True)
    for k,txt in enumerate(['An item was updated', 'A new order was created', 'A task was completed']):
        y=405+k*27
        d.ellipse((34,y+3,42,y+11),fill=(183,191,198))
        text(d,(52,y),txt,13,(123,130,136))
    return im


def draw_good_ui(selected=-1):
    im=Image.new('RGBA',(984,500),(255,255,252,255));d=ImageDraw.Draw(im)
    rr(d,(1,1,982,498),19,WHITE,outline=(208,215,208),width=2)
    rr(d,(1,1,190,498),19,DEEP)
    d.rectangle((174,1,190,498),fill=DEEP)
    text(d,(25,30),'F',35,LIME,True)
    text(d,(53,36),'FIELDWORK',16,(243,247,236),True)
    label(d,(25,118),'WORKSPACE',(153,175,162),11)
    rr(d,(15,151,176,198),9,(65,91,78))
    text(d,(29,164),'Pick queue',17,WHITE,True)
    text(d,(29,223),'Inventory',16,(192,205,196))
    text(d,(29,267),'Activity',16,(192,205,196))
    d.line((20,448,170,448),fill=DARKLINE,width=2)
    text(d,(29,462),'STATION 04',12,(194,214,203),True)
    # Main workspace
    label(d,(224,32),'FULFILLMENT  /  FRIDAY 13 NOVEMBER',ACCENT,13)
    text(d,(222,62),'Pick queue',40,INK,True)
    text(d,(224,121),'Move the next order to packing.',17,MUTED)
    rr(d,(785,67,949,114),10,DEEP)
    text(d,(868,79),'Start picking',16,WHITE,True,anchor='mt')
    d.line((224,162,949,162),fill=LINE,width=2)
    label(d,(226,181),'ORDER',MUTED,12)
    label(d,(501,181),'ITEMS',MUTED,12)
    label(d,(651,181),'STATUS',MUTED,12)
    label(d,(854,181),'ACTION',MUTED,12)
    data=[('#HW-1042','12 items','Ready'),('#HW-1045','8 items','Ready'),('#HW-1047','5 items','Hold'),('#HW-1051','14 items','Ready')]
    for i,(code,count,state) in enumerate(data):
        y=211+i*64
        if i==selected: rr(d,(214,y-5,954,y+56),12,(234,241,227))
        else: d.line((224,y+54,946,y+54),fill=(234,237,233),width=1)
        text(d,(225,y+9),code,20,INK,True)
        text(d,(500,y+13),count,16,MUTED)
        rr(d,(651,y+7,740,y+38),14,(226,239,215) if state=='Ready' else (248,236,211))
        text(d,(696,y+12),state,13,DEEP if state=='Ready' else (134,88,27),True,anchor='mt')
        text(d,(853,y+11),'Open   →',16,ACCENT,True)
    text(d,(225,476),'4 orders in this illustrative queue',12,MUTED)
    return im

BAD=draw_bad_ui()
GOOD=[draw_good_ui(s) for s in (-1,1,2)]

def place_panel(base, panel, x,y,w,h,alpha=1):
    if alpha <= 0.001:return
    resized=panel.resize((int(w),int(h)), Image.Resampling.LANCZOS)
    if alpha<0.999:
        resized.putalpha(resized.getchannel('A').point(lambda v: int(v*alpha)))
    base.alpha_composite(resized,(int(x),int(y)))

def background(): return Image.new('RGBA',(W,H),BG+(255,))

def draw_progress(d, t):
    d.line((78,650,1202,650),fill=(224,227,221),width=2)
    progress=clamp(t/DURATION) if t<16.15 else 1-tween(t,16.15,16.98)
    d.line((78,650,78+int(1124*progress),650),fill=ACCENT,width=3)


def frame(t):
    canvas=background();d=ImageDraw.Draw(canvas)
    # The same identity is present throughout: no disconnected, generic text transitions.
    stage = '01 / PRINCIPLE' if t<4 or t>=16.3 else '02 / BEFORE → AFTER' if t<9.5 else '03 / REAL INTERACTION' if t<13.35 else '04 / USE THE SKILL'
    header(d,stage)
    footer(d,'backend-to-ui  /  alifakbxr/product-ui')
    draw_progress(d,t)
    if t<4.05 or t>=16.18:
        visible=(tween(t,16.28,16.94) if t>=16.18 else 1-tween(t,3.30,4.06))
        rise=0
        # animate entire message via opacity in a layer
        layer=Image.new('RGBA',(W,H),(0,0,0,0));z=ImageDraw.Draw(layer)
        label(z,(82,177+rise),'EXISTING FRONTEND. EXISTING BACKEND.',ACCENT,15)
        text(z,(76,226+rise),'Make it feel',91,INK,True)
        text(z,(76,326+rise),'made for',91,INK,True)
        text(z,(76,426+rise),'people.',91,DEEP,True)
        z.line((82,578,1197,578),fill=LINE,width=2)
        text(z,(83,597),'Less template. More product.',20,MUTED)
        if visible <1:layer.putalpha(layer.getchannel('A').point(lambda a:int(a*visible)))
        canvas.alpha_composite(layer)
    if 3.65<t<9.65:
        fadeIn=tween(t,3.68,4.15);fadeOut=1-tween(t,9.15,9.68)
        layer=Image.new('RGBA',(W,H),(0,0,0,0));z=ImageDraw.Draw(layer)
        label(z,(80,119),'A REAL TASK DESERVES A REAL INTERFACE',ACCENT,14)
        text(z,(77,146),'Keep the workflow. Change the experience.',37,INK,True)
        # single consistent canvas; before/after is an intentional wipe
        px,py,pw,ph=145,228,984,408
        if fadeIn>0:
            bad=BAD.resize((pw,ph),Image.Resampling.LANCZOS)
            good=GOOD[0].resize((pw,ph),Image.Resampling.LANCZOS)
            layer.alpha_composite(bad,(px,py))
            u=tween(t,4.45,8.30)
            cut=int(pw*u)
            if cut>0:layer.paste(good.crop((0,0,cut,ph)),(px,py))
            xx=px+cut
            z.line((xx,py-8,xx,py+ph+7),fill=ACCENT,width=4)
            z.ellipse((xx-10,py+ph//2-11,xx+10,py+ph//2+11),fill=ACCENT)
        text(z,(145,205),'BEFORE',12,MUTED,True)
        text(z,(1129,205),'AFTER',12,ACCENT,True,anchor='ra')
        if fadeIn*fadeOut<0.999:layer.putalpha(layer.getchannel('A').point(lambda v:int(v*fadeIn*fadeOut)))
        canvas.alpha_composite(layer)
    if 9.32<t<13.6:
        u=tween(t,9.35,9.72)*(1-tween(t,13.22,13.58))
        layer=Image.new('RGBA',(W,H),(0,0,0,0));z=ImageDraw.Draw(layer)
        label(z,(80,153),'PRESERVE THE LOGIC',ACCENT,15)
        text(z,(78,195),'Improve',57,INK,True)
        text(z,(78,261),'the flow.',57,DEEP,True)
        text(z,(80,380),'Your routing. Your data.',21,MUTED)
        text(z,(80,414),'Your framework.',21,MUTED)
        z.line((82,484,425,484),fill=LINE,width=2)
        text(z,(80,508),'React  /  Vue  /  Svelte',16,MUTED)
        text(z,(80,538),'and the stack you already use',16,MUTED)
        selected=1 if 10.22<=t<11.72 else 2 if t>=11.72 else 0
        px,py,pw,ph=485,180,728,380
        place_panel(layer,GOOD[selected],px,py,pw,ph)
        if selected:
            # A real user-state change, not arbitrary celebratory particles
            text(z,(486,577),'↳  Selected order changed',16,ACCENT,True)
        if u<.999: layer.putalpha(layer.getchannel('A').point(lambda v:int(v*u)))
        canvas.alpha_composite(layer)
    if t>13.27:
        u=tween(t,13.35,13.95)
        out=1-tween(t,16.08,16.45)
        layer=Image.new('RGBA',(W,H),(0,0,0,0));z=ImageDraw.Draw(layer)
        label(z,(81,176),'ONE SKILL. YOUR STACK.',ACCENT,16)
        text(z,(76,223),'backend-to-ui',92,INK,True)
        text(z,(80,340),'Product-aware frontend engineering.',27,DEEP)
        text(z,(80,389),'For the project you actually have.',27,MUTED)
        rr(z,(78,476,1198,562),15,DEEP)
        text(z,(107,504),'npx skills add alifakbxr/product-ui --skill backend-to-ui',24,WHITE)
        text(z,(82,594),'github.com/alifakbxr/product-ui',17,MUTED)
        layer.putalpha(layer.getchannel('A').point(lambda v:int(v*u*out)))
        canvas.alpha_composite(layer)
    return canvas.convert('RGB')


def make_original_soundtrack(path:Path):
    """Soft original UI sound design, no sampled or copyrighted music."""
    sr=44100
    moments=[(.42,329.63,.040),(3.85,220,.036),(4.52,261.63,.035),(8.3,392,.043),(9.7,293.66,.028),(10.45,440,.025),(11.75,392,.025),(13.7,329.63,.045),(16.35,220,.021)]
    with wave.open(str(path),'wb') as output:
        output.setnchannels(1);output.setsampwidth(2);output.setframerate(sr)
        chunk=4096;total=int(DURATION*sr)
        for start in range(0,total,chunk):
            raw=bytearray()
            for k in range(start,min(start+chunk,total)):
                t=k/sr
                # Low, subtle ambience. Two frequencies: intentionally original sound design.
                pulse=(.0025*math.sin(2*math.pi*82.41*t)+.0020*math.sin(2*math.pi*123.47*t))
                for onset,hz,amp in moments:
                    dt=t-onset
                    if 0<=dt<.45:
                        env=min(1,dt/.015)*math.exp(-dt*12.0)
                        pulse += amp*env*(math.sin(2*math.pi*hz*dt)+.26*math.sin(2*math.pi*(hz*2)*dt))
                raw += struct.pack('<h',int(max(-1,min(1,pulse))*32767))
            output.writeframesraw(raw)


def build(outdir:Path):
    outdir.mkdir(parents=True,exist_ok=True)
    ffmpeg=shutil.which('ffmpeg')
    if not ffmpeg: raise RuntimeError('ffmpeg is required')
    silent=outdir/'intro_silent.mp4'
    output=outdir/'intro.mp4'
    cmd=[ffmpeg,'-hide_banner','-loglevel','error','-y',
         '-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}',
         '-r',str(FPS),'-i','-',
         '-c:v','libx264','-preset','medium','-crf','20',
         '-pix_fmt','yuv420p','-movflags','+faststart',str(silent)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    try:
        for n in range(round(FPS*DURATION)):
            im=frame(n/FPS)
            if n==round(FPS*12.0):im.save(outdir/'cover.png')
            proc.stdin.write(im.tobytes())
    except Exception:
        proc.kill()
        raise
    finally:
        try:proc.stdin.close()
        except Exception:pass
    if proc.wait():raise RuntimeError('ffmpeg video encode failed')
    with tempfile.TemporaryDirectory(prefix='product-ui-audio-') as temp:
        audio=Path(temp)/'original-ui-sound.wav'
        make_original_soundtrack(audio)
        subprocess.run([ffmpeg,'-hide_banner','-loglevel','error','-y',
                        '-i',str(silent),'-i',str(audio),'-c:v','copy',
                        '-c:a','aac','-b:a','96k','-shortest','-movflags','+faststart',
                        str(output)],check=True)
    silent.unlink()
    print(f'Generated MP4: {output} ({output.stat().st_size:,} bytes)')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,default=Path('media'))
    args=parser.parse_args()
    build(args.out)
