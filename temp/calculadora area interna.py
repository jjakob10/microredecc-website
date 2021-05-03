# duty cycle(ton/T); rds(on); id(on); frequencia; tr; tf; Vds(off); temperatura junção; temperatura ambiente; Rcd; Rjc; fator de correção de temperatura e fator de correção comprimento

def potcom(f, tr, tf, id, Voff):
    p = (f/2)*(tr+tf)*id*Voff
    return p


def potcond(ton, T, rds, id):
    p = (ton/T)*rds*id*id
    return p


def rja(tj, tam, p1, p2):
    rja = (tj-tam) / (p1+p2)
    return rja


def rda(rja, rcd, rjc):
    rda = rja-rcd-rjc
    return rda


def disscor(rda, ft, fc):
    disscor = rda*ft*fc
    return disscor


def aocup(afio, voltas):
    aocup = afio * voltas
    return aocup


def comparar(anuc, aocup):
    r = anuc > aocup*2
    return r
