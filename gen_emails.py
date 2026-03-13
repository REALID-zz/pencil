import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

BASE = 'd:/Workspace/pencil'
SUB = os.path.join(BASE, 'submission')

def make_eml(to, subject, body_html, attachments, filename):
    msg = MIMEMultipart()
    msg['From'] = 'hihelloaikenni@gmail.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body_html, 'html', 'utf-8'))
    for img_path, img_name in attachments:
        if os.path.exists(img_path):
            with open(img_path, 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-Disposition', 'attachment', filename=img_name)
                msg.attach(img)
    eml_path = os.path.join(BASE, filename)
    with open(eml_path, 'w', encoding='utf-8') as f:
        f.write(msg.as_string())
    size = os.path.getsize(eml_path) / 1024 / 1024
    print(f'Created: {filename} ({size:.1f}MB)')

PORTFOLIO = 'https://realid-zz.github.io/pencil/'

ARTIST_BIO = """<p>My name is <b>Mengzhen Yang</b> (b. 1993, Ma'anshan, Anhui, China). I am a visual artist working primarily in oil painting. My large-scale works are built through aggressive palette-knife impasto technique over months and years. My painting "I Am a Growth" took over three years of continuous creation.</p>
<p>My practice spans oil painting, charcoal drawing, watercolor, digital illustration, and generative art. Each painting takes months to years to complete.</p>
<p>Online Portfolio: <a href="{url}">{url}</a></p>""".format(url=PORTFOLIO)

SIGN = """<p>Best regards,<br><b>Mengzhen Yang</b><br>hihelloaikenni@gmail.com</p>"""

paint_imgs = [
    (f'{SUB}/painting/Jungle_Descent.jpg', 'Jungle_Descent.jpg'),
    (f'{SUB}/painting/Crimson_Sovereign.jpg', 'Crimson_Sovereign.jpg'),
    (f'{SUB}/painting/I_Am_a_Growth.jpg', 'I_Am_a_Growth.jpg'),
    (f'{SUB}/painting/Achilla.jpg', 'Achilla.jpg'),
    (f'{SUB}/drawing/Horse_Study.jpg', 'Horse_Study.jpg'),
]

# 1. Noname Studio Shanghai
make_eml(
    'noname.studio@yahoo.com',
    'Artist Residency Application - Mengzhen Yang',
    f"""<div style="font-family:Arial,sans-serif;font-size:14px;line-height:1.8;color:#333">
<p>Dear Noname Studio Team,</p>
<p>I am writing to apply for an artist residency at Noname Studio in Zhujiajiao.</p>
{ARTIST_BIO}
<h3>Residency Proposal</h3>
<p>I would like to apply for a <b>2-month residency</b> beginning at your earliest available date. I plan to create a new series of 3-4 large-scale oil paintings (120-180 cm) exploring the threshold between figuration and abstraction. The series centers on floating human figures painted through aggressive impasto technique. This continues the trajectory of my recent works "Crimson Sovereign" and "Jungle Descent."</p>
<p>The 300 sqm studio at Noname would be ideal for the physical scale and intensity my practice demands.</p>
<p>I have attached images of five recent works. I would be happy to donate one work to the Noname Studio Foundation collection as part of the residency terms.</p>
<p>Thank you for your consideration.</p>
{SIGN}
</div>""",
    paint_imgs,
    'EMAIL-1-Noname-Studio.eml'
)

# 2. Corridor Foundation Shenzhen
make_eml(
    'info@corridorfoundation.com',
    'International Artist Residency Inquiry - Mengzhen Yang',
    f"""<div style="font-family:Arial,sans-serif;font-size:14px;line-height:1.8;color:#333">
<p>Dear Corridor Foundation Team,</p>
<p>I am a Chinese visual artist working primarily in large-scale oil painting. I am writing to inquire about your International Artist Residency Program in Shenzhen.</p>
{ARTIST_BIO}
<p>Could you please let me know:</p>
<ol>
<li>Is the residency currently accepting applications for 2026-2027?</li>
<li>What materials are required for the application?</li>
</ol>
<h3>Proposed Project</h3>
<p>I would use the residency to develop a new series of large-scale oil paintings exploring the tension between figuration and abstraction. My recent works "Crimson Sovereign" and "Jungle Descent" represent this direction.</p>
<p>I have attached images of recent works.</p>
{SIGN}
</div>""",
    paint_imgs[:3],
    'EMAIL-2-Corridor-Shenzhen.eml'
)

# 3. Serlachius Finland (deadline March 31)
make_eml(
    'residency@serlachius.fi',
    'Residency Application Inquiry 2027 - Mengzhen Yang, Visual Artist',
    f"""<div style="font-family:Arial,sans-serif;font-size:14px;line-height:1.8;color:#333">
<p>Dear Serlachius Residency Team,</p>
<p>I am writing to apply for the Serlachius Residency 2027. I understand the application deadline is March 31, 2026.</p>
{ARTIST_BIO}
<h3>Project Description</h3>
<p>I plan to use the Serlachius Residency to develop a new series of oil paintings exploring the tension between figuration and abstraction. Working with palette knife and impasto technique, I will create 3-4 medium-to-large scale works (80-150 cm) that investigate the moment when a recognizable form dissolves into pure material.</p>
<p>The Serlachius Museum's collection of Finnish art offers a meaningful context for my work. The quiet, focused environment and the converted Art Nouveau pharmacy studios would provide the sustained concentration my slow, physically intensive painting process demands.</p>
<p><b>Requested duration:</b> 2 months, any period in 2027.</p>
<p>I have attached images of recent works. Could you please confirm if email applications are accepted, or direct me to the online form?</p>
{SIGN}
</div>""",
    paint_imgs[:4],
    'EMAIL-3-Serlachius-Finland.eml'
)

print('\nAll 3 emails generated!')
print('Files are in d:/Workspace/pencil/')
print('Double-click each .eml file -> it opens in your email client -> click Send')
