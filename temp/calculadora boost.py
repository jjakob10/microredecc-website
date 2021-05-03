from getCommercialL import getCommercialL
import math


def calcBuck(Vin, Vout, Iout, Freq, _DeltaV, _DeltaI, _DeltaVin, _DeltaIin):
    DeltaV = _DeltaV/100
    DeltaI = _DeltaI/100
    DeltaVin = _DeltaVin/100
    DeltaIin = _DeltaIin/100
    dutyCicle = 0
    Lo = 0
    Co = 0
    Ce = 0
    Le = 0
    resFreq = 0
    comLe = 0
    comCe = 0
    type_ = ""
    if (Vin >= Vout):
        type_ = "Buck"
        dutyCicle = Vout / Vin
        Iin = (Vout * Iout) / Vin
        Lo = Vin / (4 * Freq * DeltaI * Iout)
        Co = Vin / (31 * Lo * Freq * Freq * DeltaV * Vout)
        Ce = Iout / (4 * Freq * DeltaVin * Vin)
        Le = Iout / (31 * Freq * Freq * Ce * DeltaIin * Iin)
        resFreq = 1 / (2 * math.pi * math.sqrt(Ce * Le))
        comLe = getCommercialL(Le, 1) * 1000
        comCe = getCommercialL(Ce, 1) * 1000000
        Le = 1000 * Le
        Ce = 1000000 * Ce
        # Ce = Ce.toFixed(2)
        # Le = Le.toFixed(2)
        # comCe = comCe.toFixed(2)
        # comLe = comLe.toFixed(2)
        # resFreq = resFreq.toFixed(2)
    else:
        type_ = "Boost"
        dutyCicle = 1 - (Vin / Vout)
        Lo = (Vin * dutyCicle) / (Freq * DeltaI * Iout)
        Co = Iout * (Vout - Vin) / (Vout * Freq * DeltaV * Vout)

    comLo = getCommercialL(Lo, 1) * 1000
    comCo = getCommercialL(Co, 1) * 1000000
    Lo = 1000 * Lo
    Co = 1000000 * Co

    # comLo = comLo.toFixed(2)
    # comCo = comCo.toFixed(2)

    Co = Co.toFixed(2)
    Lo = Lo.toFixed(2)

    dutyCicle = dutyCicle.toFixed(4)

    values = {dutyCicle, Lo, Co, Le, Ce, comLo,
              comCo, comLe, comCe, resFreq, type_}

    return values
