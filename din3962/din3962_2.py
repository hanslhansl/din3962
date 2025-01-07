from din3962 import GearToothQuality


def Deviations(q : GearToothQuality, b : float):
    """F_β, f_Hβ, f_βf"""
    if b <= 20:
        match q:
            case GearToothQuality.DIN1:
                return 2.5, 2., 1.5
            case GearToothQuality.DIN2:
                return 3.5, 2.5, 2.5
            case GearToothQuality.DIN3:
                return 4.5, 3., 3.
            case GearToothQuality.DIN4:
                return 5.5, 4., 3.5
            case GearToothQuality.DIN5:
                return 7., 6., 4.5
            case GearToothQuality.DIN6:
                return 9., 8., 5.5
            case GearToothQuality.DIN7:
                return 13., 11., 7.
            case GearToothQuality.DIN8:
                return 18., 16., 9.
            case GearToothQuality.DIN9:
                return 28., 25., 14.
            case GearToothQuality.DIN10:
                return 45., 36., 25.
            case GearToothQuality.DIN11:
                return 71., 56., 40.
            case GearToothQuality.DIN12:
                return 110., 90., 63.
    elif b <= 40:
        match q:
            case GearToothQuality.DIN1:
                return 3., 2., 2.
            case GearToothQuality.DIN2:
                return 4., 2.5, 3.
            case GearToothQuality.DIN3:
                return 5., 3.5, 4.
            case GearToothQuality.DIN4:
                return 6., 4.5, 5.
            case GearToothQuality.DIN5:
                return 8., 6.5, 6.
            case GearToothQuality.DIN6:
                return 10., 9., 7.
            case GearToothQuality.DIN7:
                return 15., 13., 9.
            case GearToothQuality.DIN8:
                return 20., 18., 12.
            case GearToothQuality.DIN9:
                return 32., 28., 18.
            case GearToothQuality.DIN10:
                return 50., 40., 28.
            case GearToothQuality.DIN11:
                return 80., 63., 45.
            case GearToothQuality.DIN12:
                return 125., 100., 71.
    elif b <= 100:
        match q:
            case GearToothQuality.DIN1:
                return 4., 2.5, 3.
            case GearToothQuality.DIN2:
                return 5., 3., 4.
            case GearToothQuality.DIN3:
                return 6., 4., 5.
            case GearToothQuality.DIN4:
                return 8., 5., 6.
            case GearToothQuality.DIN5:
                return 10., 7., 7.
            case GearToothQuality.DIN6:
                return 12., 10., 9.
            case GearToothQuality.DIN7:
                return 18., 14., 12.
            case GearToothQuality.DIN8:
                return 25., 20., 18.
            case GearToothQuality.DIN9:
                return 40., 28., 28.
            case GearToothQuality.DIN10:
                return 63., 45., 45.
            case GearToothQuality.DIN11:
                return 100., 71., 63.
            case GearToothQuality.DIN12:
                return 160., 110., 110.
    elif b <= 160:
        match q:
            case GearToothQuality.DIN1:
                return 5., 3., 4.
            case GearToothQuality.DIN2:
                return 6., 3.5, .5
            case GearToothQuality.DIN3:
                return 8., 4.5, 7.
            case GearToothQuality.DIN4:
                return 10., 6., 8.
            case GearToothQuality.DIN5:
                return 12., 8., 9.
            case GearToothQuality.DIN6:
                return 16., 11., 12.
            case GearToothQuality.DIN7:
                return 22., 16., 16.
            case GearToothQuality.DIN8:
                return 32., 22., 25.
            case GearToothQuality.DIN9:
                return 50., 32., 40.
            case GearToothQuality.DIN10:
                return 80., 50., 63.
            case GearToothQuality.DIN11:
                return 125., 80., 100.
            case GearToothQuality.DIN12:
                return 200., 125., 160.
    else:
        match q:
            case GearToothQuality.DIN1:
                return 5., 3., 4.
            case GearToothQuality.DIN2:
                return 6., 3.5, 5.
            case GearToothQuality.DIN3:
                return 8., 4.5, 7.
            case GearToothQuality.DIN4:
                return 10., 6., 8.
            case GearToothQuality.DIN5:
                return 12., 8., 9.
            case GearToothQuality.DIN6:
                return 16., 11., 12.
            case GearToothQuality.DIN7:
                return 22., 16., 16.
            case GearToothQuality.DIN8:
                return 32., 22., 25.
            case GearToothQuality.DIN9:
                return 50., 32., 40.
            case GearToothQuality.DIN10:
                return 80., 50., 63.
            case GearToothQuality.DIN11:
                return 125., 80., 100.
            case GearToothQuality.DIN12:
                return 200., 125., 160.