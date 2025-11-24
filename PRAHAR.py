import math
import time
import random

PI = math.pi
tnt = 4.184e15  # Joules in 1 MT TNT
hiroshima = 0.015

# interior width for readable output
width = 60

# asteroid density
Dens = {'C': {'name': 'C-type (Carbonaceous)', 'density': 1500, 'desc': '🪨 Dark, carbon-rich.'},
    'S': {'name': 'S-type (Stony)', 'density': 3000, 'desc': '🗿 Rocky, silicate-rich.'},
    'M': {'name': 'M-type (Metallic)', 'density': 7800, 'desc': '⚙️ Iron-nickel core.'}}

Historical = [{'name': 'Chelyabinsk', 'year': 2013, 'size': 20, 'energy': 0.5, 'desc': '💥 1,500 injured.'},
    {'name': 'Tunguska', 'year': 1908, 'size': 60, 'energy': 10, 'desc': '🌲 Flattened 2,000 km².'},
    {'name': 'Meteor Crater', 'year': -50000, 'size': 50, 'energy': 10, 'desc': '🕳️ Created 1.2 km crater.'},
    {'name': 'Chicxulub', 'year': -66000000, 'size': 10000, 'energy': 100000000, 'desc': '🦕 Mass extinction.'}]

# ISRO Observatory names 
ISRO_Obs = [ 'NETRA (Network for Space Objects Tracking)',
    'Devasthal Observatory, Uttarakhand',
    'Mount Abu Observatory, Rajasthan', 
    'Indian Astronomical Observatory, Hanle, Ladakh']

# INDIAN asteroid name prefixes 
Indian_names = ['Ashani', 'Vajra', 'Agni', 'Rudra', 'Kaal', 'Vinash', 'Pralaya', 'Mahakal']

# MAKE THE SH!T INTERESTING

def clear_screen():
    print('\n' * 3)


def slow_print(text, delay=0.006):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()


def wrap_words(s, width=width):
    s = s.strip()
    if not s:
        return ['']
    words = s.split()
    lines = []
    cur = words[0]
    for w in words[1:]:
        if len(cur) + 1 + len(w) <= width:
            cur += ' ' + w
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    return lines


def title_line(t):
    print('\n' + '=' * width)
    print(t.center(width))
    print('=' * width + '\n')


def section(title, content):
    if isinstance(content, str):
        content = [content]
    head = f"-- {title} "
    print(head.ljust(width, '-'))
    for ln in content:
        for part in wrap_words(str(ln)):
            print(part)
    print('-' * width + '\n')


# PHYSICS CALCULATIONS

def vol_sphere(d):#DIAMETER
    r = d / 2
    return (4/3) * PI * (r ** 3)


def mass_from(vol, dens):
    return vol * dens


def ke(mass, vel):
    return 0.5 * mass * (vel ** 2)


def to_megatons(j):#joules  
    return j /tnt


def crater_est(mt):
    return 1000 * (mt ** (1/3)) if mt > 0 else 0


def richter_est(mt):
    if mt <= 0:
        return 0
    return 0.67 * math.log10(mt) + 5.87


def fireball_r(mt):
    return 140 * (mt ** 0.4) if mt > 0 else 0


def hazard_level(mt):
    # returns a small dict describing expected consequences
    if mt < 1:
        return {'level': 'LOCAL EVENT', 'color': '🟢 GREEN', 'desc': 'Minor regional damage.',
                'effects': [f'💥 Blast radius: ~{fireball_r(mt)/1000:.2f} km', '🏢 Building damage nearby']}
    if mt < 100:
        return {'level': 'REGIONAL THREAT', 'color': '🟡 YELLOW', 'desc': 'Large city destruction likely.',
                'effects': [f'💥 Blast radius: ~{fireball_r(mt)/1000:.2f} km', '🌆 Severe damage tens of km away']}
    if mt < 10000:
        return {'level': 'GLOBAL CATASTROPHE', 'color': '🔴 RED', 'desc': 'Widespread devastation.',
                'effects': [f'💥 Blast radius: ~{fireball_r(mt)/1000:.2f} km', '❄️ Possible impact winter']}
    return {'level': 'EXTINCTION LEVEL EVENT', 'color': '🟣 PURPLE', 'desc': 'Biosphere collapse possible.',
            'effects': ['☠️ GAME OVER FOR MOST LIFE', f'💥 Blast radius: ~{fireball_r(mt)/1000:.2f} km']}


def find_similar(mt):
    best = None
    bestd = float('inf')
    for e in Historical:
        v = max(mt, 0.001)
        d = abs(math.log10(e['energy']) - math.log10(v))
        if d < bestd:
            bestd = d
            best = e
    return best


# USER INTERACTION 

def intro():
    clear_screen()
    title_line('🇮🇳 P.R.A.H.A.R. — Planetary Risk Assessment for Hazardous Asteroid Reentry 🇮🇳')
    slow_print('🛰️ A scientific initiative by ISRO')


def detect():
    title_line('⚠️ PHASE 1: DETECTION ⚠️')
    obs = random.choice(ISRO_Obs)
    asteroid_name = random.choice(Indian_names)
    obj_id = random.randint(1000, 9999)
    full_name = f"{asteroid_name}-{obj_id}"

    slow_print(f'🚨 ALERT: Detected by {obs}')
    slow_print(f'📡 Object: {full_name}')
    slow_print('⚠️ STATUS: Potential Earth impactor')
    print('\n' + '-' * width + '\n')

    while True:
        try:
            d = float(input('📏 Enter asteroid DIAMETER (metres): '))
            if d <= 0:
                print('❌ Diameter must be positive')
                continue
            return d, full_name   #return name too
        except ValueError:
            print('❌ Enter a valid number')



def analyze():
    title_line('🔬 PHASE 2: SPECTRUM ANALYSIS 🔬')
    slow_print('🔍 Analyzing...')
    time.sleep(0.4)
    for k in ['C', 'S', 'M']:
        v = Dens[k]
        section(f'[{k}] {v["name"]}', [v['desc'], f"⚖️ Density: {v['density']} kg/m3"]) 
    while True:
        ch = input('🎯 Select type [C/S/M]: ').upper()
        if ch in Dens:
            section('✅ CONFIRMED', f"{Dens[ch]['name']} (Density: {Dens[ch]['density']})")
            return ch
        print('❌ Invalid. Choose C, S or M')


def trajectory():
    title_line('🎯 PHASE 3: TRAJECTORY 🎯')
    slow_print('🧮 Computing approach vector...')
    time.sleep(0.4)
    while True:
        try:
            v_km = float(input('⚡ Enter impact VELOCITY (km/s): '))
            if v_km <= 0:
                print('❌ Velocity must be positive')
                continue
            v_ms = v_km * 1000
            section('🚀 SPEED', [f'⚡ {v_km:.1f} km/s', f'🔊 Mach: {v_ms/343:.1f}'])
            return v_ms
        except ValueError:
            print('❌ Enter a number')


def simulate(d, atype, velocity):
    title_line('💥 PHASE 4: IMPACT SIMULATION 💥')
    slow_print('🔬 RUNNING PHYSICS SIMULATION...')
    time.sleep(0.4)
    vol = vol_sphere(d)
    dens = Dens[atype]['density']
    m = mass_from(vol, dens)
    energy = ke(m, velocity)
    mt = to_megatons(energy)
    crater = crater_est(mt)
    r = richter_est(mt)
    fb = fireball_r(mt)
    return {'mass': m, 'mt': mt, 'crater': crater, 'richter': r, 'fireball': fb}


def report(d, atype, velocity, res, asteroid_full_name):
    title_line('📊 IMPACT REPORT 📊')
    section('🎯 OBJECT', asteroid_full_name)
    section('📐 PHYSICAL', 
            [f'📏 Diameter: {d:.0f} m', 
             f'🪨 type: {Dens[atype]["name"]}', 
             f'⚖️ Mass: {res["mass"]:.2e} kg', 
             f'⚡ Velocity: {velocity/1000:.1f} km/s'])
    mt = res['mt']
    section('⚡ ENERGY', 
            [f'💣 {mt:,.1f} megatons', 
             f'☢️ ~{(mt/hiroshima):,.0f} Hiroshima bombs'])
    sim = find_similar(mt)
    if sim:
        section('📚 Historical SIMILAR', 
                f"{sim['name']} ({'year '+str(sim['year']) if sim['year']>0 else str(abs(sim['year']))+' years ago'})")
    section('🕳️ CRATER', 
            f"📏 Estimated diameter: {res['crater']/1000:.2f} km")
    if res['richter'] > 0:
        section('🌊 SEISMIC', 
                f"📈 Magnitude: {res['richter']:.1f}")
    haz = hazard_level(mt)
    section(f"⚠️ THREAT: {haz['color']} {haz['level']}", 
            [haz['desc']] + haz['effects'])


def options():
    print('\n' + '-' * width)
    print('🔄 1) Run again   🚪 2) Exit')
    while True:
        c = input('Choose [1/2]: ').strip()
        if c in ('1', '2'):
            return c
        print('❌ Choose 1 or 2')


def main():
    intro()
    while True:
        d, asteroid_full_name = detect()
        t = analyze()
        v = trajectory()
        r = simulate(d, t, v)
        report(d, t, v, r, asteroid_full_name)
        if options() == '2':
            print('\n' + '=' * width)
            slow_print('\n Stay vigilant.\n')
            break


if __name__ == "__main__":
    main()
