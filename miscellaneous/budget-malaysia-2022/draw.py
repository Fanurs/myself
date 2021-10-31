import inspect
import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read in data
with open('initiative-1.json', 'r') as file:
    content = json.load(file)
df1 = pd.DataFrame(content).transpose()
df1.sort_values('budget', ascending=True, inplace=True)

with open('initiative-2.json', 'r') as file:
    content = json.load(file)
df2 = pd.DataFrame(content).transpose()
df2.sort_values('budget', ascending=True, inplace=True)

R = np.sqrt((sum(df1.budget) + sum(df2.budget)) / sum(df2.budget))

fig, ax = plt.subplots(dpi=100, figsize=(8, 7.5), constrained_layout=True, facecolor='black')
def annotate(text, xy, bg=False, **kwargs):
    global ax
    kwargs.setdefault('fontsize', 10)
    kwargs.setdefault('ha', 'center')
    kwargs.setdefault('va', 'center')
    if bg:
        kwargs.setdefault('bbox', dict(facecolor='black'))
    ax.text(xy[0], xy[1], text, **kwargs)

annotate('Budget 2022 Malaysia', (-3.35, 9.8), color='white', ha='left', fontsize=16, weight='bold')
annotate(inspect.cleandoc("""
    Summary chart for the two racial
    based Initiatives under Strategy 2,
    "Membangun sebuah keluarga Malaysia"
    (Cultivating Family Malaysia)
    """),
    (-3.35, 8.8),
    color='white',
    ha='left',
    fontsize=11,
)


# initiative 2: non-bumi
df = df2.copy()
ax.pie(
    df.budget,
    explode=[0.8, 0.5, 0.3, 0.05, 0.05, 0.05],
    startangle=100,
    colors=df.color,
    radius=1,
    center=(0, 0),
)
theta = np.radians(13)
dw = R * np.sin(theta)
ax.plot([-1.2 - dw, R + 0.2], [-1.0 + dw, R + 0.15], color='white', linestyle='dotted', zorder=0)
ax.plot([-1.2 + dw, R + 0.35], [-1.2 - dw, R + 0.1], color='white', linestyle='dotted', zorder=0)
annotate('Children in\nSabah & Sarawak', (-0.6, 2.2), color=df.loc['ss_children', 'color'])
annotate('Rukun Tetangga\nArea (KRT)', (-1.5, 1.6), color=df.loc['krt', 'color'])
annotate('Non-Muslim\nhouses of worship', (-2.3, 1.0), color=df.loc['non_muslim', 'color'])
annotate('Indian\nCommunity', (-1.85, -0.15), color=df.loc['indian', 'color'], bg=True)
annotate('Chinese\nCommunity', (0.0, -1.4), color=df.loc['chinese', 'color'], bg=True)
annotate('Orang\nAsli', (1.5, -0.1), color=df.loc['asli', 'color'], bg=True)
annotate(f'{df.loc["asli", "budget"]:,.0f}\njuta', (0.5, 0.35))
annotate(f'{df.loc["chinese", "budget"]:,.0f}\njuta', (0.05, -0.6))
annotate(f'{df.loc["indian", "budget"]:,.0f}\njuta', (-0.65, -0.1))
annotate(inspect.cleandoc(f"""
    Initiative 2
    "Pembangunan Semua Kaum"
    Total: {sum(df2.budget):,.0f} juta ({1e2*sum(df2.budget)/(sum(df1.budget) + sum(df2.budget)):.1f}%)
    """),
    (-0.8, -2.4), color='white', fontsize=12, bg=True, weight='bold')


# initiative 1: bumi
df = pd.concat([df1, df2])
explode = [1.0 if i in df2.index else 0.1 for i in df.index]
explode[0] = 0.5
ax.pie(
    df.budget,
    explode=explode,
    startangle=233.5,
    colors=df.color,
    radius=R,
    center=(R + 0.6, R + 0.4),
    frame=True,
)
annotate(f'Education for Bumiputera\n{df.loc["education", "budget"]:,.0f} juta', (4.2, 7.5), color='white', fontsize=14)
annotate(inspect.cleandoc("""
    Includes MARA, UiTM and Yayasan
    Peneraju. To produce more
    Bumiputera professionals in the
    areas of medicine, engineering
    and finance.
    """),
    (4.0, 6.2), color='lightgray')

annotate(f'Capacity building\n& funding programmes\n{df.loc["building", "budget"]:,.0f} juta', (7.3, 4.8), color='white', fontsize=14)
annotate(inspect.cleandoc("""
    Perbadanan Usahawan Nasional
    Berhad, TEKUN Nasional and
    Dana Kemakmuran Bumiputera
    """),
    (7.2, 3.7), color='lightgray')

annotate(f'Pillar of\nIslam\n{df.loc["islam", "budget"]:,.0f} juta', (4.3, 2.0), color='white', fontsize=14)

annotate('Bumiputera\nyouths', (2.7, 0.3), color=df.loc['youth', 'color'])

annotate(inspect.cleandoc(f"""
    *Initiative 1
    "Pembangunan Bumiputera & Syiar Islam"
    Total: {sum(df1.budget):,.0f} juta ({1e2*sum(df1.budget)/(sum(df1.budget) + sum(df2.budget)):.1f}%)
    """),
    (6.2, -0.5), color='white', fontsize=14, weight='bold')
annotate('*Only includes projects with budget > 100 juta',
    (7.9, -1.3), color='gray', ha='right')


# demographics 2021 est.
annotate('Demographics 2021 (est.)', (-3.35, 6.3), ha='left', va='top', color='white', weight='bold')
annotate(inspect.cleandoc("""
    Malay: 56.6%
    Other Bumiputera: 13.1%
    Chinese: 22.5%
    Indian: 6.8%
    Others: 1.0%
    """),
    (-3.35, 6),
    ha='left', va='top',
    color='white',
    # bbox=dict(boxstyle='round', facecolor='dimgray', alpha=0.5),
)


# references and design
annotate(inspect.cleandoc("""
    References:
    - https://budget.mof.gov.my/2022
    - https://www.theedgemarkets.com/article/full-budget-2022-speech
    - https://www.dosm.gov.my
    """),
    (3.5, -2.4), color='silver', ha='left', fontsize=8)

img = plt.imread('logo-b2022-dark.png')
newax = fig.add_axes([0.8, 0.8, 0.2, 0.2], anchor='NE', zorder=-1)
newax.imshow(img)
newax.axis('off')

ax.axis('equal')
fig.savefig('budget2022.png', dpi=500, facecolor='black')
plt.show()
